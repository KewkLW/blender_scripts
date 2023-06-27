import bpy
import os

def render_all_cameras(context):
    scene = context.scene
    for ob in scene.objects:
        if ob.type == "CAMERA":
            bpy.context.scene.camera = ob
            file = os.path.join(os.path.dirname(bpy.data.filepath), "/tmp/renders/", ob.name)
            bpy.context.scene.render.filepath = file
            bpy.ops.render.render(write_still=True)

if __name__ == "__main__":
    render_all_cameras(bpy.context)