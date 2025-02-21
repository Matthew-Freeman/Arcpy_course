import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\My_Files\ArcPy_Course\LPA\Projects\GeomProject\GeomProject.gdb"
srWGS84 = arcpy.SpatialReference("WGS 1984")

arcpy.management.CreateFishnet(
    out_feature_class="FishnetLines",
    origin_coord="0 0",
    y_axis_coord="0 1",
    cell_width=1,
    cell_height=1,
    number_rows=10,
    number_columns=15,
    corner_coord=None,
    labels="LABELS",
    template="DEFAULT",
    geometry_type="POLYLINE"
)
if arcpy.Exists("FishnetPoints"):
    arcpy.management.Delete("FishnetPoints")
arcpy.management.Rename("FishnetLines_label","FishnetPoints")

arcpy.management.CreateFishnet(
    out_feature_class="FishnetPolys",
    origin_coord="0 0",
    y_axis_coord="0 1",
    cell_width=1,
    cell_height=1,
    number_rows=4,
    number_columns=6,
    corner_coord=None,
    labels="NO_LABELS",
    template="DEFAULT",
    geometry_type="POLYGON"
)
for geomType in ["Polys","Lines","Points"]:
    arcpy.management.DefineProjection(
    in_dataset="Fishnet{0}".format(geomType),
    coor_system=srWGS84
    #'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
)



print("\nScript completed!")
