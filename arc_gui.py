import tkinter as tk
import customtkinter
from radiobutton import RadioButtonFrame
from typing import Optional, Union, Tuple

class App(customtkinter.CTk):

    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("1200x800")
        self.title("RadioButtonFrame test")

        app = TabApp(master=self)
        app.pack(fill="both", expand=True)

class TabApp(customtkinter.CTkTabview):
    def __init__(self, master: tk.Widget, **kwargs):
        super().__init__(master)



        self.add("tab 1")
        self.add("tab 2")
        self.tab_view = RadioButtonFrame(master=self.tab("tab 1"))
        self.tab_view.pack(fill="both", expand=True)



app = App()
app.mainloop()