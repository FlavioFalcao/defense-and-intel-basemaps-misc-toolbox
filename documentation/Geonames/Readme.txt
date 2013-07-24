======================================================================================
Geonames Tools
======================================================================================
The Geoname Tools toolbox contains tools to create a gazetteer style locator based on 
the National Geospatial-Intelligence Agency (NGA) UTF-8 encoded tab-delimited geonames 
text files.

--------------------------------------------
Contents of Zip File
--------------------------------------------
1) Geonames Tools toolbox (Geonames Tools.tbx) - Contains the following geoprocessing 
tools and toolset:

	- Load Geonames File - used to load the contents of a single geonames text file 
	into a point geodatabase point feature class and processes the loaded features 
	for input into the Create Geonames Gazetteer Locator tool.

	- Create Geonames Gazetteer Locator - used to create a gazetteer style locator 
	based on the contents of the point geodatabase feature class populated by the 
	Load Geonames File tool.

Model Script Tools (toolset) - Contains the following script tools which are executed
by the Load Geonames File tool (NOTE: THESE SCRIPT TOOLS SHOULD NOT BE EXECUTED MANUALLY;
THEY ARE DESIGNED TO BE EXECUTED ONLY BY THE LOAD GEONAMES FILE TOOL).

	- Check Input - Verifies that the input geonames feature class is of type point, 
	that it has the correct fields to support the loading of the geonames text file, 
	and that the input feature class does not have any existing features.

	- Load Geonames - Loads the contents of the geonames text file into the point 
	geodatabase feature class.


2) ModelScripts folder - Contains the Python scripts that are the source for the 
Script Tools referenced in the Model Script Tools toolset. 
NOTE: DO NOT DELETE THE FILES CONTAINED IN THIS FOLDER.


3) Data\Geonames.gdb file geodatabase - Contains the following datasets:

	- GeonamesTemplate - A point feature class containing the appropriate schema and 
	coordinate system (WGS1984) for loading the geonames text file by the 
	Load Geonames File tool.


	- AdminCodes - a table containing the principle administrative division code and 
	associated name. The Load Geonames File tool maps the division code from the 
	geonames text file to the contents of this table to determine the name and 
	division class of the principle administrative division and stores these values 
	on the geonames point feature class.

	Example of contents: Code = AF13; Name =  Kabul; AdminDivisionClass = wilayat (province). 

	This information is exposed to the user in the gazetteer locator created by the 
	Create Geonames Gazetteer Locator tool.

	NOTE: CONTENTS 	OF THIS TABLE ARE CURRENT AS OF APRIL 2010.


	- CountryCodes - a table containing the country code and associated country name.
	The Load Geonames File tool maps the country code from the geonames text file to the 
	contents of this table to determine the country name and stores this value on the 
	geonames point feature class. 

	Example of contents: Code = AF; Name =  AFGHANISTAN. 

	This information is exposed to the user in the gazetteer locator created by the 
	Create Geonames Gazetteer Locator tool. 

	NOTE: CONTENTS OF THIS TABLE ARE CURRENT AS OF APRIL 2010.


	- FeatureCodes - a table containing the feature type code and associated feature 
	type name. The Load Geonames File tool maps the feature type code from the geonames 
	text file to the contents of this table to determine the feature type name and stores
	this value on the geonames point feature class. 

	Example of contents: Code = CNLI; Name =  irrigation canal(s). 

	This information is exposed to the user in the gazetteer locator created by the 
	Create Geonames Gazetteer Locator tool.



--------------------------------------------
Processing Steps
--------------------------------------------
1) Download the world-wide or individual country geonames text files from 
http://earth-info.nga.mil/gns/html/namefiles.htm.

WARNING: Do not use this tool to load more then one geonames text file into the same feature class; 
duplication of features will result. Either append all geonames text files into a single text file 
before running this tool or load each text file into separate feature classes and use the Merge 
tool found in the Data Management toolbox to combine these multiple datasets into a single, new 
output dataset.

2) Create a new file geodatabase.

3) Copy the GeonamesTemplate feature class from the Data\Geonames.gdb file geodatabase to the file 
geodatabase created in step #2.

4) Rename the copied feature class to "Geonames" or some other name of your choice.

5) Run the Geonames Tools.tbx\Load Geonames File tool to load the geonames text file from step #1 
into the point feature class from step #4.

6) Run the Geonames Tools.tbx\Create Geonames Gazetteer Locator tool to create a gazetteer style 
locator based on the contents of the point feature class from step #5.
