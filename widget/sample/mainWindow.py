from import_module import *



class SAMPLE_QMainWindow(QMainWindow):
    def __init__(self, parent=None, title='Sample Window', width=800, height=600):
        super(SAMPLE_QMainWindow, self).__init__(parent=parent)


        self.setWindowTitle(title)
        self.resize(width, height)


        self.menuBar_()

        self.statusBar().showMessage('')
        self.status_mouse_pos = QLabel('')
        self.statusBar().addPermanentWidget(self.status_mouse_pos)


    def menuBar_(self):
        '''

        :return:
        '''
        # create menu
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")
        menuBar.addMenu(editMenu)
        menuBar.addMenu(helpMenu)


    def getPosition(self):
        '''

        :return:
        '''
        pos = self.geometry()
        print(pos)


