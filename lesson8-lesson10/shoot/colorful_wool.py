import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
player = mc.player

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        x,y,z = hit.pos
        if hit.face == 5:
            mc.setBlock(x, y, z, block.WOOL.id, 14)
        elif hit.face == 3:
            mc.setBlock(x, y, z, block.WOOL.id, 3)
        # YOUR CODE HERE
        elif hit.face == 4:
            mc.setBlock(x, y, z, block.WOOL.id, 4)
        elif hit.face == 2:
            mc.setBlock(x, y, z, block.WOOL.id, 5)
        elif hit.face == 1:
            mc.setBlock(x, y, z, block.WOOL.id, 0)
        elif hit.face == 0:
            mc.setBlock(x, y, z, block.WOOL.id, 15)