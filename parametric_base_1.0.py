import bpy
import math as m

ob = bpy.data.objects["Cube"]

frame_number = 0
u = -0.6
v = -0.6

for i in range (0,500):
    bpy.context.scene.frame_set(frame_number)
    u += 1
    v += 0.1
    ob.location = ( (m.cos(u)/2-m.cos(2*u))*(100*m.sin(u/5)) , (m.cos(u)/2-m.cos(2*u))*(m.cos(u)*100*m.cos(u/5)) , 0)
    ob.keyframe_insert(data_path="location", index=-1)
    frame_number+=1
