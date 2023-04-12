import customtkinter
import tkinter as tk
from tkinter import ttk
#import pandas as pd

class Species(customtkinter.CTkFrame):
    
    def __init__(self, header_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header_name = header_name
        
        # self.label = customtkinter.CTkLabel(self, text=self.header_name)
        # self.label.pack(pady=5, padx=5)
        
        # set default number of species blocks
        self.num_species_blocks = tk.StringVar()
        self.num_species_blocks.set('1')
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        num_species_menu_label = customtkinter.CTkLabel(self, text='Number of Species Blocks:', width=200)
        num_species_menu_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
        #num_species_menu = customtkinter.CTkComboBox(self, width=150, values=values, variable = self.num_species_blocks, state='readonly')
        num_species_menu = ttk.Combobox(self, width=2, textvariable=self.num_species_blocks, values=values, state='readonly')
        num_species_menu.grid(row=0, column=1)
        
        num_species_menu.bind('<<ComboboxSelected>>', self.on_select)
        #num_species_menu.bind('<<ComboboxSelected>>', self.update_rxn_grp)
        num_species_menu.current(0)
        self.species_blocks = []
        self.species_labels_blocks = []
        self.species_checks = []
        self.type_block = []
        self.rxn_grp_blck = []
        #self.on_select(event=int(self.num_species_blocks.get()))
        
        self.type_label = customtkinter.CTkLabel(self, text='Type')
        self.type_label.grid(row=0, column= 6)

        self.rxn_grp_label = customtkinter.CTkLabel(self, text='Reaction Group')
        self.rxn_grp_label.grid(row=0, column=7)
        self.rxn_dicts = dict()
    def on_select(self, event=None):
        # clear existing species blocks
        for block in self.species_blocks:
            block.destroy()
        self.species_blocks = []
        self.species_checks = []
        self.rxn_grp_blck = []
        
        for block in self.species_labels_blocks:
            block.destroy()
        self.species_labels_blocks = []
        
        for block in self.type_block:
            block.destroy()
        self.type_block = []
        
        for block in self.rxn_grp_blck:
            block.destroy()
        self.rxn_grp_blck=[]
        
        
        # create new species blocks
        self.num_blocks = int(self.num_species_blocks.get())
        for i in range(self.num_blocks):
            species_label = customtkinter.CTkLabel(self, text=f'Species {i+1}:')
            species_label.grid(row=i+2, column=0, padx=5, pady=5, sticky='e')
            species_label_entry = customtkinter.CTkEntry(self, width=200)
            species_label_entry.grid(row=i+2, column=1, padx=5, pady=5, sticky='w')
            
            #species_smiles = tk.Label(self.master, text=f'SMILES {i+1}:')
            #species_smiles.grid(row=i+2, column=3, padx=5, pady=5)
            species_adj_smiles = customtkinter.CTkComboBox(self, width=100, state='readonly',values=['SMILES', 'AdjacencyList'])
            species_adj_smiles.grid(row=i+2, column=3, padx=5, pady=5)
            species_adj_smiles.bind('ComboBoxSelected>>', self.incr_size_)
            species_adj_smiles_entry = customtkinter.CTkEntry(self, width=200)
            species_adj_smiles_entry.grid(row=i+2, column=4, padx=5, pady=5, sticky='w')

            reactive_var = tk.BooleanVar()
            reactive_var.set(0)
            reactive_check = customtkinter.CTkCheckBox(self, text="Reactive", variable=reactive_var)
            reactive_check.grid(row=i+2, column=5, padx=5, pady=5)
            
            type_var = tk.StringVar()
            type_var.set('')
            values = ['','Reactant', 'Product']
            type_check = customtkinter.CTkComboBox(self, width=150, values=values, variable=type_var, state='readonly')
            type_check.grid(row=i+2, column=6)
            
            rxn_var = tk.StringVar()
            
            div = int(self.num_species_blocks.get())//2
            rxn_grps = div if div != 0 else 1
            
            #values =['Reaction 1']
            values = [f"Reaction {i}" for i in range(1,rxn_grps+1)]
            rxn_grp = customtkinter.CTkComboBox(self, values=values,variable=rxn_var, state='readonly')
            rxn_grp.grid(row=i+2, column=7)
            
            
            self.rxn_grp_blck.append(rxn_grp)
            
            
            self.type_block.append(type_check)

            self.species_blocks.append(species_label_entry)
            self.species_blocks.append(species_adj_smiles)
            self.species_blocks.append(species_adj_smiles_entry)
            self.species_checks.append(reactive_var)
            self.species_labels_blocks.append(species_label)
            #self.species_labels_blocks.append(species_smiles)
            self.species_labels_blocks.append(reactive_check)
            
        #self.update_rxn_grp()
        
    # def update_rxn_grp(self, event=None):
        
        
    #     div = int(self.num_species_blocks.get())//2
    #     print(div)
    #     rxn_grps = div if div != 0 else 1
    #     print(rxn_grps)
    #     for i in range(len(self.rxn_grp_blck)):
    #         self.rxn_grp_blck[i].values = [f"Reaction {i}" for i in range(1,rxn_grps+1)]
    #         print(self.rxn_grp_blck[i])
    #         print(self.rxn_grp_blck[i].values)
    #     print(self.rxn_grp_blck)
    
    def incr_size_(self, event=None):
        
        for i in self.species_adj_smiles:
            print(i)
            if self.species_adj_smiles[i].get() == 'SMILES':
                self.species_blocks[i+2]._set_dimension(width=200, height=200)
    
    def generate_reaction_connections(self):
        
        # Get the labels
        # get the type
        # Get the reaction_label
        #rxn_df = pd.DataFrame()
        
        self.rxn_dicts = {}
        
        for i in range(0,len(self.species_blocks),3):
            rxn_grp = self.rxn_grp_blck[i//3].get()
            print(rxn_grp)
            
            
            spec_label =self.species_blocks[i].get()
            print(spec_label)

            type_rxn = self.type_block[i//3].get()
            print(type_rxn)
            
            try: 
                if self.rxn_dicts[rxn_grp]:
                    if self.rxn_dicts[rxn_grp][type_rxn]:
                        print('listing')
                        temp_list = [self.rxn_dicts[rxn_grp][type_rxn]]
                        temp_list.append(spec_label)
                        self.rxn_dicts[rxn_grp][type_rxn] = temp_list
                    else:
                        print('cant list')
                        print(self.rxn_dicts[rxn_grp][type_rxn])
                        self.rxn_dicts[rxn_grp][type_rxn]=spec_label
                        
            
            except KeyError:
                print('KeyERRORED')
                try:
                    self.rxn_dicts[rxn_grp][type_rxn] = spec_label
                except KeyError:
                    self.rxn_dicts[rxn_grp] = {}
                    self.rxn_dicts[rxn_grp][type_rxn] = spec_label
                
            # if value exists for type_rxn
            # grab value - > list
            # append to list
            # type_rxn: list
            #else:
            # type_rxn:value
               
        print(self.rxn_dicts)
        
        return self.rxn_dicts
            
            