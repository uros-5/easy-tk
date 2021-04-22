import json
import ast

from tkinter import *
from easy_tk.TkChild import TkChild
from easy_tk.TkMaster import TkMaster
from easy_tk.helpers import new_name

class EasyTk(object):

    def __init__(self):
        self.all_widgets = {}
        self.all_masters = {}
        self.all_methods = {}
        self.all_variables = {}
        self.modules = []

    def convert_json(self, file_name):
        file = open(file_name)
        self.json_data = json.load(file)
        file.close()

    def load_one(self,key):
        child = TkChild(key, self.json_data[key],self.modules,self.all_variables)
        child.master = self.get_master(child.str_master)
        self.add_widget(child.name, child)

    def add_widgets(self):
        for i in self.json_data:
            child = TkChild(i, self.json_data[i],self.modules,self.all_variables)
            child.master = self.get_master(child.str_master)
            self.add_widget(child.name, child)

    def add_widget(self, name, child):
        if name in self.all_widgets:
            name = new_name(name, self.all_widgets)
            self.all_widgets.setdefault(name, child)
        else:
            self.all_widgets.setdefault(name, child)

    def widgets_on_screen(self):
        for i in self.all_widgets:
            self.all_widgets[i].screen()

    def get_master(self, master):
        try:
            obj = self.all_widgets[master].get()
        except:obj = None
        finally:
            if master not in self.all_masters:
                tk_master = self.create_master(obj,master)
                self.all_masters.setdefault(master,tk_master)
            return self.all_masters[master]

    def set_root(self, root):
        child = TkChild("root", {})
        child.on_screen = True
        child.obj = root
        self.all_widgets.setdefault("root", child)
        self.all_masters.setdefault("root",self.create_master(root,'root'))

    def create_master(self,master_obj,name=""):
        master = TkMaster()
        master.obj = master_obj
        master.name = name
        return master

    def set_methods(self):
        for i in self.all_widgets:
            try:
                methods = self.all_widgets[i].get_methods()
                for j in methods:
                    try:
                        self.all_methods[j]()
                    except:
                        self.all_methods[j](self.all_widgets)
            except KeyError as e:
                print(f"Method [{j}] does not exist. [{i}]")
                continue

    def add_complete_widget(self,dict_easy):
        tk_child = dict_easy.get("TkChild")
        tk_master = dict_easy.get("TkMaster")
        if isinstance(tk_child,TkChild):
            self.all_widgets.setdefault(dict_easy["name"],dict_easy["TkChild"])
        if isinstance(tk_master,TkMaster):
            self.all_masters.setdefault(dict_easy["name"], dict_easy["TkMaster"])

    def set_modules(self,modules):
        self.modules = modules

    def import_methods(self,methods):
        self.all_methods = methods
    
    def import_variables(self,variables={}):
        self.all_variables = variables

    def add_method(self,name,method):
        self.all_methods.setdefault(name,method)

    def remove_widget(self,name=""):
        for child in list(self.all_widgets.keys()):
            if child != "root" and self.all_widgets[child].master.name == name:
                self.all_widgets[child].get().destroy()
                self.all_widgets.pop(child)

        for master in list(self.all_masters.keys()):
            if self.all_masters[master].name == name:
                self.all_masters[master].get().destroy()
                self.all_masters.pop(master)
    
    def change_frame_key(self,key,new_key):
        str_json_data = str(self.json_data)
        str_json_data = str_json_data.replace(key,new_key)
        self.json_data = ast.literal_eval(str_json_data)

