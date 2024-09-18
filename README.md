# Reload Scripts
Reloads all installed scripts (official, community and user).
User scripts must have __init__.py at the beginning of their file:

Recarga todos los script instalados (oficiales, comunidad y usuario).
Los scripts de ususario deben tener en el inicio de su archivo __init__.py:

```python
#bl_info = {}

import sys

if "bpy" in locals():
    if __name__ in sys.modules:
        del sys.modules[__name__]

    dotted = __name__ + "."
    for name in tuple(sys.modules):
        if name.startswith(dotted):
            del sys.modules[name]


#######################################
#Each imported file must be done like this:
#Cada archivo importado debe hacerse de esta forma:
#from .file import *

from .panels import *
from .operators import *

# ...
#######################################

import bpy
#Rest of code / Resto de codigo

```

# Installation
1. Edit -> Preferences -> Add-ons and click "Install"
2. Enable the Add-on
# Usage
"location": "View3D > UI > Tool > Reloads Scripts"

# Tags
#Blender #Python #scripts #addon
