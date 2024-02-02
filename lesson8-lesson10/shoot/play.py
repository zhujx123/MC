import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
player = mc.player
x,y,z = mc.player.getTilePos()
mc.setBlock(x, y, z, block.WOOL.id, 1)

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        x1,y1,z1 = hit.pos
        if (x,y,z) == (x1,y1,z1):
            mc.setBlock(x, y, z, block.AIR.id)
            if hit.face == 5:
                mc.setBlock(x-1, y, z, block.WOOL.id, 1)
                x -= 1
            elif hit.face == 3:
                mc.setBlock(x, y, z-1, block.WOOL.id, 1)
                z -= 1
            elif hit.face == 4:
                mc.setBlock(x+1, y, z, block.WOOL.id, 1)
                x += 1
            elif hit.face == 2:
                mc.setBlock(x, y, z+1, block.WOOL.id, 1)
                z += 1