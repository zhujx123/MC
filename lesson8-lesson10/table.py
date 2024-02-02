import time
import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
player = mc.player
x,y,z = player.getTilePos()

# for i in range(40):
#     for j in range(40):
#         mc.setBlock(x+i, y, z+j, block.STONE)

mc.setBlock(x,y,z,block)
