import bpy

from bpy.types import Panel

class MyPanel(Panel):
    bl_label = "My Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        column = layout.column()
        column.operator("object.hide_selection", icon='HIDE_ON')
        column.operator("object.unhide_selection", icon='HIDE_OFF')
        
        box = column.box()
        box.prop(scene.my_props, "viewport")
        box.prop(scene.my_props, "render")  
        box.prop(scene.my_props, "keyframe")
        
def register():
    bpy.utils.register_class(MyPanel)
    
def unregister():
    bpy.utils.unregister_class(MyPanel)