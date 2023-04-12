import customtkinter
import tkinter as tk
from tkinter import ttk

class jobType(customtkinter.CTkFrame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.general_frame = customtkinter.CTkFrame(self)
        # self.general_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ns")
        # self.general_frame.grid_columnconfigure(0, weight=1)


        self.header = customtkinter.CTkLabel(self, text="Job Type")
        
        # Create StringVar for all job types: rotors, conformers, fine, freq, opt, sp, bde
        self.rotor_var = tk.StringVar()
        self.conformer_var = tk.StringVar()
        self.fine_var = tk.StringVar()
        self.freq_var = tk.StringVar()
        self.opt_var = tk.StringVar()
        self.sp_var = tk.StringVar()
        self.bde_var = tk.StringVar()

        # Create CTkCheckboxes for all job types
        self.rotor_checkbox = customtkinter.CTkCheckBox(self, text="Rotors",command=lambda: self.checkbox_event(self.rotor_var),
                                                        variable=self.rotor_var, onvalue="on", offvalue="off")
        self.conformer_checkbox = customtkinter.CTkCheckBox(self,text="Conformers", command=lambda: self.checkbox_event(self.conformer_var),
                                                            variable=self.conformer_var, onvalue="on", offvalue="off")

        self.fine_checkbox = customtkinter.CTkCheckBox(self, text="Fine Scan",command=lambda: self.checkbox_event(self.fine_var),
                                                       variable=self.fine_var, onvalue="on", offvalue="off")
        self.freq_checkbox = customtkinter.CTkCheckBox(self, text="Frequency", command=lambda: self.checkbox_event(self.freq_var),
                                                       variable=self.freq_var, onvalue="on", offvalue="off")
        self.opt_checkbox = customtkinter.CTkCheckBox(self, text="Optimization", command=lambda: self.checkbox_event(self.opt_var),
                                                      variable=self.opt_var, onvalue="on", offvalue="off")
        self.sp_checkbox = customtkinter.CTkCheckBox(self, text="Single Point", command=lambda: self.checkbox_event(self.sp_var),
                                                     variable=self.sp_var, onvalue="on", offvalue="off")
        self.bde_checkbox = customtkinter.CTkCheckBox(self, text="Bond Dissociation Energy", command=lambda: self.checkbox_event(self.bde_var),
                                                      variable=self.bde_var, onvalue="on", offvalue="off")

        # Align all checkboxes, but in the center of the frame but aligned left
        self.rotor_checkbox.grid(row=0, column=0,pady=(10, 0), padx=(10,0),sticky="w")
        self.conformer_checkbox.grid(row=1, column=0,pady=(10, 0),padx=(10,20), sticky="w")
        self.fine_checkbox.grid(row=2, column=0,pady=(10, 0),padx=(10,0), sticky="w")
        self.freq_checkbox.grid(row=3, column=0, pady=(10,0), padx=(10, 20),sticky="w")
        self.opt_checkbox.grid(row=4, column=0, pady=(10,0), padx=(10, 20), sticky="w")
        self.sp_checkbox.grid(row=5, column=0, pady=(10,0), padx=(10, 20), sticky="w")
        self.bde_checkbox.grid(row=6, column=0, pady=(10,20), padx=(10, 20),sticky="w")
        

        




    def checkbox_event(self, var):
            print("checkbox toggled, current value:", var.get())