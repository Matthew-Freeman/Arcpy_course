import arcpy

#dataElement = r"D:\My_Files\ArcPy_Course\LPA\Data\Sample.gdb\NaturalEarth"
dataElement = r"D:\My_Files\ArcPy_Course\LPA\Data\Sample.gdb"
#dataElement = r"D:\My_Files\ArcPy_Course\LPA\Data\Sample.gdb\Countries"
descDictionary = arcpy.da.Describe(dataElement)
#print(descDictionary)
for i,key in enumerate(descDictionary):
    print("{0}.{1}:{2}".format(i+1,key,descDictionary[key]))
##desc = arcpy.Describe(dataElement)
##print("Describing {0}...".format(dataElement))
##print("Name:         " + desc.name)
##print("dataType:     " + desc.dataType)
##print("catalogPath:  " + desc.catalogPath)
##print("Children:")
##for child in desc.children:
##    if child.dataType == "FeatureDataset":
##        pass
##    else:
##        if hasattr(child,"shapeType"):
##            print("    {0} is a {1} of shapeType {2}".format(
##            child.name,child.dataType, child.shapeType))
##            print("    with Extent: {0}".format(child.extent))
##        else:
##            print("    {0} is a {1}".format(child.name,child.dataType))
##
##        print("    and Fields:")
##        for field in child.fields:
##            print("    {0} of type {1}".format(field.name,field.type))

print("\nScript completed!")
