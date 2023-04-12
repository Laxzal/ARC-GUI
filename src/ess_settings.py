import customtkinter


class essSettings(customtkinter.CTkFrame):
    
    def __init__(self, *args, header_name="ESS Settings", **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, columnspan=2)
        
        self.list_of_col_locations = [3]
        # Create a button under the header called add location
        self.add_location_button = customtkinter.CTkButton(self, text="Add Location", command=lambda: self.add_location(self.list_of_col_locations[-1] + 1, "event"))
        self.add_location_button.grid(row=1, column=0, columnspan=2)
        
    def add_location(self, col, event) -> None:
        self.location_label = customtkinter.CTkEntry(self)
        self.location_label.grid(row=1, column=col)
        self.list_of_col_locations.append(col)

        