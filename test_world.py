import planar

######## CREATE WORLD ########
planar.init()
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

#### LOOKING AT THE DATA ####
import os
import json
world = open("planar_test.irl")
world = json.load(world)

print("\nGlobal Properties:")
print("Gravity: {}m/s^2".format(world["global_properties"]["gravity"]))

print("\nAsset list:")
for asset in world["assets"]:
    print(asset)

print("\nObjects:")
for key, value in world["objects"].items():
    print("{}\n- asset: {}\n- physics enabled: {}\n- location: {}".format(key, value["asset"], value["physics_enabled"], value["transform"]["t"]))
