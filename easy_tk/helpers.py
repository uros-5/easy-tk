widgets = {}
class WindowScrollbar(object):

    def __init__(self,easy):
        global widgets
        widgets = easy

    def set_scrollbar(self):
        self.grid_config_container()
        self.canvas_methods()
        self.scrollbar_methods()
        self.frame2_methods()
    
    def grid_config_container(self):
        container = widgets.get("FrameContainer")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    def canvas_methods(self):
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas = widgets.get("Canvas")
        scrollbar = widgets.get("Scrollbar")
        frame2 = widgets.get("Frame2")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((4, 4), window=frame2, anchor="nw",
                             tags="frame2")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def scrollbar_methods(self):
        scrollbar = widgets.get("Scrollbar")
        canvas = widgets.get("Canvas")
        scrollbar["command"] = canvas.yview

    def frame2_methods(self):
        def onFrameConfigure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        frame2 = widgets.get("Frame2")
        canvas = widgets.get("Canvas")
        frame2.bind("<Configure>", onFrameConfigure)

def new_name(name,widgets):
    widgets2 = []
    for i in widgets:
        if i.startswith(name):
            widgets2.append(i)
    name2 = f'{name}_{len(widgets2)+1}'
    return name2
