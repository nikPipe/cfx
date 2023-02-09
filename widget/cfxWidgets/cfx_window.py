from import_module import *


from collections import OrderedDict

from widget.sample import mainWindow
from widget.sample import sample_widget_template
from widget.cfxWidgets import cfx_help_widget, cfx_rigfx_widget, cfx_setting_widget, cfx_side_main_widget


for each in [mainWindow, sample_widget_template, cfx_help_widget, cfx_rigfx_widget, cfx_setting_widget, cfx_side_main_widget]:
    reload(each)

import platform
import sys

class CFXWINDOW:
    def __init__(self):
        self.sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        self.cfx_help_widget_class = cfx_help_widget.CFX_HELP_WIDGET()
        self.cfx_rigfx_widget_class = cfx_rigfx_widget.CFX_RIGFX_WIDGET()
        self.cfx_setting_widget_class = cfx_setting_widget.CFX_SETTING_WIDGET()
        self.cfx_side_main_widget = cfx_side_main_widget.CFX_SIDE_MAIN_WIDGET()

        self.window_name = 'CFX'
        self.width = 500
        self.height = 800

    def cfx_window_(self):

        #CREATE MENU DIC
        menuDic = OrderedDict([

        ])
        self.mainWindow = ''

        if "maya" in sys.executable.lower():
            from widget.sample import mayaWindow
            self.mainWindow = mayaWindow.mayaWindow_sample()
            self.setWindow_detail(self.mainWindow)
            self.mainWindow.setCentralWidget(self.widget_def(window=self.mainWindow))
            self.mainWindow.show(dockable=True)

        elif "houdini" in sys.executable.lower():
            import hou
            self.mainWindow = mainWindow.SAMPLE_QMainWindow(parent=hou.ui.mainQtWindow())
            self.mainWindow.setCentralWidget(self.widget_def(window=self.mainWindow))
            self.mainWindow.show()

        elif "blender" in sys.executable.lower():
            print("This script is running in Blender")
        elif "3dsmax" in platform.system().lower():
            print("This script is running in 3ds Max")
        elif "unity" in sys.executable.lower():
            print("This script is running in Unity")
        else:
            print("This script is running in an unknown 3D software environment")


        if self.mainWindow:
            self.setWindow_detail(self.mainWindow)


    def getUserData(self):
        '''

        :return:
        '''
        pass

    def setUserData(self):
        '''

        :return:
        '''
        pass


    def setWindow_detail(self, window):
        '''

        :param window:
        :return:
        '''
        window.setWindowTitle(self.window_name)
        window.resize(self.width, self.height)






    def widget_def(self, window):
        '''

        :return:
        '''
        cfx_help_widget_ = self.cfx_help_widget_class.widget()
        cfx_rigfx_widget_ = self.cfx_help_widget_class.widget()
        cfx_setting_widget_ = self.cfx_setting_widget_class.widget()
        cfx_side_main_widget_ = self.cfx_side_main_widget.widget()

        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)
        for each in [cfx_help_widget_, cfx_rigfx_widget_, cfx_setting_widget_, cfx_side_main_widget_]:
            verticalLayout.addWidget(each)



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



