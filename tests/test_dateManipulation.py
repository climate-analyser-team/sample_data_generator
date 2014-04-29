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
from monthlist import latList
from monthlist import lonList

class TestDateManipulation(unittest.TestCase):

    def test_checkDayOffsetLists(self):
        self.assertEqual(monthlist((2014, 1, 31), 1), [0])
        self.assertEqual(monthlist((2014, 1, 31), 2), [0, 28])
        self.assertEqual(monthlist((2014, 1, 31), 24), [
              0,  28,  59,  89, 120, 150, 181, 212, 242, 273, 303, 334,
            365, 393, 424, 454, 485, 515, 546, 577, 607, 638, 668, 699
        ])
        return;

    def test_LatLonLists(self):
        self.assertEqual(len(latList(18)), 18)
        self.assertEqual(latList(19), [
            -90.0, -80.0, -70.0, -60.0, -50.0, -40.0, -30.0, -20.0, -10.0, 0.0,
             10.0,  20.0,  30.0,  40.0,  50.0,  60.0,  70.0,  80.0,  90.0])
        self.assertEqual(len(lonList(500)), 500)
        self.assertEqual(lonList(6), [-180.0, -120.0, -60.0, 0.0, 60.0, 120.0])
