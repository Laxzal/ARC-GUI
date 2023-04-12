import customtkinter
import tkinter as tk
from tkinter import ttk

class Reactions(customtkinter.CTkFrame):
    
    def __init__(self, header_label, species, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        self.reaction_label = customtkinter.CTkLabel(self, text=header_label)
        self.reaction_label.grid(row=0, column=0, padx = 10)
        
        self.generate_rxn = customtkinter.CTkButton(self,text='Generate Reaction List', command=self.gen_rxns)
        self.generate_rxn.grid(row=0, column=1)
        
        self.rxn_group_list = []
        self.rxn_label_list = []
    
        self.species_tab = species
    def gen_rxns(self, event=None):
        
        rxn_dict = self.species_tab.generate_reaction_connections()
        
        # Clear the labels
        for group, label in zip(self.rxn_label_list, self.rxn_group_list):
            group.destroy()
            label.destroy()
        
        for i, key in enumerate(rxn_dict.keys()):
            for low_key in rxn_dict[key]:
                if low_key == 'Reactant':
                    if isinstance(rxn_dict[key][low_key],list):
                        reactants = " + ".join(r for r in rxn_dict[key][low_key])
                    else:
                        reactants = rxn_dict[key][low_key]

                elif low_key == 'Product':
                    if isinstance(rxn_dict[key][low_key],list):
                        products = " + ".join(p for p in rxn_dict[key][low_key])
                    else:
                        products = rxn_dict[key][low_key]            
            full_rxn = reactants + ' <=> ' + products
            self.rxn_group = customtkinter.CTkLabel(self, text=key)
            self.rxn_group.grid(row=i+1, column = 0)
            self.rxn_label = customtkinter.CTkLabel(self, text=full_rxn)
            self.rxn_label.grid(row=1+i, column=1)
            
            # Append the group and label a list
            self.rxn_group_list.append(self.rxn_group)
            self.rxn_label_list.append(self.rxn_label)
            
            

                        
                
                
            
            
        