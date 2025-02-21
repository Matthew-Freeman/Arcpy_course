import arcpy

shp = r"D:\My_Files\ArcPy_Course\LPA\Data\ne_10m_admin_0_countries.shp"

#print([field.name for field in arcpy.ListFields(shp)])

##with arcpy.da.SearchCursor(shp,['NAME',"CONTINENT", 'POP_EST'],"FID <10") as cursor:
##    for row in cursor:
##        print("{0} people in {1}".format(row[2],row[0]))


##with arcpy.da.SearchCursor(shp,['NAME',"SHAPE@XY","SHAPE@AREA","SHAPE@LENGTH","SHAPE@"],"FID <10") as cursor:
##    for row in cursor:
##        print("Centroid of {0} is at {1}".format(row[0],row[1]))
##        print("its area is {0} and its perimeter is {1}".format(row[2],row[3]))
##        print("and it has {0} polygon(s)".format(row[4].partCount))
##        print("with a total of {0} vertices".format(row[4].pointCount))

##countryList = []
##with arcpy.da.SearchCursor(shp,["NAME"]) as cursor:
##    for row in cursor:
##        countryList.append(row[0])
##countryList = [row[0] for row in arcpy.da.SearchCursor(shp,["NAME"])]
##print(countryList)
##print(len(countryList))

##continentList = [row[0] for row in arcpy.da.SearchCursor(shp,["CONTINENT"])]
##print(set(continentList)) #removing duplicated values
##print(len(set(continentList)))
##print(sorted(set(continentList)))

##countryContinentList = [[row[0],row[1]] for row in arcpy.da.SearchCursor(shp,["NAME","CONTINENT"],"FID<10")]
##print(countryContinentList)
##print(countryContinentList[2])
##print(countryContinentList[2][1])

##fidCountryDict = {}
##with arcpy.da.SearchCursor(shp,["FID",'NAME'],"FID <10") as cursor:                        
##    for row in cursor:
##        fidCountryDict[row[0]] = row[1]
##fidCountryDict = {row[0]:row[1] for row in arcpy.da.SearchCursor(shp,["FID",'NAME'],"FID <10")}
##print(fidCountryDict)
##print(fidCountryDict[4])

fid3FieldsDict = {row[0]:[row[1],row[2],"{:,}".format(row[3])] for row in arcpy.da.SearchCursor(shp,["FID",'NAME','CONTINENT','POP_EST'],"FID <10")}
print(fid3FieldsDict)
print(fid3FieldsDict[4])
print(fid3FieldsDict[4][2])

print("\nScript completed!")
