import customtkinter

class projectInfo(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="projectInfo", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.pack()

        # Create a label for the entry box called Project Name
        self.project_name_label = customtkinter.CTkLabel(self, text="Project Name", anchor="center")
        self.project_name_label.pack()
        
        self.project_name_entry = customtkinter.CTkEntry(self)
        self.project_name_entry.pack()

    def get_value(self):
        """ returns selected value as a string, returns an empty string if nothing selected """
        return self.radio_button_var.get()

    def set_value(self, selection):
        """ selects the corresponding radio button, selects nothing if no corresponding radio button """
        self.radio_button_var.set(selection)