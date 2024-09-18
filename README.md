# Reload Scripts
Reloads all installed scripts

## Reload Scripts
Reloads all installed scripts (official, community and user ... including panels).
User scripts must have \_\_init\_\_.py at the beginning of their file:

Recarga todos los script instalados (oficiales, comunidad y usuario ... incluído paneles!).
Los scripts de ususario deben tener en el inicio de su archivo \_\_init\_\_.py:

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
#code

```

## Installation
1. Edit -> Preferences -> Add-ons and click "Install"
2. Enable the Add-on
## Usage
"location": "View3D > UI > Tool > Reloads Scripts"

![imagen](https://github.com/coiapy/Reload-Scripts/blob/main/reload_scripts.png)

## Tags
#Blender #Python #scripts #addon
