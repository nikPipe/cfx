from import_module import *
from widget.sample import sample_widget_template
for each in [sample_widget_template]:
    reload(each)

class CFX_RIGFX_WIDGET(QWidget):

    def __init__(self):
        super(CFX_RIGFX_WIDGET, self).__init__()
        self.sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        self.initUI()


    def initUI(self):
        '''

        :return:
        '''

        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=self)

        #RIGX AND TEMPLATE TABWIDGET
        tabWidget = self.sample_widget_template.tab_widget(parent_self=self)
        verticalLayout.addWidget(tabWidget)

        #ADD RIGFX WIDGET
        tabWidget.addTab(self.rigfx_widget(), 'RigFX')

        #ADD TEMPLATE WIDGET
        tabWidget.addTab(self.template_widegt(), 'Template')


        #button = self.sample_widget_template.pushButton(set_text='Rigx Test')
        #verticalLayout.addWidget(button)


    def rigfx_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        splitter_rigfx_create = self.sample_widget_template.splitter_def(parent_self=self,
                                                                        set_orientation=self.sample_widget_template.horizonatal)

        splitter_rigfx_create.addWidget(self.rigfx_treeWidget())
        splitter_rigfx_create.addWidget(self.rigfx_create_blend_widget())


        splitter_rigfx_button = self.sample_widget_template.splitter_def(parent_self=self,
                                                                        set_orientation=self.sample_widget_template.vertical)

        verticalLayout.addWidget(splitter_rigfx_button)

        splitter_rigfx_button.addWidget(splitter_rigfx_create)
        splitter_rigfx_button.addWidget(self.rigx_extra_button_widget())


        return widget

    def rigfx_treeWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        #TREEWIDGET LINEEDIT
        treewidget_lineedit = self.sample_widget_template.line_edit()
        verticalLayout.addWidget(treewidget_lineedit)

        #TREEWIDGET
        treewidget = self.sample_widget_template.treeWidget(parent_self=self)
        verticalLayout.addWidget(treewidget)

        return widget

    def rigfx_create_blend_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        #CREATE AND BLEND TAB
        tabWidget = self.sample_widget_template.tab_widget(parent_self=self)
        verticalLayout.addWidget(tabWidget)

        #CREATE WIDGET
        tabWidget.addTab(self.rigfx_create_widget(), 'Create')
        tabWidget.addTab(self.rigfx_blend_widget(), 'Blend')


        return widget


    def rigfx_create_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        # CREATE AND BLEND TAB
        tabWidget = self.sample_widget_template.tab_widget(parent_self=self)
        verticalLayout.addWidget(tabWidget)

        return widget

    def rigfx_blend_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        # CREATE AND BLEND TAB
        tabWidget = self.sample_widget_template.tab_widget(parent_self=self)
        verticalLayout.addWidget(tabWidget)

        return widget

    def rigx_extra_button_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        # CREATE AND BLEND TAB
        tabWidget = self.sample_widget_template.tab_widget(parent_self=self)
        verticalLayout.addWidget(tabWidget)

        return widget

    def template_widegt(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        splitter_template_local_server_create = self.sample_widget_template.splitter_def(parent_self=self,
                                                                                         set_orientation=self.sample_widget_template.vertical)
        verticalLayout.addWidget(splitter_template_local_server_create)

        splitter_template_local_server_create.addWidget(self.template_server_widget())
        splitter_template_local_server_create.addWidget(self.template_local_widget())


        return widget

    def template_server_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        #LABEL
        server_label = self.sample_widget_template.label(set_text='Server', set_alighment=self.sample_widget_template.center_alignment)
        verticalLayout.addWidget(server_label)

        treeWidget = self.sample_widget_template.treeWidget()
        verticalLayout.addWidget(treeWidget)

        return widget

    def template_local_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget_template.widget_def()
        verticalLayout = self.sample_widget_template.vertical_layout(parent_self=widget)

        # LABEL
        local_label = self.sample_widget_template.label(set_text='Local',
                                                         set_alighment=self.sample_widget_template.center_alignment)
        verticalLayout.addWidget(local_label)

        treeWidget = self.sample_widget_template.treeWidget()
        verticalLayout.addWidget(treeWidget)

        return widget











