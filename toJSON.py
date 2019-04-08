import planar

######## CREATE WORLD ########
planar.init_plane()
planar.add_object(
    asset = "Block.obj",
    transform = {
        "t" : (128.51, 33.27, 0.78),
        "r" : (33.27, 77,8, 12.03),
        "s" : (1, 1, 1)
    },
    physics_enabled = True
)
planar.add_object(
    asset = "Wall.obj"
)

# finally, save to file!
planar.export(plane = planar.plane)
