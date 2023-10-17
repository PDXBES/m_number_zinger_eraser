import utility
import arcpy
import sys
import config

arcpy.env.overwriteOutput = True

print("M Number Zinger Eraser - Process Starting")


try:

    utility.create_erased_zingers(config.NEWSTORMZINGER2PIPE_copy, config.areas_copy)
    utility.create_erased_zingers(config.NEWSTORMZINGER2NODE_copy, config.areas_copy)


except Exception as e:

    print("Exception Encountered - Process Interrupted".format())
    arcpy.ExecuteError()
    print(str(sys.exc_info()[0]))

print("M Number Zinger Eraser - Process Ended")