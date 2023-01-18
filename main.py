# coding=utf-8
import arcpy

arcpy.env.workspace = r"C:\Users\USER03-60\Downloads\PracticaSIG2"
print arcpy.env.workspace

fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    desc = arcpy.Describe(fc)
    s = fc.encode('ascii', 'ignore').decode('ascii')
    print "Name: {}".format(s)
    print "Data Type: {}".format(desc.dataType)
    print "Data Class: {}".format(desc.dataSetType)
    print "Type: {}".format(desc.featureType)
    print "Shape Type: {}".format(desc.ShapeType)
    print "\n-------------------------------------\n"

print "Feature class list complete."
