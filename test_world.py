import planar

######## CREATE WORLD ########
planar.init(
    name = "Aetheria",
    description = "This is the first Plane created with the Planar system. Basically, just a testbed."
)
planar.set_skybox("HDRI_Night.exr")
planar.set_terrain(heightmap = "LandscapeHeight.png")
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
planar.add_link(
    location = (100, 150, 1.5),
    destination = (500, 500, 500)
)







# finally, save to file!
planar.export(plane = planar.plane)

#### LOOKING AT THE DATA ####
import os
import json
world = open("planar_test.irl")
world = json.load(world)

print("\n{}\n{}".format(world["global_properties"]["name"], world["global_properties"]["description"]))

print("\nGlobal Properties:")
print("Gravity: {}m/s^2".format(world["global_properties"]["gravity"]))

print("\nAsset list:")
for asset in world["assets"]:
    print(asset)

print("\nObjects:")
for key, value in world["objects"].items():
    print("{}\n- asset: {}\n- physics enabled: {}\n- location: {}".format(key, value["asset"], value["physics_enabled"], value["transform"]["t"]))
