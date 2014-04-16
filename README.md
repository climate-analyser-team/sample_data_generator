# sample-data-generator

Generates sample randomised data which can later be used for correctness
checking.

## Pre-requisites

### HDF5 Library
Library which handles management of extremely large and complex data
collections.

#### Installation instructions
1. Download + Extract HDF5 Library Source
    ``` bash
    curl http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.12.tar.gz -o hdf5-1.8.12.tar.gz
    tar -xzf hdf5-1.8.12.tar.gz
    rm hdf5-1.8.12.tar.gz
    ```

2. Create a build directory
    ``` bash
    mkdir build-hdf5 && cd build-hdf5
    ```

3. Build and install the library. Select an installation location using
   `--prefix=LOCATION`.
    ``` bash
    ../hdf5-1.8.12/configure --prefix=/usr/local
    make all
    sudo make install
    ```

4. Cleanup
    ``` bash
    cd ..
    rm -rf build-hdf5
    rm -rf hdf5-1.8.12 # Optional
    ```

### netCDF C Library
The netCDF library defines a machine-independent format for representing
scientific data.

#### Installation instructions
1. Download + Extract netCDF C Library source
    ``` bash
    curl https://codeload.github.com/Unidata/netcdf-c/tar.gz/v4.3.1.1 -o netcdf-c-4.3.1.1.tar.gz
    tar -xzf netcdf-c-4.3.1.1.tar.gz
    rm netcdf-c-4.3.1.1.tar.gz
    ```

2. Create a build directory
    ``` bash
    mkdir build-netcdf && cd build-netcdf
    ```

3. Build and install the library. `/usr/local` should be replaced with the
   installation location of the HDF5 library.
    ``` bash
    CPPFLAGS=-I/usr/local/include LDFLAGS=-L/usr/local/lib ../netcdf-c-4.3.1.1/configure --prefix=/usr/local
    make all
    sudo make install
    ```

4. Cleanup
    ``` bash
    cd ..
    rm -rf build-netcdf
    rm -rf netcdf-c-4.3.1.1
    ```

### pip package installer
The PyPA recommended tool for installing Python packages.

#### Installation instructions
1. Download `pip`

    ``` bash
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py -o get-pip.py
    ```

2. Install `pip`

    ``` bash
    sudo python get-pip.py
    ```

### NumPy Library
NumPy is the fundamental package for scientific computing with Python.

#### Installation instructions
1. Install NumPy using `pip`

    ``` bash
    sudo pip install numpy
    ```

### netCDF4 Python Interface
Python/numpy interface to the netCDF version 4 library.

#### Installation instructions
1. Install the library using `pip`

    ``` bash
    sudo pip install netcdf4
    ```
