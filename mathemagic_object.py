import bpy
import math as m
#empty lists for later
verts = []
edges = []    
faces = []
listspacex = []
listspacey = []
#defining sin, cos and tan to be limited by 2pi, important for not overlapping the shape
def sinv(uinput):
    mid = (2*m.pi)*(uinput/loopv)
    return m.sin(mid)
def sinu(uinput):
    mid = (2*m.pi)*(uinput/loopu)
    return m.sin(mid)
def cosu(uinput):
    mid = (2*m.pi)*(uinput/loopu)
    return m.cos(mid)
def cosv(uinput):
    mid = (2*m.pi)*(uinput/loopv)
    return m.cos(mid)
def tanu(uinput):
    mid = (2*m.pi)*(uinput/loopu)
    return m.tan(mid)
def tanv(uinput):
    mid = (2*m.pi)*(uinput/loopv)
    return m.tan(mid)
"""
**********user input section***********
"""
#set the scale of x,y,z here!
scalex = 4
scaley = 8
scalez = 2
#here we can choose u and v resolutions
loopu = 25
loopv = 25

#opening up a loop of loops, this is so we can make a list of lists containing vertex points
#this makes it a lot easier to reference them later!
#it means that everything is in loops: listspace[2][4] refers to the fifth vertex on the 3rd loop
for b in range(0,loopv):
    for a in range(0,loopu):
        
        #defining a and b as u and v, this is where we can multiply by a resolution if we want
        u = a
        v = b
        
        #here is where you could enter your uv equation
        x = cosu(4*u)/4+sinv(8*v)/16+((13/10)+sinu(u))*cosv(v)
        y = sinu(4*u)/4+sinv(8*v)/16+(2/3)*cosu(u)+((13/10)+sinu(u))*sinv(v)
        z = sinv(8*v)/16+sinv(100*v)/100-sinu(3*u)/10+cosu(u)
        
        coord = [[x , y , z]]
        listspacex.extend(coord)
    listspacey.extend([listspacex])
    listspacex = []
    
for b in range(0,loopv):
    for a in range(0,loopu):
        verts.extend([((scalex*listspacey[b][a][0]),(scaley*listspacey[b][a][1]),(scalez*listspacey[b][a][2]))])
# This section below goes through a list as long as the number of inner lists
# in above (listspacey*listspacex) and puts faces between sets of vertices in the right place
for i in range(0,loopu*loopv):
    f1=(i+loopu)%(loopu*loopv)
    f2=i
    f3=(i+1)%(loopu*loopv)
    f4=(i+loopu+1)%(loopu*loopv)
    faces.extend([ ( f1,f2,f3,f4 ) ])
    #loopu and v being defined as the resolution for u and v above
# This bit picks up the list of faces and vertices we added to, and puts them all in 
# a new mesh, that then gets spit out as an object called "shapeobject"
meshdata = bpy.data.meshes.new("shapedata")
meshdata.from_pydata(verts, edges, faces)                
mesh_obj = bpy.data.objects.new("shapeobject", meshdata)
bpy.context.collection.objects.link(mesh_obj)
