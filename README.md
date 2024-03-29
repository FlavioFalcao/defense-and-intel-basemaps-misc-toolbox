defense-and-intel-basemaps-misc-toolbox 
=================================

**IMPORTANT NOTE: THE TOOLS IN THIS TOOLBOX HAVE BEEN MOVED. THIS REPO IS NOW DEPRECATED AND WILL NOT BE MAINTAINED**

Please use the solutions-geoprocessing-toolbox repo:

[https://github.com/Esri/solutions-geoprocessing-toolbox](https://github.com/Esri/solutions-geoprocessing-toolbox)

=================================

A set of tools and models for use in ArcGIS Desktop. These tools provide specialized processing and workflows for defense and intelligence mapping tasks.

![Image of Defense and Intel Analysis Toolbox](Screenshot.JPG)

## Features

* Tools for creating mosaic datasets
* Tools for adding rasters to mosaic datasets
* Tools for calculating raster visibility
* Geonames Tools Toolbox

## <a id="Requirements"></a>Requirements

* ArcGIS Desktop 10.1 Standard 
* Apache Ant - used to download and extract dependent data and run test drivers
* Java Runtime Environment (JRE) or Developer Kit (JDK)

## <a id="Instructions"></a>Instructions

### General Help
[New to Github? Get started here.](http://htmlpreview.github.com/?https://github.com/Esri/esri.github.com/blob/master/help/esri-getting-to-know-github.html)

### Getting Started with the toolbox
* Download the Github repository
    * If repository was downloaded as a zip, extract the zip file
    * Make note of this directory, the steps below assume it will be called "defense-and-intel-basemaps-misc-toolbox"
* Install and configure Apache Ant
    * Download Ant from the [Apache Ant Project](http://ant.apache.org/bindownload.cgi) and unzip to a location on your machine
    * Set environment variable `ANT_HOME` to Ant Install Location
    * Add Ant\bin to your path: `%ANT_HOME%\bin`
    * NOTE: Ant requires Java [Runtime Environment (JRE) or Developer Kit (JDK)](http://www.oracle.com/technetwork/java/javase/downloads/index.html) to be installed and the environment variable `JAVA_HOME` to be set to this location
    * To verify your Ant Installation: Open Command Prompt> `ant -h` and verify it runs and returns the help options correctly 
    * You may optionally install the [PyDev Eclipse Plugin for Python](http://pydev.org) if you plan to use Eclipse to run/debug
* To download the data dependencies 
    * Open Command Prompt>
    * cd defense-and-intel-basemaps-misc-toolbox
    * > ant
    * Verify “Build Succeeded”  
* To run unit tests
    * Open Command Prompt>
    * > cd defense-and-intel-basemaps-misc-toolbox\source\test
    * > ant
    * Verify “Build Succeeded”
    * Note: this will run the test drivers from each test subdirectory (TestCreateCIBMosaicDataset, TestCalculateRasterVisibility, etc.)


## Resources

* Learn more about Esri's [ArcGIS for Defense maps and apps](http://resources.arcgis.com/en/communities/defense-and-intelligence/).

## Issues

* Find a bug or want to request a new feature?  Please let us know by submitting an issue.

## Contributing

Esri welcomes contributions from anyone and everyone. Please see our [guidelines for contributing](https://github.com/esri/contributing).

## Licensing

Copyright 2013 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's
[license.txt](license.txt) file.

[](Esri Tags: ArcGIS Defense and Intelligence Military)
[](Esri Language: Python)
