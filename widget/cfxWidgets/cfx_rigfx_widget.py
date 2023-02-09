from import_module import *
from widget.sample import sample_widget_template
for each in [sample_widget_template]:
    reload(each)






class CFX_RIGFX_WIDGET:

    def __init__(self):
        self.sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()


    def widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()

        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        button = self.sample_widget_template.pushButton(set_text='Test')
        verticalLayout.addWidget(button)


        return widget
