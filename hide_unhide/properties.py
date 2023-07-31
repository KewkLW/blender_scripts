import bpy

from bpy.types import PropertyGroup
from bpy.props import BoolProperty

class MyProperties(PropertyGroup):

    viewport: BoolProperty(name="Viewport", default=True)
    render: BoolProperty(name="Render", default=True)
    keyframe: BoolProperty(name="Keyframe", default=False)

def register():
    bpy.utils.register_class(MyProperties)
    bpy.types.Scene.my_props = bpy.props.PointerProperty(type=MyProperties)

def unregister():
    del bpy.types.Scene.my_props
    bpy.utils.unregister_class(MyProperties)