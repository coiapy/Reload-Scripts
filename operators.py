import bpy
import sys


def ShowMessageBox(title = "Message Box", icon = 'INFO', lines=""):
    myLines=lines
    def draw(self, context):
        for n in myLines:
            self.layout.label(text=n)
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

def funcion_timers():
    sys.path = list(set(sys.path))
    for area in bpy.context.window.screen.areas:
        if area.type == 'VIEW_3D':
            area.tag_redraw()


class ReloadM(bpy.types.Operator):#newreload.reload
    """• Reload All Addons"""
    bl_idname = "newreload.reload"
    bl_label = "• Reload All Addons"

    def execute(self, context):
        sys.path = list(set(sys.path))
        bpy.ops.script.reload()
        bpy.app.timers.register(funcion_timers, first_interval=1)
        return {'FINISHED'}


class DirP(bpy.types.Operator): #dir_path
    """• List Folders path"""
    bl_idname = "newreload.dir_path"
    bl_label = "Dir Path"

    def execute(self, context):
        sys.path = list(set(sys.path))
        li =[]
        title =(f'Nº Folders in sys.path: {len(sys.path)}')
        for i in sys.path:
            li.append(str(i))
        ShowMessageBox(title=title, icon='INFO', lines=li)
        return {'FINISHED'}