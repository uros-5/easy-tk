import re
from tkinter import *
from tkinter.ttk import Separator

modules_re = re.compile(r'(Frame|Entry|Button|Label|Separator|Radiobutton|Canvas|Scrollbar).*')
variable_re = re.compile(r'^var:(\w+$)')


class TkChild(object):

    def __init__(self, name, data, modules=[],variables={}):
        self.name = name
        self.str_master = data.get("master")
        self.layout = data.get("layout")
        self.__grid = data.get("grid")
        self.__pack = data.get("pack")
        self.__place = data.get("place")
        self.new_row = data.get("newRow")
        self.__config = data.get("config")
        self.methods = data.get("methods")
        self.grid_set_num = 0
        self.__master = object
        self.on_screen = False
        self.all_variables = variables
        self.method_set_done = False
        make_modules(modules)

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, new_master):
        if type(new_master.obj) == type(None):
            self.on_screen = True
            self.method_set_done = True
            print(f'Master [{self.str_master}] does not exist. [{self.name}] This widget is not created.')
            return
        self.__master = new_master
        self.create_obj()

    @property
    def grid(self):
        return self.__grid

    @grid.getter
    def grid(self):
        if self.new_row in (True, None):
            self.master.row = True
        if "row" in self.__grid and "column" not in self.__grid:
            self.grid_set_num = 1
        if "column" in self.__grid and "row" not in self.__grid:
            self.grid_set_num = 2
        if "row" in self.__grid and "column" in self.__grid:
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
        obj = modules_re.findall(self.name)
        if len(obj) > 0:
            master = self.__master.get()
            exec(f'self.obj = {obj[0]}(master)')
            master = None
        else:
            self.on_screen = True
            self.method_set_done = True
            print(f'Provided object ["{self.name}"] is not included in modules list. [{self.name}] This widget is not created.')

    def screen(self):
        if self.on_screen == False:
            if self.layout == "grid":
                self.set_grid()
                self.set_config()
                self.on_screen = True
            elif self.layout == "pack":
                self.set_pack()
                self.set_config()
                self.on_screen = True
            elif self.layout == "place":
                self.set_place()
                self.set_config()
                self.on_screen = True
            else:
                print(f'Layout [{self.layout}] on [{self.name}] does not exist.')

    def set_pack(self):
        pack = self.pack
        for i in pack:
            try:
                if type(pack[i]) == str:
                    variable = self.set_variable(pack[i])
                    if type(variable) == str:
                        exec(f"self.obj.pack({i} = '{variable}')")
                    else:
                        exec(f"self.obj.pack({i} = {variable})")
                else:
                    exec(f'self.obj.pack({i} = {pack[i]})')
            except NameError as e:
                print(e, f' [{self.name}]')
                self.set_none()
                return
            except Exception as e:
                print(f'Wrong attribute [{i}] for pack. [{self.name}] This widget is not created.')
                self.set_none()
                return
        self.obj.pack()

    def set_grid(self):
        grid = self.grid
        for i in grid:
            try:
                if type(grid[i]) == str:
                    variable = self.set_variable(grid[i])
                    if type(variable) == str:
                        exec(f"self.obj.grid({i} = '{variable}')")
                    else:
                        exec(f"self.obj.grid({i} = {variable})")
                else:
                    exec(f'self.obj.grid({i} = {grid[i]})')
            except NameError as e:
                print(e,f' [{self.name}]')
                self.set_none()
                return
            except Exception:
                print(f'Wrong attribute [{i}] for grid. [{self.name}] This widget is not created.')
                self.set_none()
                return
        if self.grid_set_num == 0:
            self.obj.grid(row=self.master.row, column=self.master.column)
        elif self.grid_set_num == 1:
            self.obj.grid(column=0)
        elif self.grid_set_num == 2:
            self.obj.grid(row=self.master.row)
    
    def set_place(self):
        place = self.__place
        for i in place:
            try:
                if type(place[i]) == str:
                    variable = self.set_variable(place[i])
                    if type(variable) == str:
                        exec(f"self.obj.place({i} = '{variable}')")
                    else:
                        exec(f"self.obj.place({i} = {variable})")
                else:
                    exec(f'self.obj.place({i} = {place[i]})')
            except NameError as e:
                print(e, f' [{self.name}]')
                self.set_none()
                return
            except Exception:
                print(f'Wrong attribute [{i}] for place. [{self.name}] This widget is not created.')
                self.set_none()
                return

    def set_config(self):
        config = self.config
        for i in config:
            try:
                self.obj[i] = self.set_variable(config[i])
            except:
                print(f'Attribute [{i}] is unknown option for config.  [{self.name}]')
                return

    def get(self):
        return self.obj

    def get_methods(self):
        if self.methods != None and self.method_set_done == False:
            self.method_set_done = True
            return self.methods
        return []

    def set_none(self):
        self.obj = 0
        self.method_set_done = True
        self.__config = {}

    def set_variable(self,value):
        if type(value) == type(""): 
            var = variable_re.findall(value)
            if len(var) > 0:
                #input(">>>")
                return self.all_variables[var[0]]
            else:
                return value
        return value


modules = ["Frame", "Entry", "Button", "Label", "Separator", "Radiobutton", "Canvas", "Scrollbar"]

def make_modules(list_modules):
    global modules_re
    global modules

    def make_module_name(name):
        return name.replace(".", "_")

    def make_re():
        global modules
        temp_modules = ""
        for i in modules:
            temp_modules += i + "|"

        temp_modules = temp_modules[0:-1]
        modules_re = re.compile(f'({temp_modules}).*')
        return modules_re

    for i in range(len(list_modules)):
        name = make_module_name(list_modules[i].__name__)
        exec(f'global {name}')
        exec(f'{name} = list_modules[i]', locals(), globals())
        if name not in modules:
            modules.append(name)
    if len(list_modules) > 0:
        modules_re = make_re()

