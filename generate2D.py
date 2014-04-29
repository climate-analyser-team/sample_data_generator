#
# One-dimensional netCDF sample file generator
# Author:		Ashley Hall
# Last modified: 29 Apr 2014
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
from monthlist import latList
from monthlist import lonList
import numpy

# Creates a 2D netCDF file with random data in the range of [-5, 5].
# filename: The filename to save to.
# start: a tuple in the format (year, month, date) which represents the first
#		datapoint
# months: the number of months to generate data for.
def generate2D(filename, start, months, lats, lons):
	cdf = Dataset(filename, 'w', format='NETCDF4')

	cdf.createDimension('time', months)
	times = cdf.createVariable('time', 'f8', ('time', ))
	times.units = 'days since %04d-%02d-%02d 00:00:00.0' % start
	times.calendar = 'gregorian'
	times[:] = monthlist(start, months)

	cdf.createDimension('lat', lats)
	latitudes = cdf.createVariable('lat', 'f4', ('lat', ))
	latitudes.units = 'degrees north'
	latitudes[:] = latList(lats)

	cdf.createDimension('lon', lons)
	longitudes = cdf.createVariable('lon', 'f4', ('lon', ))
	longitudes.units = 'degrees east'
	longitudes[:] = lonList(lons)

	randoms = cdf.createVariable('random', 'i4', ('time', 'lat', 'lon', ))
	randoms.units = 'random values'
	randoms[:] = numpy.random.randint(-5, 6, (months, lats, lons, ))

	cdf.close()
	return
