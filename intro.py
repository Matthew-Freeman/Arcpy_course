import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\My_Files\ArcPy_Course\LPA\Data\Sample.gdb"

# fc = r"D:\My_Files\ArcPy_Course\LPA\Data\ne_10m_admin_0_countries.shp"
fc = arcpy.GetParameterAsText(0)
if fc == "":
    fc = r"D:\My_Files\ArcPy_Course\LPA\Data\ne_10m_admin_0_countries.shp"
numFeats = arcpy.GetCount_management(fc)
print_message("{0} has {1} features(s)".format(fc,numFeats))

##arcpy.CreateFileGDB_management(r"D:\My_Files\ArcPy_Course\LPA\Data","Sample")
##arcpy.Select_analysis(fc,"Egypt","NAME = 'Egypt'")

print_message("Script completed")
