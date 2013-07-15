#------------------------------------------------------------------------------
# Copyright 2013 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------
# Name: TestCreateCIBMosaicDataset.py
# Requirements: ArcGIS Desktop Standard
#------------------------------------------------------------------------------

import arcpy
import os
import sys
import traceback

import TestUtilities

def RunTest():
    try:
        arcpy.AddMessage("Starting Test: CreateCIBMosaicDataset")

        toolbox = TestUtilities.toolbox
        arcpy.ImportToolbox(toolbox, "CreateCIBAlias")
        arcpy.env.overwriteOutput = True

        
        # Set environment settings
        print "Running from: " + str(TestUtilities.currentPath)
        print "Geodatabase path: " + str(TestUtilities.geodatabasePath)
        
        arcpy.env.overwriteOutput = True
        
                       
        webMercator = arcpy.SpatialReference(r"WGS 1984 Web Mercator (Auxiliary Sphere)")

        if os.path.exists(os.path.join(TestUtilities.inputGDB, "Imagery_Test")):
            #delete it
            print "hi"

        ########################################################
        # Execute: 
        arcpy.CreateCIBMosaicDataset_CreateCIBAlias(TestUtilities.inputGDB, "Imagery_Test", webMercator)  
        ########################################################


        inputMosaicDataset = os.path.join(TestUtilities.inputGDB, "Imagery_Test")
        
     
        
        # Check For Valid Input: Make sure Input Mosaic Dataset was created
        objects2Check = []
        objects2Check.extend([inputMosaicDataset, toolbox])
        for object2Check in objects2Check :
            desc = arcpy.Describe(object2Check)
            if desc == None :
                raise Exception("Bad Input")
            else :
                print "Valid Object: " + desc.Name
                print "Success " + inputMosaicDataset + " was created" 
                
                
        #Verify Results        
        inputFeatureCount = int(arcpy.GetCount_management(inputMosaicDataset).getOutput(0)) 
        print "Input FeatureClass: " + str(inputMosaicDataset)
        print "Input Feature Count: " +  str(inputFeatureCount)
        
        if inputFeatureCount > 0 :
            print "Mosaic Dataset has already been created and populated"
             
           
        
        print "Test Successful"        
                
    except arcpy.ExecuteError: 
        # Get the tool error messages 
        msgs = arcpy.GetMessages() 
        arcpy.AddError(msgs) 
    
        # return a system error code
        sys.exit(-1)
        
    except Exception as e:
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
    
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages() + "\n"
    
        # Return python error messages for use in script tool or Python Window
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
    
        # return a system error code
        sys.exit(-1)

RunTest()