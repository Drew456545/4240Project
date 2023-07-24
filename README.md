# 4240 Project - System Monitoring with GUI
Simple, light-weight linux task manager with GUI built with python. 

![image](https://github.com/Drew456545/4240Project/assets/113255492/01339943-def7-460f-83ae-9fe0b6fa97cc)

Uses the psutils and tkinter libraries for python, documentation for which can be found here: 
    https://psutil.readthedocs.io/en/latest/
    https://docs.python.org/3/library/tkinter.html

Provides a interface to view a snapshot of top processes, cpu, memory, and network usage and system information. 
Clicking on one of the processes provides additional details. You can refresh the list and kill selected processes 
by clicking on the corresponding buttons.

# Install
Install pip if you don't already have it

` sudo apt install pip  `

Using pip, install tkinter and psutil

` pip install tk  `

` pip install psutil `

Run using `python3 sysmongui.py` or create an executable using pyinstaller:

`pip install pyinstaller` `pyinstaller sysmongui.py --onefile` `cd dist`

Run the executable with: `./sysmongui`

