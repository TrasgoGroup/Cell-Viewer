"""
             A P A C H E   L I C E N S E
                    ------------ 
              Version 2.0, January 2004

       Copyright 2021 Miguel Cruces Fernández

  Licensed under the Apache License, Version 2.0 (the 
"License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, 
software distributed under the License is distributed on an 
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
either express or implied. See the License for the specific 
language governing permissions and limitations under the 
License.

           miguel.cruces.fernandez@usc.es
               mcsquared.fz@gmail.com
"""

try:  # Python 3
    import tkinter as tk
    from tkinter import ttk
except ImportError:  # Python 2.7
    import Tkinter as tk
    import ttk

import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    from tkcalendar import DateEntry, Calendar
except ModuleNotFoundError:
    install("tkcalendar")
    from tkcalendar import DateEntry, Calendar
