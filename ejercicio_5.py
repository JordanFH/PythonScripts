import arcpy
import sys
import os

# a.env.workspace = r"C:\Users\USER03-60\Downloads\Evaluacion2"
#
# input_raster = "Mapa_Cajamarca.jpg"
# output_file = "salida.txt"
#
# a.RasterToASCII_conversion(input_raster, output_file)

arcpy.env.workspace = r"C:\Users\USER03-60\Downloads\PracticaSIG6\Alcoiecm.shp"

fieldName = "Referencia"

exp = 123

ruta = arcpy.env.workspace

with arcpy.da.SearchCursor(ruta, "Referencia") as cursor:
    for row in cursor:
        print row[0]

rows = arcpy.UpdateCursor(ruta)

print "-----------------------"

with arcpy.da.UpdateCursor(ruta, "Referencia") as cursor:
    for row in cursor:
        row[0] = 321
        cursor.updateRow(row)
        print row[0]

# print ruta
# arcpy.management.AddField(ruta, fieldName, "LONG")
arcpy.CalculateField_management(ruta, fieldName, exp, "PYTHON")
