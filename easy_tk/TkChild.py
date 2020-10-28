import re
from tkinter import *
from tkinter.ttk import Separator

sablon = re.compile(r'(Frame|Entry|Button|Label|Separator|Radiobutton|Canvas|Scrollbar).*')


class TkChild(object):

    def __init__(self, name, data,modules=[]):
        self.name = name
        self.str_master = data.get("master")
        self.layout = data.get("layout")
        self.__grid = data.get("grid")
        self.__pack = data.get("pack")
        self.new_row = data.get("newRow")
        self.__config = data.get("config")
        self.methods = data.get("methods")
        self.grid_set_num = 0
        self.__master = object
        self.on_screen = False
        self.method_set_done = False
        make_modules(modules)

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, new_master):
        self.__master = new_master
        self.create_obj()

    @property
    def grid(self):
        return self.__grid

    @grid.getter
    def grid(self):
        if "row" in self.__grid:
            if self.new_row == True:
                self.master.row = True
            self.grid_set_num = 1
        if "column" in self.__grid:
            a = self.master.column
            self.grid_set_num = 2
        if "row" and "column" in self.__grid:
            self.grid_set_num = 3
        return self.__grid

    @property
    def pack(self):
        return self.__pack

    @pack.getter
    def pack(self):
        if self.__pack == None:
            return {}
        return self.__pack

    @property
    def config(self):
        return self.__config

    @pack.getter
    def config(self):
        if self.__config == None:
            return {}
        return self.__config

    def create_obj(self):
        obj = sablon.findall(self.name)
        if len(obj) > 0:
            master = self.__master.get()
            exec("self.obj = {}(master)".format(obj[0]))
            master = None

    def screen(self):
        if self.on_screen == False:
            if self.layout == "grid":
                self.set_grid()
                self.set_config()
                self.on_screen = True
            else:
                self.set_pack()
                self.set_config()
                self.on_screen = True

    def set_pack(self):
        pack = self.pack
        for i in pack:
            if type(pack[i]) == str:
                exec("self.obj.pack({} = '{}')".format(i, pack[i]))
            else:
                exec("self.obj.pack({} = {})".format(i, pack[i]))

    def set_grid(self):
        grid = self.grid
        for i in grid:
            exec("self.obj.grid({} = {})".format(i, self.__grid[i]))
        if self.grid_set_num == 0:
            if self.new_row == True:
                self.master.row = True
            self.obj.grid(row=self.master.row, column=self.master.column)

    def set_config(self):
        config = self.config
        for i in config:
            self.obj[i] = config[i]

    def get(self):
        return self.obj

    def get_methods(self):
        if self.methods != None and self.method_set_done == False:
            self.method_set_done = True
            return self.methods
        return []


modules = ["Frame","Entry","Button","Label","Separator","Radiobutton","Canvas","Scrollbar"]
def make_modules(list_modules):

    def make_module_name(name):
        return name.replace(".", "_")

    def make_re():
        modules = ""
        for i in modules:
            modules+=i+"|"

        modules = modules[0:-1]
        modules_re = re.compile(r'({}).*'.format(modules))
        return modules_re

    global sablon

    for i in range(len(list_modules)):
        name = make_module_name(list_modules[i].__name__)
        exec("global {}".format(name))
        exec("{} = lista[i]".format(name),locals(),globals())
        if name not in modules:
            modules.append(name)

    if len(list_modules) > 8:
        sablon = make_re()