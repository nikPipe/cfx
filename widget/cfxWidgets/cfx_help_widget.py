from import_module import *
from widget.sample import sample_widget_template
for each in [sample_widget_template]:
    reload(each)






class CFX_HELP_WIDGET(QWidget):

    def __init__(self, parent):
        super(CFX_HELP_WIDGET, self).__init__()
        self.sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.parent_self = parent


        self.initUI()




    def initUI(self):
        '''

        :return:
        '''

        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=self)

        button = self.sample_widget_template.pushButton(set_text='Help Test',
                                                        connect=self.parent_self.update_def)
        verticalLayout.addWidget(button)






