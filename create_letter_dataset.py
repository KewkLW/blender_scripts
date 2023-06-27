import os
import bpy

def load_fonts(font_directory):
    fonts = []
    for file in os.listdir(font_directory):
        if file.endswith(".ttf") or file.endswith(".otf"):  # you can add other font file extensions if necessary
            font_path = os.path.join(font_directory, file)
            font = bpy.data.fonts.load(font_path)
            fonts.append(font)
    return fonts

def main():
    font_directory = "c:/Windows/Fonts"  # change this to your font directory
    fonts = load_fonts(font_directory)

    filename = "c:/tmp/text.txt"
    with open(filename, "r") as f:
        for line in f:
            text = line.strip()
            for font in fonts:
                text_object = create_text(text, font)
                text_object.name = f"{text} ({font.name})"
                text_object.location = (0, 0, 0)

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

def render_all_cameras(context, font_name):
    scene = context.scene
    for ob in scene.objects:
        if ob.type == "CAMERA":
            bpy.context.scene.camera = ob
            file = os.path.join(os.path.dirname(bpy.data.filepath), f"/tmp/renders/{font_name}/", ob.name)
            bpy.context.scene.render.filepath = file
            bpy.ops.render.render(write_still=True)

def main():
    font_directory = "c:/Windows/Fonts"  # change this to your font directory
    fonts = load_fonts(font_directory)

    filename = "c:/tmp/text.txt"
    with open(filename, "r") as f:
        for line in f:
            text = line.strip()
            for font in fonts:
                text_object = create_text(text, font)
                text_object.name = f"{text} ({font.name})"
                text_object.location = (0, 0, 0)
                render_all_cameras(bpy.context, font.name)

if __name__ == "__main__":
    main()