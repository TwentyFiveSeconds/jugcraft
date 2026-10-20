package io.github.jimbozoomer.jugcraft.test;

import io.github.jimbozoomer.jugcraft.Jugcraft;
import io.github.jimbozoomer.jugcraft.concordance.BenchStatus;
import io.github.jimbozoomer.jugcraft.concordance.ConcordanceProgress;
import io.github.jimbozoomer.jugcraft.concordance.CrucibleBlockEntity;
import io.github.jimbozoomer.jugcraft.concordance.JugcraftConcordance;
import io.github.jimbozoomer.jugcraft.concordance.KindledLanternItem;
import io.github.jimbozoomer.jugcraft.concordance.LampwrightBenchBlockEntity;
import io.github.jimbozoomer.jugcraft.concordance.rules.ResearchState;
import java.io.IOException;
import net.fabricmc.fabric.api.gametest.v1.GameTest;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.nbt.NbtAccounter;
import net.minecraft.nbt.NbtIo;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.GameType;
import net.minecraft.world.level.block.Blocks;

/** Checks the authored template against the running 26.3 registries and existing magic. */
public class AcademyGameTests {

	@GameTest
	public void academyUsesNativeBlockStates(GameTestHelper helper) {
		try (var input = helper.getLevel().getServer().getResourceManager()
				.getResourceOrThrow(Jugcraft.id("structure/academy/winterhold.nbt")).open()) {
			var tag = NbtIo.readCompressed(input, NbtAccounter.unlimitedHeap());
			var palette = tag.getListOrEmpty("palette");
			for (int i = 0; i < palette.size(); i++) {
				var entry = palette.getCompoundOrEmpty(i);
				String name = entry.getStringOr("id", "");
				var block = BuiltInRegistries.BLOCK.getValue(net.minecraft.resources.Identifier.parse(name));
				helper.assertTrue(block != Blocks.AIR || name.equals("minecraft:air"), "Unregistered academy block: " + name);
				var properties = entry.getCompoundOrEmpty("properties");
				for (String key : properties.keySet()) {
					var property = block.getStateDefinition().getProperty(key);
					helper.assertTrue(property != null && property.getValue(properties.getStringOr(key, "")).isPresent(),
							"Invalid academy state: " + name + " " + key);
				}
			}
		} catch (IOException e) {
			throw helper.assertionException("Could not read academy template: " + e);
		}
		helper.succeed();
	}

	@GameTest(structure = "jugcraft:academy/winterhold", maxTicks = 20)
	public void academyStationsRetainResearchAndIngredientCosts(GameTestHelper helper) {
		BlockPos position = new BlockPos(37, 9, 24);
		helper.assertBlockPresent(JugcraftConcordance.LAMPWRIGHT_BENCH, position);
		helper.assertBlockPresent(JugcraftConcordance.LAMPWRIGHT_BENCH, new BlockPos(59, 9, 24));
		helper.assertBlockPresent(JugcraftConcordance.CRUCIBLE, new BlockPos(22, 9, 54));
		helper.getBlockEntity(new BlockPos(22, 9, 54), CrucibleBlockEntity.class);
		helper.assertBlockPresent(BuiltInRegistries.BLOCK.getValue(Jugcraft.id("artificer_bench")), new BlockPos(74, 9, 54));
		helper.assertBlockPresent(Blocks.SPRUCE_WALL_SIGN, new BlockPos(48, 16, 48));
		var bench = helper.getBlockEntity(position, LampwrightBenchBlockEntity.class);
		var player = helper.makeMockServerPlayerInLevel();
		player.setGameMode(GameType.SURVIVAL);
		BlockPos stand = helper.absolutePos(new BlockPos(37, 9, 25));
		player.snapTo(stand.getX() + 0.5, stand.getY(), stand.getZ() + 0.5, 180.0F, 0.0F);
		bench.setItem(LampwrightBenchBlockEntity.SPECIMEN, new ItemStack(Items.AMETHYST_SHARD));
		bench.setItem(LampwrightBenchBlockEntity.WORK, new ItemStack(Items.LANTERN));
		helper.assertTrue(bench.status(player, LampwrightBenchBlockEntity.BUTTON_KINDLE) == BenchStatus.UNKNOWN_RESEARCH
				&& !bench.press(player, LampwrightBenchBlockEntity.BUTTON_KINDLE), "Visiting the college must not bypass research");
		ConcordanceProgress.grant(player, "jugcraft:first_light", ResearchState.UNDERSTOOD);
		helper.assertTrue(bench.press(player, LampwrightBenchBlockEntity.BUTTON_KINDLE), "A learned player can use the placed bench");
		var lantern = bench.getItem(LampwrightBenchBlockEntity.WORK);
		helper.assertTrue(lantern.is(JugcraftConcordance.KINDLED_LANTERN)
				&& KindledLanternItem.remaining(lantern, helper.getLevel().getGameTime()) == 8
				&& bench.getItem(LampwrightBenchBlockEntity.SPECIMEN).isEmpty(), "The existing recipe consumes the player's specimen");
		helper.succeed();
	}
}
