import uuid
import json
import os

# the metaplane is the top level of the planar system - a 0-1 2D map of each planar file, associated with its own specific coordinates

metaplane = {}

# load metaplane from file
def load(file_name = "metaplane.json"):
    try:
        meta_file = open(file_name)
        metaplane = json.load(meta_file)
        print("Metaplane file loaded!")
    except:
        print("No metaplane file found. Creating one.")
        export()
        load()

# export the result
def export(file_name = "metaplane.json"):
    # turn dict object into JSON
    json_out = json.dumps(metaplane, indent = 1)

    # write JSON to file
    out_file = open(file_name,"w")
    out_file.write(json_out)
    out_file.close()

    print("Metaplane file exported.")

def purge(file_name = "metaplane.json"):
    user_input = raw_input("This will delete the file {}. Are you sure? [Y/N]".format(file_name))
    if (user_input.lower() == "y"):
        os.remove(file_name)
        print("{} deleted.".format(file_name))
    else:
        print("Cancelled.")

# add a new plane to the system
def register(coordinates, file_name):
    # TODO check that coordinates are a tuple with 2 numbered elements in a range of 0-1
    metaplane[str(coordinates)] = file_name

#### MAIN PROGRAM ####
load()
