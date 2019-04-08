import json
import uuid
import os

# this is a high-level description of a game / vr world - endgame is to write compilers that take this language and reconstruct the environment and its basic multiplayer properties in any engine; basically, it's like HTML but for virtual worlds

# initialize plane
def init_plane(
    name = "World",
    population_max = 100,
    boundaries = {
        "x" : (-1000, 1000),
        "y" : (-1000, 1000),
        "z" : (-1000, 1000)
    },
    player_start = (0, 0, 0),
    gravity = -9.8
):
    global plane
    plane = {
        "global_properties" : {},
        "objects" : {}
    }
    plane["global_properties"] = {
        "name" : name,
        "population_max" : population_max,
        "boundaries" : boundaries,
        "player_start" : player_start,
        "gravity" : gravity
    }

# add an object to the plane, with a unique id
def add_object(
    asset = "",
    transform = {
        "t" : (0, 0, 0),
        "r" : (0, 0, 0),
        "s" : (1, 1, 1)
    },
    physics_enabled = False
):
    # each object has a unique id
    id = str(uuid.uuid4())
    plane["objects"][id] = {
        "asset" : asset,
        "transform" : transform,
        "physics_enabled" : physics_enabled
    }

######## CREATE WORLD ########
init_plane()
add_object(
    asset = "Block.obj",
    transform = {
        "t" : (128.51, 33.27, 0.78),
        "r" : (33.27, 77,8, 12.03),
        "s" : (1, 1, 1)
    },
    physics_enabled = True
)

json_out = json.dumps(plane, indent = 1)

# export the result
outName = "planar_test.irl"
outFile = open(outName,"w")
outFile.write(json_out)
outFile.close()

# report file size
print("JSON file size: {}kB".format(os.path.getsize(outName) / 1000.0))
