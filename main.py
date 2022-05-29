import os, shutil, requests, random, sys
from extraneous import extraneous_files, extraneous_folders
from serpapi import GoogleSearch
from PIL import Image

""" Algorithm for replicating assets folder structure for resource pack
1. Recursively copy over assets folder into root folder.
2. Remove extraneous files that were copied over.
3. Create the pack.mcmeta file with the correct version number and description.
4. Use API to load images
5. Create a list of .png file paths that needs to be replaced
6. Replace .png files with results

Information
- The assets folder will be used as the repository for copying.
- You will need an API key from https://serpapi.com 
"""

# Get user input
if len(sys.argv) != 2:
  print("ERROR: You need to provide an API key from https://serpapi.com")
  print("Usage: python main.py API-KEY")
  sys.exit()

api_key = sys.argv[1]

resourcepack_name_input = input("Resource Pack Name (Separate spaces with \"-\"): ").split("-")
resourcepack_name = " ".join(resourcepack_name_input)
resourcepack_description_input = input("Description (Separate spaces with \"-\"): ").split("-")
resourcepack_description = " ".join(resourcepack_description_input)
resourcepack_theme_input = input("Resource Pack Theme (Separate spaces with \"-\"): ")
resourcepack_theme = " ".join(resourcepack_theme_input)

print("""-Version-
1 for versions 1.6.1 - 1.8.9
2 for versions 1.9 - 1.10.2
3 for versions 1.11 - 1.12.2
4 for versions 1.13 - 1.14.4
5 for versions 1.15 - 1.16.1
6 for versions 1.16.2 - 1.16.5
7 for versions 1.17.x
8 for versions 1.18.x
9 for versions 1.19.x""")
version = input("\nEnter a number 1-9: ")

print("\nStarting script...")

# 1. Recursively copy over assets folder into root folder.
print("Copying over directories from assets folder...")

shutil.copytree("assets", "{}/assets".format(resourcepack_name))

# 2. Remove extraneous files that were copied over.
print("Removing extraneous files...")

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
            elif item.endswith(".mcmeta") or item.endswith(".json"):
                pass
            else:
                directories.append("{}/{}".format(directory, item))
        directories.remove(directory)

# 6. Replace .png files with results
print("Replacing {} images...".format(len(image_paths)))

i = 0
result_count = len(results)
image_count = len(image_paths)
for image_path in image_paths:
  url = results[random.randrange(0, result_count - 1)]["thumbnail"]
  image = Image.open(requests.get(url, stream=True).raw)
  image.save(image_path)

  i += 1
  percent_complete = i * 100 / image_count
  print("{0:.2f}% complete".format(percent_complete))

print("Operation Complete!")