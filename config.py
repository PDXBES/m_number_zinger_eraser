import arcpy


print("Reading inputs")

NEWSTORMZINGER2NODE = r"\\besfile1\asm_projects\E11526_LowerNW_Capacity\Model\Base_E11526d30Sep100AltRP\EmgaatsModel.gdb\NEWSTORMZINGER2NODE"
NEWSTORMZINGER2PIPE = r"\\besfile1\asm_projects\E11526_LowerNW_Capacity\Model\Base_E11526d30Sep100AltRP\EmgaatsModel.gdb\NEWSTORMZINGER2PIPE"
areas = r"\\besfile1\asm_projects\E11526_LowerNW_Capacity\Model\Base_E11526d30Sep100AltRP\EmgaatsModel.gdb\Areas"


NEWSTORMZINGER2NODE_copy = arcpy.CopyFeatures_management(NEWSTORMZINGER2NODE, r"in_memory/NEWSTORMZINGER2NODE_copy")
NEWSTORMZINGER2PIPE_copy = arcpy.CopyFeatures_management(NEWSTORMZINGER2PIPE, r"in_memory/NEWSTORMZINGER2PIPE_copy")
areas_copy = arcpy.CopyFeatures_management(areas, r"in_memory/areacopy")

output_gdb = r"\\besfile1\ISM_PROJECTS\CIP_Projects\E11526_Lower_NW_Capacity\WO_10227\working.gdb"