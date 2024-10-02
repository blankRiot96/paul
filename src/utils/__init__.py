"""
A progressive `utils` package that is transferred from
one game to the next and keeps growing in functionality.

To use:
```
git clone https://github.com/blankRiot96/pgbase new_project_name
cd new_project_name
source base_setup.sh
```

But I have a file in `~/.local/bin` called `newpg` that basically shortens
the cloning step to `newpg new_project_name`.

After my new project is completed, I transfer the updated `utils` package
back to `pgbase` like so:
```
cp -r src/utils ~/p/pgbase/src/utils
```
"""

from .camera import Camera
from .components import Components
from .systems import System
from .tmx import MapReader
from .world import World
