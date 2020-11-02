from tkinter import *


class TkMaster(object):

    def __init__(self):
        self.name = ""
        self.layout = ""
        self.__row = 0
        self.__column = -1
        self.obj = object

    def get(self):
        return self.obj

    @property
    def column(self):
        return self.__column

    @column.getter
    def column(self):
        self.__column += 1
        return self.__column

    @property
    def row(self):
        return self.__row

    @row.getter
    def row(self):
        return self.__row

    @row.setter
    def row(self, increment):
        if increment == True:
            self.__row += 1
            self.__column = -1