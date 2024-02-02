import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
player = mc.player

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        x,y,z = hit.pos
        if hit.face == 5:
            mc.setBlock(x, y, z, block.AIR.id)
            mc.setBlock(x-1, y, z, block.WOOL.id, 1)
        # YOUR CODE HERE
        elif hit.face == 3:
            mc.setBlock(x, y, z, block.AIR.id)
            mc.setBlock(x, y, z-1, block.WOOL.id, 1)
        elif hit.face == 4:
            mc.setBlock(x, y, z, block.AIR.id)
            mc.setBlock(x+1, y, z, block.WOOL.id, 1)
        elif hit.face == 2:
            mc.setBlock(x, y, z, block.AIR.id)
            mc.setBlock(x, y, z+1, block.WOOL.id, 1)

