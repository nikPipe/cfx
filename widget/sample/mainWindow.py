from import_module import *



class SAMPLE_QMainWindow(QMainWindow):
    def __init__(self, parent=None, title='Sample Window', width=800, height=600):
        super(SAMPLE_QMainWindow, self).__init__(parent=parent)


        self.setWindowTitle(title)
        self.resize(width, height)
