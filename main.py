import os, shutil, requests, random
from serpapi import GoogleSearch
from PIL import Image

""" Algorithm for replicating assets folder structure for resourcepack
1. Recursively copy over assets folder into root folder.
2. Remove extraneous files that were copied over.
3. Create the pack.mcmeta file with the correct version number and description.
4. Use API to load images
5. Create a list of .png file paths that needs to be replaced
6. Replace .png files with results

Rules
- pack.png will be used as the resourcepack's icon.
- The assets folder will be used as the repository for copying.
"""

# Customize resourcepack here
resourcepack_name = "Animals Pack"
resourcepack_description = "Animals, only Animals"
resourcepack_theme = "Animals"
version = 8

# 1. Recursively copy over assets folder into root folder.
print("Copying over directories...")

shutil.copytree("assets", "{}/assets".format(resourcepack_name))

# 2. Remove extraneous files that were copied over.
print("Removing extraneous files...")

extraneous_files = [
  "assets/.mcassetsroot",
  "assets/minecraft/gpu_warnlist.json",
  "assets/minecraft/regional_compliancies.json"
]
extraneous_folders = [
  "assets/realms",
  "assets/minecraft/blockstates",
  "assets/minecraft/font",
  "assets/minecraft/lang",
  "assets/minecraft/models",
  "assets/minecraft/particles",
  "assets/minecraft/shaders",
  "assets/minecraft/texts",

  "assets/minecraft/textures/colormap",
  "assets/minecraft/textures/effect",
  "assets/minecraft/textures/font",
  "assets/minecraft/textures/gui"
]

for file in extraneous_files:
  print("Removed {}".format(file))
  os.remove("{}/{}".format(resourcepack_name, file))
for folder in extraneous_folders:
  print("Removed {}".format(folder))
  shutil.rmtree("{}/{}".format(resourcepack_name, folder))

# 3. Create the pack.mcmeta file with the correct version number and description.
print("Creating custom pack.mcmeta...")

pack_mcmeta = open("{}/{}".format(resourcepack_name, "pack.mcmeta"), "w")
pack_mcmeta.write("""{
  "pack": {
    "pack_format": """ + str(version) + """,
    "description": \"""" + resourcepack_description + """\"
  }
}""")

# 4. Use API to load images
print("Making API call...")

api_key = "a0b8a19fa287d33e0680eb4f816e957014ec1bbce1598710b752265f1bb9bebe"
params = {
  "api_key": "{}".format(api_key),
  "engine": "google",
  "q": "{}".format(resourcepack_theme),
  "location": "Austin, Texas, United States",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en",
  "tbm": "isch"
}

search = GoogleSearch(params)
results = search.get_dict()["images_results"]

print("Returned {} results".format(len(results)))

# 5. Create a list of .png file paths that needs to be replaced
print("Creating list of file paths...")

image_paths = ["{}/{}/pack.png".format(os.getcwd(), resourcepack_name)]
directories = ["{}/{}/assets/minecraft/textures".format(os.getcwd(), resourcepack_name)]

while len(directories) != 0:
    current_search = directories.copy()
    for directory in current_search:
        for item in os.listdir(directory):
            if item.endswith(".png"):
                image_paths.append("{}/{}".format(directory, item))
            elif item.endswith(".mcmeta"):
                pass
            else:
                directories.append("{}/{}".format(directory, item))
        directories.remove(directory)

# 6. Replace .png files with results
print("Replacing {} images...".format(len(image_paths)))

for image_path in image_paths:
  url = results[random.randrange(0, len(results) - 1)]["thumbnail"]
  image = Image.open(requests.get(url, stream=True).raw)
  image.save(image_path)

print("Operation Complete!")