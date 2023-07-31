import bpy

from bpy.props import BoolProperty, CollectionProperty
from bpy.types import Operator

class HideOperator(Operator):
    """Hide selection"""
    bl_idname = "object.hide_selection"
    bl_label = "Hide"

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        props = context.scene.my_props
        
        for obj in context.selected_objects:
            if props.viewport:
                obj.hide_viewport = True
                
            if props.render:
                obj.hide_render = True
                
            if props.keyframe:
                obj.keyframe_insert('hide_viewport')
                obj.keyframe_insert('hide_render')
                
        return {'FINISHED'}
        
class UnhideOperator(Operator):
    """Unhide selection"""
    bl_idname = "object.unhide_selection" 
    bl_label = "Unhide"

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        props = context.scene.my_props
        
        for obj in context.selected_objects:
            if props.viewport: 
                obj.hide_viewport = False
                
            if props.render:
                obj.hide_render = False
                
            if props.keyframe:
                obj.keyframe_insert('hide_viewport')
                obj.keyframe_insert('hide_render')
                
        return {'FINISHED'}
        
def register():
    bpy.utils.register_class(HideOperator)
    bpy.utils.register_class(UnhideOperator)
    
def unregister():
    bpy.utils.unregister_class(HideOperator)
    bpy.utils.unregister_class(UnhideOperator)