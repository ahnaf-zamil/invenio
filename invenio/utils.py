# Copyright 2022 DevGuyAhnaf
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ._about import __version__, __copyright__

import sys
import platform

nl = "\n"

banner = f"""
d888888b d8b   db db    db d88888b d8b   db d888888b  .d88b.  
  `88'   888o  88 88    88 88'     888o  88   `88'   .8P  Y8. 
   88    88V8o 88 Y8    8P 88ooooo 88V8o 88    88    88    88 
   88    88 V8o88 `8b  d8' 88~~~~~ 88 V8o88    88    88    88 
  .88.   88  V888  `8bd8'  88.     88  V888   .88.   `8b  d8' 
Y888888P VP   V8P    YP    Y88888P VP   V8P Y888888P  `Y88P'  

v{__version__}
{__copyright__}

{platform.python_implementation()} {sys.version.replace(nl, " ")}
Running on {platform.platform()}
"""
