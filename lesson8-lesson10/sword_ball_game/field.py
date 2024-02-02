import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
player = mc.player
x, y, z = player.getTilePos()
print(x,y,z)
# car field -805 0 976
# ice -491 29 1013

# 草地
mc.setBlocks(x-29, y, z-19, x+29, y, z+19, block.WOOL.id, 0)
mc.setBlocks(x-28, y, z-18, x+28, y, z+18, block.WOOL.id, 13)
# # 中线
# mc.setBlocks(x, y, z-19, x, y, z+19, block.WOOL.id, 0)
# # # 球场分区羊毛底
# mc.setBlocks(x+29,y,z-9,x+17,y,z+9,block.WOOL.id,0)
# mc.setBlocks(x-29,y,z-9,1x-17,y,z+9,block.WOOL.id,0)
# # # 球场分区
# mc.setBlocks(x+28,y,z-8,x+18,y,z+8,block.WOOL.id,13)
# mc.setBlocks(x-28,y,z-8,x-18,y,z+8,block.WOOL.id,13)

# mc.setBlocks(x,y,z,x,y,z,block.WOOL.id,0)
mc.setBlock(x,y,z,block.STONE)
