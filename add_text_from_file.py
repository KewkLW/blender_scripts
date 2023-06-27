import bpy
import os
import math

def read_text_file(filename):
    with open(filename, "r") as f:
        text = f.read()
    return text

def create_text(text, font):
    curve = bpy.data.curves.new(name="TextCurve", type='FONT')
    curve.body = text
    curve.font = font
    curve.extrude = 0.14
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    
    # Creating the object
    text_object = bpy.data.objects.new(name="Text", object_data=curve)

    # Linking object to the scene
    bpy.context.collection.objects.link(text_object)
    
    # Centering the origin
    bpy.context.view_layer.objects.active = text_object
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')

    # Rotate 90 degrees about the X-axis
    text_object.rotation_euler[0] = math.pi / 2

    return text_object

def main():
    filename = "c:/tmp/text.txt"
    text = read_text_file(filename)
    # font = bpy.data.fonts["Arial"]
    font = bpy.data.fonts.get("Arial")
    if not font:
        font = bpy.data.fonts.load("c:/Windows/Fonts/Arial.ttf")
    text_object = create_text(text, font)
    text_object.name = f"{text} ({font.name})"
    text_object.location = (0, 0, 0)

if __name__ == "__main__":
    main()
