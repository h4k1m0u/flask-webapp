# LAS
-----
##### Compile GrassGIS 7.8.2 with LibLAS and PDAL support
- LibLAS and [PDAL](https://github.com/PDAL/PDAL) are used to read point-cloud data in GrassGIS. As mentioned in the [official doc](https://grasswiki.osgeo.org/wiki/Compile_and_Install_Ubuntu), they can be installed with `apt-get` with other GIS packages by adding the following repo:

```
sudo add-apt-repository ppa:ubuntugis/ppa
```

- GrassGIS source-code can be downloaded from [its github repo](https://github.com/OSGeo/grass/releases).
- Install all the dependencies including liblas-config and pdal-config: `sudo apt install liblas-c-dev libpdal-dev`
- Configuration: `./configure --with-pdal --with-liblas --with-freetype-includes=/usr/include/freetype2`
- Compilation: `make`
- Installation: `sudo make install`
- Install Wx-Python: `sudo apt install python3-wxgtk4.0`

##### LibLAS CLI
- Install the command-line client from the same UbuntuGIS repo above with: `apt-get install liblas-bin`
- Use it to get metadata from a las file: `lasinfo --no-check r.las`

##### Open a LAS file with GrassGIS
- Run `r.in.lidar`
- Provide the `LAS input file` as well as a `Name for the output raster`.
- Make sure to override the projection check by enabling the `(o)` option, and enable also the `(e)` option for region extent.


# PLY
-----
##### Install ply GrassGIS Addon
- Ply is another format for point-cloud data like LAS.
- In GrassGIS's GUI, go to `Settings -> Addon extensions -> Install extensions from addons`
- Type `v.in.ply` and double-click on it to install it.


# Point-cloud reader
--------------------
- [Displaz](https://github.com/FugroRoames/displaz) was tested and worked well.
