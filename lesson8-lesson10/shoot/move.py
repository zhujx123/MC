import time
import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
player = mc.player
x,y,z = player.getTilePos()
x += 1
mc.setBlock(x,y,z,block.WOOL.id,1)
time.sleep(1)

# YOUR CODE HERE
mc.setBlock(x,y,z, block.AIR.id)
mc.setBlock(x+1,y,z, block.WOOL.id, 1)


