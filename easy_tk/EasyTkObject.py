from tkinter import Tk
from easy_tk.EasyTk import EasyTk


class EasyTkObject(object):

    def __init__(self):
        self.easy = self.easy_factory()

    def create_root(self):
        self.root = Tk()
        self.easy.set_root(self.root)
        self.geometry = "519x434"

    def get(self,name,obj=True):
        if obj == True:
            return self.easy.all_widgets.get(name).get()
        elif obj == False:
            return self.easy.all_widgets.get(name)

    def import_methods(self,methods={}):
        self.easy.import_methods(methods)

    def import_modules(self,modules):
        self.easy.set_modules(modules)

    def import_variables(self,variables):
        self.easy.import_variables(variables)

    def open_file(self,file):
        self.easy.convert_json(file)

    def reading_from_json(self):
        self.easy.add_widgets()
        self.easy.widgets_on_screen()
        self.easy.set_methods()

    def start_root(self):
        self.root.geometry(self.geometry)
        self.root.grid()
        self.root.mainloop()

    def add_just_one(self,file_name,key):
        self.easy.convert_json(file_name)
        self.easy.load_one(key)

    def easy_factory(self):
        return EasyTk()