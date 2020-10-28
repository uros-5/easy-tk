from tkinter import Canvas, Frame, Scrollbar
import re

def grid_config_container(widgets):
    container = widgets.get("FrameContainer").get()
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

def canvas_methods(widgets):
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    canvas = widgets.get("Canvas").get()
    scrollbar = widgets.get("Scrollbar").get()
    frame2 = widgets.get("Frame2").get()
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((4, 4), window=frame2, anchor="nw",
                         tags="frame")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

def scrollbar_methods(widgets):
    scrollbar = widgets.get("Scrollbar").get()
    canvas = widgets.get("Canvas").get()
    scrollbar["command"] = canvas.yview

def frame2_methods(widgets):
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame2 = widgets.get("Frame2").get()
    canvas = widgets.get("Canvas").get()
    frame2.bind("<Configure>", onFrameConfigure)

def new_name(name,widgets):
    widgets2 = []
    for i in widgets:
        if i.startswith(name):
            widgets2.append(i)
    name2 = "{}_{}".format(name,len(widgets2)+1)
    return name2