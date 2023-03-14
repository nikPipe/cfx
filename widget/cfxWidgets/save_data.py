
import tempfile, os
import getpass as gt
from collections import OrderedDict
import json


class SAVE_DATA:
    def __init__(self, parent):
        '''

        :param parent:
        '''
        self.parent = parent

    def getSize(self):
        width = self.parent.mainWindow.frameGeometry().width()
        height = self.parent.mainWindow.frameGeometry().height()
        return width, height

    def get_size_from_jsonFile(self):
        '''

        :return:
        '''
        width = 500
        height = 800
        file_name = self.get_temp_file()
        with open(file_name) as user_file:
            file_contents = user_file.read()
            jsonfile = json.loads(file_contents)
            print(jsonfile)
            width = jsonfile['width']
            height = jsonfile['height']


        return width, height


    def write_data(self):
        '''

        :return:
        '''
        filePath = self.get_temp_file()

        with open(filePath, 'w') as fp:
            fp.write(self.getData())

    def getData(self):
        '''

        :return:
        '''
        order_dic = OrderedDict()
        order_dic['width'], order_dic['height'] = self.getSize()
        json_read = json.dumps(order_dic, indent=4)

        return json_read
    def get_temp_file(self):
        '''

        :return:
        '''
        #CREATE OR GET TEMP FILE IF EXIST

        file_name = gt.getuser() + '_CFX.json'
        print(file_name)

        path = tempfile.gettempdir()
        if '\\' in path:
            path = path.replace('\\', '/')

        listfile = os.listdir(path)
        fullPath = '/'.join([path, file_name])
        if file_name not in listfile:
            with open(fullPath, 'w') as fp:
                order_dic = OrderedDict()
                order_dic['width'], order_dic['height'] = 500, 800
                json_read = json.dumps(order_dic, indent=4)
                fp.write(json_read)

        return fullPath



