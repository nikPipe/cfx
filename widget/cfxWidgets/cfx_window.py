from import_module import *


from collections import OrderedDict

from widget.sample import mainWindow
from widget.sample import sample_widget_template
for each in [mainWindow, sample_widget_template]:
    reload(each)
sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

import platform
import sys





class CFXWINDOW:
    def __init__(self):
        self.window_name = 'CFX'
        self.width = 500
        self.height = 800


    def cfx_window_(self):
        #MAINWINDOW
        window = mainWindow.SAMPLE_QMainWindow()

        #CREATE MENU DIC
        menuDic = OrderedDict([

        ])
        print('this is working now')
        print(sys.executable.lower())

        if "maya" in sys.executable.lower():
            from widget.sample import mayaWindow
            self.mayaWindow_ = mayaWindow.mayaWindow_sample(title=self.window_name, menubarDic=menuDic,
                                                            width=self.width, height=self.height)
            self.mayaWindow_.setCentralWidget(self.widget_def(window=self.mayaWindow_))
            self.mayaWindow_.show(dockable=True)
        elif "houdini" in sys.executable.lower():



            print("This script is running in Houdini")
        elif "blender" in sys.executable.lower():
            print("This script is running in Blender")
        elif "3dsmax" in platform.system().lower():
            print("This script is running in 3ds Max")
        elif "unity" in sys.executable.lower():
            print("This script is running in Unity")
        else:
            print("This script is running in an unknown 3D software environment")




    def widget_def(self, window):
        '''

        :return:
        '''
        widget = sample_widget_template.widget_def()

        self.create_cfxSetup_widget()


        return widget

    def create_cfxSetup_widget(self):
        '''

        :return:
        '''
        name_label = sample_widget_template.label(set_text='Name')
        name_lineedit = sample_widget_template.line_edit(set_PlaceholderText='specify the object')
        pushButton = sample_widget_template.pushButton(set_text='Create CFX Setup')

        widget = sample_widget_template.grid_layout_set(list_object=[[name_label, name_lineedit],
                                                                     pushButton])

        print(widget)



