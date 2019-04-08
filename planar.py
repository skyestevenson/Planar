import uuid

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
