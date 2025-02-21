import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\My_Files\ArcPy_Course\LPA\Projects\MapSeriesProject\MapSeriesProject.aprx")
lyt = aprx.listLayouts("Layout")[0]
if lyt.mapSeries is not None:
    mapSeries = lyt.mapSeries
else:
    print("Is not a map series")
mapSeries.exportToPDF(r"D:\My_Files\ArcPy_Course\LPA\PDFs\LayoutFromClass.pdf","RANGE","1-10")
del aprx

print("\nScript completed!")
