#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Runs the package.

Slight Fimulator - Flight simlator in Python
Copyright (C) 2017 Hao Tian and Adrien Hopkins
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Installs Python 3 division and print behaviour
from __future__ import division, print_function

from classes import *
from functions import *
from constants import *

# Edit this line to change the screen size
screen_size = (1280, 960)

if __name__ == '__main__':
    print("""Slight Fimulator Copyright (C) 2017 Hao Tian and Adrien Hopkins
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.\n""")
    game = Game(size=screen_size)
    game.mainloop()
