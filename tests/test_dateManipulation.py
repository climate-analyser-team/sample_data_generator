#
# Date manipulation test suite.
# Author:        Andrew Dunn
# Last modified: 22 Apr 2014
#
# This file is part of Climate Analyser.
#
# Climate Analyser is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Climate Analyser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Climate Analyser.
# If not, see <http://www.gnu.org/licenses/>.
#

import unittest
from monthlist import monthlist

class TestDateManipulation(unittest.TestCase):

    def test_checkDayOffsetLists(self):
        self.assertEqual(monthlist((2014, 1, 31), 1), [0])
        self.assertEqual(monthlist((2014, 1, 31), 2), [0, 28])
        self.assertEqual(monthlist((2014, 1, 31), 24), [
              0,  28,  59,  89, 120, 150, 181, 212, 242, 273, 303, 334,
            365, 393, 424, 454, 485, 515, 546, 577, 607, 638, 668, 699
        ])
        return;
