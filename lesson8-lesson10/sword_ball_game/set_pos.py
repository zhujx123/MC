import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
player = mc.player
x, y, z = player.getTilePos()
# print(x,y,z)
# car field -805 0 976
# player.setPos(-805, 0, 976)
# ice -491 29 1013
# player.setPos(-491, 29, 1013)

mc.setBlocks(x,y,z,x+10,y,z+10,block.WOOL)
