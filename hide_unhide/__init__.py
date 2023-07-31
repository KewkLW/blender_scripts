bl_info = {
    "name": "Hide Unhide",
    "author": "Kewk",
    "version": (1, 0),
    "blender": (2, 30, 0),
    "location": "View3D > Sidebar > MotionPath > Anim Tools",
    "description": "Adds Hide/Unhide operators",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy

from . import ui
from . import operators
from . import properties

modules = (
    ui,
    operators,
    properties
)

def register():
    for module in modules:
        module.register()

def unregister():
    for module in modules:
        module.unregister()
        
if __name__ == "__main__":
    register()