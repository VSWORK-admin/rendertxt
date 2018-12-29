@echo off
cd  %~dp0
"C:\Program Files\Blender\2.80\blender.exe" render.blend -b -P rendertxt.py
pause