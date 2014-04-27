#
# One-dimensional netCDF sample file generator
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

# This file requires the sample_data_generator directory to be in the python path
from netCDF4 import Dataset
from monthlist import monthlist
import numpy

# Creates a 1D netCDF file with random data in the range of [-5, 5].
# filename: The filename to save to.
# start: a tuple in the format (year, month, date) which represents the first
#        datapoint
# months: the number of months to generate data for.
def generate1D(filename, start, months):
    cdf = Dataset(filename, 'w', format='NETCDF4')

    cdf.close()
    return
