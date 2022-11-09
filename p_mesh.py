import bpy
import math as m

sin = m.sin
cos = m.cos
tan = m.tan

listspacex = []
listspacey = []
u = 1
v = 1
res = 3

for b in range(0,res*10):
    for a in range(0,res*10):
        
        u = a/res
        v = b/res
        
        x = sin(v)*(u)
        y = sin(v)*sin(u)
        z = cos(v)
        
        coord = [[x , y , z]]
        listspacex.extend(coord)
    listspacey.extend([listspacex])
    listspacex = []
    
for b in range(0,res*10):
    for a in range(0,res*10):
        verts = [(listspacey[b][a][0],listspacey[b][a][1],listspacey[b][a][2])]
        edges = []    
        faces = []
        meshdata = bpy.data.meshes.new("shapedata")
        meshdata.from_pydata(verts, edges, faces)
        mesh_obj = bpy.data.objects.new("shapedata", meshdata)
        bpy.context.collection.objects.link(mesh_obj)
