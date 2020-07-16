@echo off
TITLE PyRay2
cd /d %~dp0

if exist pyray2\PyRay2.py (
	set PYRAY_FILE=pyray2\PyRay2.py
)


python -O %PYRAY_FILE% %*
