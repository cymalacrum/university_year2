import bpy
import math as m


sin = m.sin
cos = m.cos
tan = m.tan


ob = bpy.data.objects["Circle"]

frame_number = 0
u = -0.6
v = -0.6

for i in range (0,500):
    bpy.context.scene.frame_set(frame_number)
    
    #Define ur variables here!
    x = u/8 
    y = (5*sin(3*u/9))/(3+5*sin(u/9))
    z = 0
    
    
    u += 1
    ob.location = (x,y,z)
    ob.keyframe_insert(data_path="location", index=-1)
    frame_number+=1
