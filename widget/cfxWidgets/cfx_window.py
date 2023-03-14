from import_module import *


from collections import OrderedDict

from widget.sample import mainWindow
from widget.sample import sample_widget_template
from widget.cfxWidgets import cfx_help_widget, cfx_rigfx_widget, cfx_setting_widget, cfx_side_main_widget, cfx_shelf_widget, save_data


for each in [mainWindow, sample_widget_template, cfx_help_widget, cfx_rigfx_widget, cfx_setting_widget, cfx_side_main_widget,
             cfx_shelf_widget, save_data]:
    reload(each)

import platform
import sys

class CFXWINDOW:
    def __init__(self):
        self.sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        self.cfx_help_widget_class = cfx_help_widget.CFX_HELP_WIDGET(self)
        self.cfx_rigfx_widget_class = cfx_rigfx_widget.CFX_RIGFX_WIDGET()
        self.cfx_setting_widget_class = cfx_setting_widget.CFX_SETTING_WIDGET()
        self.cfx_side_main_widget = cfx_side_main_widget.CFX_SIDE_MAIN_WIDGET(rig_fx_widget=self.cfx_rigfx_widget_class,
                                                                              setting_widget= self.cfx_setting_widget_class,
                                                                              help_widget=self.cfx_help_widget_class)
        self.cfx_shelf_widget = cfx_shelf_widget.CFX_SHELF_WIDGET()
        self.save_data_class = save_data.SAVE_DATA(self)



        self.window_name = 'CFX'
        self.width, self.height = self.save_data_class.get_size_from_jsonFile()
        self.left_side = 'Left'
        self.right_side = 'Right'
        self.top_side = 'Top'
        self.bottom_side = 'Bottom'

    def update_def(self):
        '''

        :return:
        '''
        print('this is updating')
        width = self.mainWindow.frameGeometry().width()
        height = self.mainWindow.frameGeometry().height()
        self.save_data_class.write_data()





    def cfx_window_(self):

        #CREATE MENU DIC
        menuDic = OrderedDict([

        ])

        if "maya" in sys.executable.lower():
            from widget.sample import mayaWindow
            reload(mayaWindow)
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

    def dockWidget(self, widget, side='Left', name='Dockable'):
        '''

        :return:
        '''
        dockWidget = QDockWidget(name, self.mainWindow)
        dockWidget.setWidget(widget)

        if side.lower() == self.left_side.lower():
            side_val = Qt.LeftDockWidgetArea

        elif side.lower() == self.right_side.lower():
            side_val = Qt.RightDockWidgetArea

        elif side.lower() == self.top_side.lower():
            side_val = Qt.TopDockWidgetArea

        elif side.lower() == self.bottom_side.lower():
            side_val = Qt.BottomDockWidgetArea

        else:
            side_val = Qt.LeftDockWidgetArea

        self.mainWindow.addDockWidget(side_val, dockWidget)

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


        #SET SIDE DOCKWIDGET
        self.dockWidget(self.cfx_side_main_widget, name='setting')

        #SHELF_WIDGET
        self.dockWidget(widget=self.cfx_shelf_widget, side=self.top_side, name='Shelf')

        widget = self.sample_widget_template.widget_def()
        verricalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        verricalLayout.addWidget(self.cfx_rigfx_widget_class)

        verricalLayout.addWidget(self.cfx_setting_widget_class)
        self.cfx_setting_widget_class.hide()

        verricalLayout.addWidget(self.cfx_help_widget_class)
        self.cfx_help_widget_class.hide()

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



