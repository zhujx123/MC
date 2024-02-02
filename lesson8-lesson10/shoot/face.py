import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
player = mc.player

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        mc.postToChat(hit.face)