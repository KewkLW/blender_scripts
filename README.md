# 3D Text Creator in Blender
add_text_from_file.py
This script uses the Python API for [Blender](https://www.blender.org/), a free and open-source 3D computer graphics software toolset, to create 3D text objects from a text file. It uses a specified font to render the text in 3D and positions it at the origin of the scene.

## Requirements

- Blender 2.9x or above
- Python 3.7 or above

## Usage

1. Save the script in the same directory where you plan to run it.

2. Open Blender and go to the scripting workspace. Click on 'Open' and navigate to the directory where you saved the script. Select the script and click 'Open Text Block'.

3. In the `main` function, modify the `filename` variable to point to the text file you want to use. By default, it is set to "c:/tmp/text.txt".

4. If you want to use a font other than Arial, modify the `font` variable in the `main` function. Make sure to provide the full path to the .ttf file. 

5. Run the script in Blender by clicking the 'Run Script' button or by pressing Alt + P.

## Code Overview

The script has the following key functions:

- `read_text_file(filename)`: This function reads a text file and returns its contents as a string.

- `create_text(text, font)`: This function creates a 3D text object in Blender. It takes two arguments - `text` which is the string to render in 3D, and `font` which is the font to use for the text.

- `main()`: This is the main function of the script. It reads the text from a specified file, loads the specified font, creates a 3D text object, and positions it at the origin of the scene.

## Note

Ensure that the Blender application is able to access the file paths specified in the script.


# Blender Text Renaming Tool

This script is a utility tool for [Blender](https://www.blender.org/), a free and open-source 3D computer graphics software toolset. The script uses the Python API for Blender to rename selected text objects in the scene.

## Requirements

- Blender 2.9x or above
- Python 3.7 or above

## Usage

1. Save the script in the same directory where you plan to run it.

2. Open Blender and go to the scripting workspace. Click on 'Open' and navigate to the directory where you saved the script. Select the script and click 'Open Text Block'.

3. Before running the script, make sure to select the text objects in the scene that you want to rename.

4. Run the script in Blender by clicking the 'Run Script' button or by pressing Alt + P.

## Code Overview

The script contains a single function, `rename_text()`, which gets executed when you run the script.

- `rename_text()`: This function renames all selected text objects in the scene. The new name of each text object is composed of the first letter of the text and the name of the font, separated by a space and enclosed in parentheses. For example, if the text is "Hello" and the font is "Arial", the new name of the text object will be "H (Arial)".

## Note

Ensure that the text objects you want to rename are selected before running the script.

# Blender Multi-Camera Renderer

This script uses the Python API for [Blender](https://www.blender.org/), a free and open-source 3D computer graphics software toolset, to render the scene from the perspective of each camera in the scene.

## Requirements

- Blender 2.9x or above
- Python 3.7 or above

## Usage

1. Save the script in the same directory where your Blender project file is located.

2. Open Blender and go to the scripting workspace. Click on 'Open' and navigate to the directory where you saved the script. Select the script and click 'Open Text Block'.

3. Run the script in Blender by clicking the 'Run Script' button or by pressing Alt + P.

## Code Overview

The script contains a single function, `render_all_cameras(context)`, which gets executed when you run the script.

- `render_all_cameras(context)`: This function iterates over all objects in the scene, finds the cameras, sets each camera as the active camera in turn, and then renders the scene to a file. The rendered image files are saved in a directory named "/tmp/renders/" within the directory where the Blender project file is located. The name of each file is the same as the name of the camera used to render it.

## Note

Ensure that the Blender application is able to access the directory where you plan to save the rendered images. Also, make sure that there is a "/tmp/renders/" directory in the same location as your Blender project file, as this is where the script will save the rendered images.
