#
# 1D sample netCDF file generation test suite
# Author:		Ashley Hall
# Last modified: 27 Apr 2014
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
from netCDF4 import Dataset
from generate2D import generate2D

class Test2DGeneration(unittest.TestCase):

	def test_checkReadable(self):
		filename = "sample_2D.nc"

		generate2D(filename, (2014, 01, 31,), 12, 6, 12)
		cdf = Dataset(filename, 'r', format='NETCDF4')

		self.assertEqual(cdf.variables['lat'][:].tolist(), [
			-90, -60, -30, 0, 30, 60, 90
		])
		self.assertEqual(cdf.variables['lat'][:].tolist(), [
			-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180
		])

		#self.assertEqual(len(cdf.variables['random'][:]), 12)

		cdf.close()

		return;
