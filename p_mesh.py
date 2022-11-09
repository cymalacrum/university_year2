import bpy
import math as m


sin = m.sin
cos = m.cos
tan = m.tan

listspacex = []

u = 1
v = 1

x = 1

for a in range(0,100):
    
    x = cos(a)
    y = sin(a)
    z = 0
    
    coord = [[x , y , z]]
    listspacex.extend(coord)
for a in range(0,100):
    
    verts = [(listspacex[a][0],listspacex[a][1],listspacex[a][2])]
    edges = []    
    faces = []
    meshdata = bpy.data.meshes.new("shapedata")
    meshdata.from_pydata(verts, edges, faces)
    mesh_obj = bpy.data.objects.new("shapedata", meshdata)
    bpy.context.collection.objects.link(mesh_obj)

