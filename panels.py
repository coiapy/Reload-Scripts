import bpy
import sys

class VIEW_3D_PT_ReloadS(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    bl_label = 'Reload Scripts'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 90

    def draw(self, context):
        layout = self.layout
        title =(f'Folders sys.path: {len(sys.path)}')
        layout.label(text=title, icon='FILE_SCRIPT')

        split = layout.split(factor=0.50, align=True)
        split.operator('newreload.reload', text='Reload', icon='FILE_REFRESH')
        split.operator('newreload.dir_path', text='sys.path', icon='INFO')