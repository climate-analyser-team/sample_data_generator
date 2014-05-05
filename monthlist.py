#
# Creates a list of day offsets for a given number of months from a particular
# date.
#
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

from datetime import date
from datetime import timedelta
from calendar import monthrange
from numpy import arange

# Adds the specified number of months to the given date and returns as a tuple.
def addMonths(start, months):
    result = divmod((start[1] - 1) + months, 12)
    year = start[0] + result[0]
    month = result[1] + 1

    range = monthrange(year, month)
    day = min(start[2], range[1])

    return year, month, day

# start should be a tuple in the format (year, month, day)
# months should be the number of months
def monthlist(start, months):
    first = date(start[0], start[1], start[2])

    output = []
    for i in range (0, months):
        next = addMonths(start, i)
        current = date(next[0], next[1], next[2])
        delta = current - first
        output.append(delta.days)

    return output

# generates the given number of latitudes between -90 to 90
def latList(lats):
    latsn = lats - 1
    return arange(-90.0, 90.0 + (180.0 / latsn), 180.0 / latsn).tolist()

# generates the given number of longitudes between -180 to 180
def lonList(lons):
    lonsn = lons
    return arange(-180.0, 180.0, 360.0 / lonsn).tolist()
