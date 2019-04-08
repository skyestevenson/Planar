import json
import os
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

json_out = json.dumps(planar.plane, indent = 1)

# export the result
outName = "planar_test.irl"
outFile = open(outName,"w")
outFile.write(json_out)
outFile.close()

# report file size
print("JSON file size: {}kB".format(os.path.getsize(outName) / 1000.0))
