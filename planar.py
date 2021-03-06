import uuid
import json
import os

# initialize plane
def init(
    name = "World",
    description = "This is a virtual world.",
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
        "assets" : [],
        "global_properties" : {},
        "environment" : {},
        "objects" : {},
        "links" : []
    }
    plane["global_properties"] = {
        "name" : name,
        "description" : description,
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
    # add asset to asset list
    add_asset(asset)

# add asset path to global asset list
def add_asset(path):
    # only add it if it's not in the asset list already
    if path not in plane["assets"]:
        plane["assets"].append(path)

# set up the skybox from an asset
def set_skybox(image):
    plane["environment"]["skybox"] = image
    add_asset(image)

# set up terrain
def set_terrain(
    heightmap,
    dimensions = (1000, 1000)
):
    plane["environment"]["terrain"] = {
        "dimensions" : dimensions,
        "heightmap" : heightmap
    }
    add_asset(heightmap)

# add a link to the plane
def add_link(
    location = (0, 0, 0),
    destination = (0, 0, 0)
):
    plane["links"].append({
        "location" : location,
        "destination" : destination 
    })

# export the result
def export(plane, file_name = "planar_test.irl"):
    # turn dict object into JSON
    json_out = json.dumps(plane, indent = 1)

    # write JSON to file
    out_file = open(file_name,"w")
    out_file.write(json_out)
    out_file.close()

    # report file size
    print("JSON file size: {}kB".format(os.path.getsize(file_name) / 1000.0))
