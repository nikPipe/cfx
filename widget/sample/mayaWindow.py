
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














