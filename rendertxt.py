import bpy
import os
import json

scene = bpy.context.scene
fp = scene.render.filepath # get existing output path
startfp = fp
## scene.render.image_settings.file_format = 'PNG' # set output format to .png

def ReadJson():
    with open('txt.txt') as json_file:  
        data = json.load(json_file)
        for p in data:
            print('Name: ' + p['name'] )
            bpy.data.objects['Text'].data.body = p['name']
            ##bpy.data.objects['Text'].active_material.diffuse_color = (p['color']['r'],p['color']['g'],p['color']['b'])
            bpy.data.objects['Text'].active_material.node_tree.nodes.get("Principled BSDF").inputs[0].default_value = (p['color']['r'],p['color']['g'],p['color']['b'],1)
            scene.frame_set(1)
            scene.render.filepath = fp + p['name']
            ##bpy.ops.render.render(write_still=True) # render still
            bpy.ops.render.render(write_still=False,animation= True) # render still
            scene.render.filepath  = startfp
            

ReadJson()