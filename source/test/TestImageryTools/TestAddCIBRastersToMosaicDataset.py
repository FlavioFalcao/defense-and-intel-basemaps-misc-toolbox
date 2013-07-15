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
# Name: TestAddCIBRastersToMosaicDataset.py
# Requirements: ArcGIS Desktop Standard
#------------------------------------------------------------------------------

import arcpy
import os
import sys
import traceback

import TestUtilities

def RunTest():
    try:
        arcpy.AddMessage("Starting Test: Add CIB Rasters To Mosaic Dataset")
 
        toolbox = TestUtilities.toolbox
        arcpy.ImportToolbox(toolbox, "addCIBAlias")
        arcpy.env.overwriteOutput = True
        
        inputMosaicDataset = os.path.join(TestUtilities.inputGDB, "Imagery_Test")
        print inputMosaicDataset
 
        # Check For Valid Input
        objects2Check = []
        objects2Check.extend([inputMosaicDataset, toolbox])
        for object2Check in objects2Check :
            desc = arcpy.Describe(object2Check)
            if desc == None :
                raise Exception("Bad Input")
            else :
                print "Valid Object: " + desc.Name 
        
        # Set environment settings
        print "Running from: " + str(TestUtilities.currentPath)
        print "Geodatabase path: " + str(TestUtilities.geodatabasePath)
        
        arcpy.env.overwriteOutput = True
           
        ########################################################3
        # Execute the Model under test: 
        arcpy.AddCIBRastersToMosaicDataset_addCIBAlias(inputMosaicDataset, TestUtilities.sampleInputPath)  
        ########################################################3
        
        inputFeatureCount = int(arcpy.GetCount_management(inputMosaicDataset).getOutput(0)) 
        print "Input FeatureClass: " + str(inputMosaicDataset)
        print "Input Feature Count: " +  str(inputFeatureCount)
            
        if (inputFeatureCount <= 0) :
            print "Invalid Input Feature Count: " +  str(inputFeatureCount)
            raise Exception("Test Failed")
         
       
        
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