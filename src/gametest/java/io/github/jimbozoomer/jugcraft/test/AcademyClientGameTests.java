package io.github.jimbozoomer.jugcraft.test;

import java.util.Locale;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestServerContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.minecraft.client.gui.screens.worldselection.WorldCreationUiState;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.Blocks;

/** Real-client views for review; these are not human playtest evidence. */
public final class AcademyClientGameTests implements FabricClientGameTest {
	@Override
	public void runTest(ClientGameTestContext context) {
		context.runOnClient(c -> c.options.renderDistance().set(10));
		try (TestSingleplayerContext world = context.worldBuilder()
				.adjustSettings(c -> c.setGameMode(WorldCreationUiState.SelectedGameMode.CREATIVE)).create()) {
			TestServerContext server = world.getServer();
			server.runCommand("time set noon");
			server.runCommand("weather clear");
			server.runCommand("forceload add 0 0 96 120");
			// Only this disposable test world: explicitly clear the preview volume above the landscape.
			server.runOnServer(s -> {
				for (int x = 0; x < 97; x++) {
					for (int z = 0; z < 121; z++) {
						for (int y = 224; y < 300; y++) {
							BlockPos pos = new BlockPos(x, y, z);
							if (!s.overworld().getBlockState(pos).isAir()) {
								s.overworld().setBlock(pos, Blocks.AIR.defaultBlockState(), 2);
							}
						}
					}
				}
			});
			server.runCommand("place template jugcraft:academy/winterhold 0 224 0");
			server.runOnServer(s -> {
				if (s.overworld().getBlockEntity(new BlockPos(37, 249, 24)) == null) {
					throw new AssertionError("Academy placement did not create the study bench");
				}
			});
			context.getInput().pressKey(options -> options.keyToggleGui);
			context.runOnClient(c -> c.options.fov().set(75));
			view(context, server, 113, 307, 145, 147, 20);
			world.getConnection().waitForChunksRender();
			context.takeScreenshot("jugcraft_academy_overview");
			view(context, server, 48, 251, 113, 180, -5);
			context.takeScreenshot("jugcraft_academy_bridge");
			view(context, server, 48, 252, 41, 180, 0);
			context.takeScreenshot("jugcraft_academy_hall");
			view(context, server, 48, 266, 39, 180, 5);
			context.takeScreenshot("jugcraft_academy_library");
			view(context, server, 48, 278, 38, 180, 10);
			context.takeScreenshot("jugcraft_academy_archmage");
			view(context, server, 23, 244, 34, 180, 10);
			context.takeScreenshot("jugcraft_academy_midden_forge");
			view(context, server, 51, 244, 65, 155, 5);
			context.takeScreenshot("jugcraft_academy_echo_chamber");
			server.runCommand("forceload remove 0 0 96 120");
			context.getInput().pressKey(options -> options.keyToggleGui);
		}
	}

	private static void view(ClientGameTestContext context, TestServerContext server,
			double x, double y, double z, float yaw, float pitch) {
		server.runOnServer(s -> {
			var player = s.getPlayerList().getPlayers().getFirst();
			player.getAbilities().flying = true;
			player.onUpdateAbilities();
		});
		server.runCommand(String.format(Locale.ROOT, "tp @p %.2f %.2f %.2f %.1f %.1f", x, y, z, yaw, pitch));
		context.runOnClient(c -> {
			c.player.getAbilities().flying = true;
			c.player.onUpdateAbilities();
		});
		context.waitTicks(20);
	}
}
