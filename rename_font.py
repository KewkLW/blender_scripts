import bpy

def rename_text():
    # Get the selected text objects
    selected_text = bpy.context.selected_objects

    # Loop through the selected text objects
    for text in selected_text:
        # Get the letter and font of the text
        letter = text.data.body[0]
        font = text.data.font.name

        # Rename the text object
        new_name = f"{letter} ({font})"
        text.name = new_name

# Run the script
rename_text()
