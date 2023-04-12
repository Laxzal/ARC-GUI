
import tkinter as tk
import customtkinter


class Levels(customtkinter.CTkFrame):
    
    def __init__(self, *args, header_name='Conformer Level', **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        # self.header = customtkinter.CTkLabel(self, text=self.header_name)
        # self.header.grid(row=0, column=0, columnspan=2)
        
        self.conformer_var = tk.StringVar()
        self.conformer_check = customtkinter.CTkCheckBox(self, text=self.header_name, 
                                                         command= lambda: self.checkbox_event(self.conformer_var),
                                                         variable=self.conformer_var, onvalue="on", offvalue="off", width=100)
        self.conformer_check.grid(row=0, column=0, sticky="w", columnspan=2)
        
        self.method_label = customtkinter.CTkLabel(self, text="method")
        self.method_label.grid(row=1, column = 0, sticky="e")
        
        self.method_entry = customtkinter.CTkEntry(self, placeholder_text="b3lyp", placeholder_text_color="gray", width=400)
        self.method_entry.grid(row=1, column=1)

        self.basis_label = customtkinter.CTkLabel(self, text="basis")
        self.basis_label.grid(row=2, column=0,sticky="e" )
        
        self.basis_entry = customtkinter.CTkEntry(self, placeholder_text="6-31g(d,p)", placeholder_text_color="gray", width=400)
        self.basis_entry.grid(row=2, column=1)
        
        self.aux_basis_label = customtkinter.CTkLabel(self, text="auxilary_basis")
        self.aux_basis_label.grid(row=3, column=0, sticky="e")
        
        self.aux_basis_entry = customtkinter.CTkEntry(self, placeholder_text="aug-cc-pVTZ/C cc-pVTZ-F12-CABS", placeholder_text_color="gray", width=400)
        self.aux_basis_entry.grid(row=3, column=1)
        
        self.dispersion_labl = customtkinter.CTkLabel(self, text="dispersion")
        self.dispersion_labl.grid(row=4, column=0, sticky='e')
        
        self.dispersion_entry = customtkinter.CTkEntry(self, placeholder_text='empiricaldispersion=gd3b', placeholder_text_color='gray', width=400)
        self.dispersion_entry.grid(row=4, column=1)
        
        self.args_label = customtkinter.CTkLabel(self, text='args')
        self.args_label.grid(row=5, column=0, sticky='e')
        
        self.args_entry = customtkinter.CTkEntry(self,width=400)
        self.args_entry.grid(row=5, column=1)
        
        self.software_label = customtkinter.CTkLabel(self, text='software')
        self.software_label.grid(row=6, column=0, sticky='e')
        
        self.software_entry = customtkinter.CTkEntry(self,placeholder_text='orca', placeholder_text_color='gray', width=400)
        self.software_entry.grid(row=6, column=1)
        
    def checkbox_event(self, var):
        print("Checkbox toggled, current value:", var.get())
        
    
    def store_values(self):
        self.method_store = self.method_entry.get() if self.method_entry.get()!= '' else None
        self.basis_store = self.basis_entry.get() if self.basis_entry.get()!= '' else None
        self.aux_basis_store = self.aux_basis_entry.get() if self.aux_basis_entry.get() != '' else None
        self.dispersion_store = self.dispersion_entry.get() if self.dispersion_entry.get() != '' else None
        self.args_store = self.args_entry.get() if self.args_entry.get() != '' else None
        self.software_store = self.software_entry.get() if self.software_entry.get() != '' else None
        
        return {'method':self.method_store,
                'basis': self.basis_store,
                'aux_basis': self.aux_basis_store,
                'dispersion': self.dispersion_store,
                'args': self.args_store,
                'software': self.software_store}