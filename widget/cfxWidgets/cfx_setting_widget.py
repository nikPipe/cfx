from import_module import *
from widget.sample import sample_widget_template
for each in [sample_widget_template]:
    reload(each)






class CFX_SETTING_WIDGET(QWidget):

    def __init__(self):
        super(CFX_SETTING_WIDGET, self).__init__()
        self.sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        self.initUI()


    def initUI(self):
        '''

        :return:
        '''

        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=self)

        button = self.sample_widget_template.pushButton(set_text='Setting Test')
        verticalLayout.addWidget(button)


