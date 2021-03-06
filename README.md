# Minecraft-Resource-Pack-Generator
Generate a themed resource pack for any version of Minecraft using Python. 

## Usage
1. Get your FREE API key through Serpapi at https://serpapi.com
2. Install the required dependencies
```
pip install -r requirements.txt
```
3. Copy the assets folder of the Minecraft version that you wish to generate the resource pack for into the root of this project. Located in "C:/Users/username/AppData/Roaming/.minecraft/versions/version/version.jar".
4. Using your API key from Serpapi, run main.py.
```
python main.py <API-Key>
```
5. Follow the prompts to name your resource pack and choose the theme.
```
Resource Pack Name (Separate spaces with "-"): My-First-Resourcepack
Description (Separate spaces with "-"): This-is-my-first-resourcepack
Resource Pack Theme (Separate spaces with "-"): The-Legend-Of-Zelda
-Version-
1 for versions 1.6.1 - 1.8.9
2 for versions 1.9 - 1.10.2
3 for versions 1.11 - 1.12.2
4 for versions 1.13 - 1.14.4
5 for versions 1.15 - 1.16.1
6 for versions 1.16.2 - 1.16.5
7 for versions 1.17.x
8 for versions 1.18.x
9 for versions 1.19.x

Enter a number 1-9: 8
```

6. Once the script completes, Launch Minecraft and apply the resource pack by moving your newly created folder into the resource packs folder for Minecraft. The destination is "C:/Users/username/AppData/Roaming/.minecraft/resourcepacks".
![Resource Packs](/screenshots/minecraft1.png?raw=true "Resource Packs")
![Folder Destination](/screenshots/minecraft2.png?raw=true "Folder Destination")
![Outcome](/screenshots/minecraft3.png?raw=true "Outcome")
8. Test the resource pack in your world or on a server.
![Testing](/screenshots/minecraft4.png?raw=true "Testing")
