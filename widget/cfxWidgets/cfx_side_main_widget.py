from import_module import *
from widget.sample import sample_widget_template
for each in [sample_widget_template]:
    reload(each)






class CFX_SIDE_MAIN_WIDGET(QWidget):

    def __init__(self, rig_fx_widget, setting_widget, help_widget):
        super(CFX_SIDE_MAIN_WIDGET, self).__init__()
        self.sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        self.initUI(rig_fx_widget, setting_widget, help_widget)


    def initUI(self, rig_fx_widget, setting_widget, help_widget):
        '''

        :return:
        '''
        self.rig_fx_widget = rig_fx_widget
        self.setting_widget = setting_widget
        self.help_widget = help_widget




        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=self)

        button = self.sample_widget_template.pushButton(set_text='Rigfx', connect=self.rig_fx_def, set_status='Rigfx Button',
                                                        set_tool_tip='Rigfx')
        verticalLayout.addWidget(button)

        button = self.sample_widget_template.pushButton(set_text='setting', connect=self.setting_def, set_status='Setting')
        verticalLayout.addWidget(button)

        button = self.sample_widget_template.pushButton(set_text='help', connect=self.help_def, set_status='Help')
        verticalLayout.addWidget(button)



    def rig_fx_def(self):
        '''

        :return:
        '''
        print('this is rig fx')
        self.rig_fx_widget.show()
        self.setting_widget.hide()
        self.help_widget.hide()

    def setting_def(self):
        '''

        :return:
        '''
        print('this is rig setting')
        self.rig_fx_widget.hide()
        self.setting_widget.show()
        self.help_widget.hide()

    def help_def(self):
        '''

        :return:
        '''
        print('this is rig Help')
        self.rig_fx_widget.hide()
        self.setting_widget.hide()
        self.help_widget.show()