import arcpy

inputFeatures = arcpy.GetParameterAsText(0)
sqlExpression = arcpy.GetParameterAsText(1)
bufferDistance = arcpy.GetParameterAsText(2)
dissolveBuffers = arcpy.GetParameter(3)
outputBufferFCName = arcpy.GetParameterAsText(4).replace(" ","")

if dissolveBuffers:
    dissolveBuffers = "ALL"
else:
    dissolveBuffers = "NONE"

arcpy.AddMessage(inputFeatures)
arcpy.AddMessage(sqlExpression)
arcpy.AddMessage(bufferDistance)
arcpy.AddMessage(dissolveBuffers)
arcpy.AddMessage(outputBufferFCName)

arcpy.Select_analysis(inputFeatures,"SelectFC",sqlExpression)
outputBufferFC = arcpy.Buffer_analysis("SelectFC",outputBufferFCName,bufferDistance,dissolve_option=dissolveBuffers)[0]

arcpy.SetParameter(5,outputBufferFC)
