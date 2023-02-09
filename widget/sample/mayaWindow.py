
from import_module import *
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import tempfile
from widget.sample import mainWindow
try:
    from importlib import reload
except:
    pass

for each in [mainWindow]:
    reload(each)


class mayaWindow_sample(MayaQWidgetDockableMixin, mainWindow.SAMPLE_QMainWindow):
    def __init__(self, title='Maya Window'):
        super(mayaWindow_sample, self).__init__(title=title)
        

        '''

        #SET WINDOW TITLE
        self.setWindowTitle(title)

        #SET WINDOW WIDGET
        if widget != '':
            self.setCentralWidget(widget)


        self.setGeometry(x, y, width, height)


        #SET STATUS BAR
        self.statusBar().showMessage(statusBar)

        #UPDATE
        self.update()
        '''

    def update(self):
        '''

        :return:
        '''
        self.setUserData()



    def setUserData(self):
        '''

        :return:
        '''
        tempDir = tempfile.gettempdir()
        print(tempDir)














