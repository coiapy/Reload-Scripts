bl_info = {
    "name": "Reloads Scripts in Production (RSP)",
    "description": "Reloads Scripts",
    "author": "Javier Aira",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > UI > Tool > Reloads Scripts",
    "category": "3D View",
}


import sys

if "bpy" in locals():
    if __name__ in sys.modules:
        del sys.modules[__name__]

    dotted = __name__ + "."
    for name in tuple(sys.modules):
        if name.startswith(dotted):
            del sys.modules[name]


###################################
from .panels import *
from .operators import *
#from .file import * 

###################################

import bpy


classes = (
    ReloadM,
    DirP,
    VIEW_3D_PT_ReloadS
    )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)