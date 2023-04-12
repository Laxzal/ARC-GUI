import customtkinter


class essSettings(customtkinter.CTkFrame):
    
    def __init__(self, *args, header_name="ESS Settings", **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, columnspan=2)
        
        self.list_of_col_locations = [3]
        # Create a button under the header called add location
        self.add_location_button = customtkinter.CTkButton(self, text="Add Location", command=self.add_location)
                                                        #    command=lambda: self.add_location(self.list_of_col_locations[-1] + 1, "event"))
        self.add_location_button.grid(row=1, column=0, columnspan=2)
        
        # Dictionary to store the labels and remove buttons
        self.labels_and_buttons = {}
        
    def add_location(self) -> None:
        # I want an Entry box to appear under the header with a button to remove it next to it and every entry box should have a unique column location
        # and also every remove button should remove the entry box that is next to it
        col = self.list_of_col_locations[-1] + 1
        
        location_label = customtkinter.CTkEntry(self)
        location_label.grid(row=1, column=col)
        # a button to remove the location
        remove_location_button = customtkinter.CTkButton(self, text="Remove Location", command=lambda: self.remove_location(col))
        remove_location_button.grid(row=2, column=col)
                # Append the label to the a dictionary of labels and their column location
        self.labels_and_buttons[col] = (location_label, remove_location_button)
        
        # Update the list of column locations
        self.list_of_col_locations.append(col)
    
    def remove_location(self, col) -> None:
        # Destroy the label and remove button
        self.labels_and_buttons[col][0].destroy()
        self.labels_and_buttons[col][1].destroy()
        
        # Remove the label and remove button from the dictionary
        del self.labels_and_buttons[col]
        
        # Update the list of column locations
        self.list_of_col_locations.remove(col)