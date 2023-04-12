import customtkinter
import tkinter as tk

class DataBase(customtkinter.CTkFrame):
    
    def __init__(self, *args, header_name, **kwargs,):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        
        self.header_label = customtkinter.CTkLabel(self, text=self.header_name, width=800)
        self.header_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.left_heading = customtkinter.CTkLabel(self, text='Unselected')
        self.left_heading.grid(row=2, column=0, padx=5, pady=5)
        self.right_heading = customtkinter.CTkLabel(self, text='Selected')
        self.right_heading.grid(row=2, column=2, padx=5, pady=5)
        
        self.option_dict={'Thermo Database':["primaryThermoLibrary","DFT_QCI_thermo","GRI-Mech3.0",
                               "CBS_QB3_1dHR","thermo_DFT_CCSDTF12_BAC","SABIC_aromatics",
                               "C3","Fulvene_H","BurkeH2O2","Chlorinated_Hydrocarbons",
                               "heavy_oil_ccsdtf12_1dHR","Narayanaswamy","CHN","CHOFClBr_G4",
                               "vinylCPD_H","CHOFBr_G4","CHOClBr_G4","SABIC_aromatics_1dHR",
                               "SulfurGlarborgH2S","CHOFCl_G4","naphthalene_H","s3_5_7_ane",
                               "NOx2018","iodinated_Hydrocarbons","JetSurF1.0",
                               "SulfurGlarborgMarshall","SABIC_aromatics_1dHR_extended",
                               "CH","NitrogenCurran","CHO","bio_oil","2-BTP","SulfurLibrary",
                               "CHOCl_G4","C10H11","CHON_G4","Klippenstein_Glarborg2016",
                               "2-BTP_G4","primaryNS","CurranPentane","halogens","USC-Mech-ii",
                               "GRI-Mech3.0-N","Fluorine","JetSurF2.0","FFCM1(-)","Chlorination",
                               "SulfurGlarborgNS","CHOBr_G4","surfaceThermoNi111","surfaceThermoPt111",
                               "NISTThermoLibrary","Lai_Hexylbenzene","SulfurHaynes","CN","BurcatNS",
                               "SulfurGlarborgBozzelli","Chernov","Spiekermann_refining_elementary_reactions",
                               "CHOF_G4","CHON"],
                          'Kinetics Database':['1989_Stewart_2CH3_to_C2H5_H', '2-BTP/full', '2-BTP/seed', 
                                '2001_Tokmakov_H_Toluene_to_CH3_Benzene', 
                                '2003_Miller_Propargyl_Recomb_High_P', 
                                '2005_Senosiain_OH_C2H2', '2006_Joshi_OH_CO', 
                                '2009_Sharma_C5H5_CH3_highP', '2015_Buras_C2H3_C4H6_highP', 
                                'Aromatics_high_pressure/C10H10_1', 
                                'Aromatics_high_pressure/C10H10_2', 
                                'Aromatics_high_pressure/C10H10_H_abstraction', 
                                'Aromatics_high_pressure/C10H11_1', 
                                'Aromatics_high_pressure/C10H11_2', 
                                'Aromatics_high_pressure/C10H11_3', 
                                'Aromatics_high_pressure/C10H11_4', 
                                'Aromatics_high_pressure/C10H7', 
                                'Aromatics_high_pressure/C10H8_H_abstraction_H_recomb',
                                'Aromatics_high_pressure/C10H9_1', 
                                'Aromatics_high_pressure/C10H9_2', 
                                'Aromatics_high_pressure/C10H9_3', 
                                'Aromatics_high_pressure/C10H9_4', 'Aromatics_high_pressure/C12H10_1', 
                                'Aromatics_high_pressure/C12H10_2', 'Aromatics_high_pressure/C12H10_H_abstraction', 
                                'Aromatics_high_pressure/C12H11', 'Aromatics_high_pressure/C12H8_H_abstraction', 
                                'Aromatics_high_pressure/C12H9', 'Aromatics_high_pressure/C14H10_H_abstraction_H_recomb', 
                                'Aromatics_high_pressure/C14H11_1', 'Aromatics_high_pressure/C14H11_2', 'Aromatics_high_pressure/C14H11_3', 
                                'Aromatics_high_pressure/C14H11_4', 'Aromatics_high_pressure/C14H9', 'Aromatics_high_pressure/C16H11', 
                                'Aromatics_high_pressure/C7H8', 'Aromatics_high_pressure/C7H8_H_abstraction', 'Aromatics_high_pressure/C7H9', 
                                'Aromatics_high_pressure/C8H5O2_H_abstraction', 'Aromatics_high_pressure/C8H5O2_oxid_CO', 
                                'Aromatics_high_pressure/C8H5O2_oxid_CO2', 'Aromatics_high_pressure/C8H6_1', 'Aromatics_high_pressure/C8H6_2', 
                                'Aromatics_high_pressure/C8H6_H_abstraction', 'Aromatics_high_pressure/C8H7_1', 'Aromatics_high_pressure/C8H7_2', 
                                'Aromatics_high_pressure/C8H7_3', 'Aromatics_high_pressure/C8H7_H_abstraction', 'Aromatics_high_pressure/C8H8', 
                                'Aromatics_high_pressure/C9H5_H_abstraction', 'Aromatics_high_pressure/C9H5_oxid_CO', 'Aromatics_high_pressure/C9H5_oxid_CO2', 
                                'Aromatics_high_pressure/C9H6_1', 'Aromatics_high_pressure/C9H6_2', 'Aromatics_high_pressure/C9H6_H_abstraction', 
                                'Aromatics_high_pressure/C9H7',    "Aromatics_high_pressure/C9H8_1",
                                "Aromatics_high_pressure/C9H8_2",
                                "Aromatics_high_pressure/C9H8_H_abstraction",
                                "Aromatics_high_pressure/C9H9_1",
                                "Aromatics_high_pressure/C9H9_2",
                                "BurkeH2O2inArHe","BurkeH2O2inN2","C10H11","C12H11_pdep","C2H2_init","C2H4+O_Klipp2017","C3","C6H5_C4H4_Mebel","CF2BrCl","CH3Cl",
                                "Chernov","CurranPentane","DMSOxy","DTU_mech_CH3Cl","Dooley/C1","Dooley/methylformate","Dooley/methylformate_2",
                                "Dooley/methylformate_all_ARHEbathgas","Dooley/methylformate_all_N2bathgas","ERC-FoundationFuelv0.9",
                                "Ethylamine","FFCM1(-)","First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP","First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP","First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP",
                                "First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP","First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP","First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP","First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP",
                                "First_to_Second_Aromatic_Ring/2017_Mebel_C6H5C2H2_C2H2_highP","First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C2H2_highP","First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP","First_to_Second_Aromatic_Ring/phenyl_diacetylene_effective",'Fulvene_H', 
                                'GRI-HCO', 'GRI-Mech3.0', 'GRI-Mech3.0-N', 'Glarborg/C0', 'Glarborg/C1', 'Glarborg/C2', 'Glarborg/C3', 'Glarborg/highP', 'HydrazinePDep', 'Iodine-R_recombination', 'JetSurF1.0', 'JetSurF2.0', 'Klippenstein_Glarborg2016', 'Lai_Hexylbenzene', 'Mebel_C6H5_C2H2', 'Mebel_Naphthyl', 'Methylformate', 'N-S_interactions', 
                                'NIST_Fluorine/CH2F2/full', 'NIST_Fluorine/CH2F2/seed', 'NIST_Fluorine/full', 'NIST_Fluorine/seed', 'NOx2018', 'Narayanaswamy', 'Nitrogen_Dean_and_Bozzelli', 'Nitrogen_Glarborg_Gimenez_et_al', 'Nitrogen_Glarborg_Lucassen_et_al', 'Nitrogen_Glarborg_Zhang_et_al', 'Sulfur/DMDS', 'Sulfur/DMS', 'Sulfur/DTBS', 'Sulfur/GlarborgBozzelli', 
                                'Sulfur/GlarborgH2S', 'Sulfur/GlarborgH2S/alt', 'Sulfur/GlarborgMarshall', 'Sulfur/GlarborgNS', 'Sulfur/HSSH_1bar', 'Sulfur/Hexanethial_nr', 'Sulfur/Sendt', 'Sulfur/TP_Song', 'Sulfur/Thial_Hydrolysis', 'Surface/Ammonia/Duan_Ni111', 'Surface/Ammonia/Duan_Ni211', 'Surface/Ammonia/Kraehnert_Pt111', 'Surface/Ammonia/Novell_Pd111', 'Surface/Ammonia/Novell_Pt111', 
                                'Surface/Ammonia/Novell_Rh111', 'Surface/Ammonia/Offermans_Pt111', 'Surface/Ammonia/Popa_Rh111', 'Surface/Ammonia/Rebrov_Pt111', 'Surface/Ammonia/Roldan_Ru0001', 'Surface/Ammonia/Scheuer_Pt', 'Surface/Ammonia/Schneider_Pd111', 'Surface/Ammonia/Schneider_Pd211', 'Surface/Ammonia/Schneider_Pt111', 'Surface/Ammonia/Schneider_Pt211', 'Surface/Ammonia/Schneider_Rh111',"Surface/Ammonia/Schneider_Rh211",
                                "Surface/Ammonia/Vlachos_Ru0001","Surface/CPOX_Pt/Deutschmann2006_adjusted","Surface/DOC/Arevalo_Pt111","Surface/DOC/Ishikawa_Rh111","Surface/DOC/Mhadeshwar_Pt111","Surface/DOC/Nitrogen","Surface/Example","Surface/Hydrazine/Roldan_Cu111","Surface/Hydrazine/Roldan_Ir111","Surface/Methane/Deutschmann_Ni","Surface/Methane/Deutschmann_Ni_full"
                                ,"Surface/Methane/Deutschmann_Pt","Surface/Methane/Vlachos_Pt111","Surface/Methane/Vlachos_Rh","TEOS","YF/full","YF/seed","biCPD_H_shift","c-C5H5_CH3_Sharma","combustion_core/version2","combustion_core/version3","combustion_core/version4","combustion_core/version5","fascella","kislovB","naphthalene_H","primaryH2O2","primaryNitrogenLibrary",
                                "primaryNitrogenLibrary/LowT","primarySulfurLibrary","vinylCPD_H"
                                ]
        }
        
        # Create an entry box to search for database
        self.search_DB = customtkinter.CTkEntry(self, width=25, placeholder_text=f'Search {self.header_name}', placeholder_text_color='grey')
        self.search_DB.grid(row=1, column=0, padx=5, pady=5, columnspan=1, sticky='ew')
        self.search_DB.bind('<KeyRelease>', self.search_database)
        self.search_DB.bind('<Return>', self.search_database)
        
    
            #Create pair of listboxes
        self.left_listbox = tk.Listbox(self, width=35, height=10, selectmode=tk.EXTENDED)
        self.left_listbox.grid(row=3, column=0, padx=5, pady=5, rowspan=2)
        self.right_listbox = tk.Listbox(self, width=35, height=10, selectmode=tk.EXTENDED)
        self.right_listbox.grid(row=3, column=2, padx=5, pady=5, rowspan=2)
        
        self.original_index = { item: index for index, item in enumerate(self.option_dict[self.header_name])}
        self.selected_items = []
        self.unselected_items = list(self.option_dict[self.header_name])
        for item in self.unselected_items:
            self.left_listbox.insert("end", item)
            
                # Create buttons to move items between listboxes
        self.db_button_add = customtkinter.CTkButton(self, text='>>', command=lambda: self.move_items(self.left_listbox, self.right_listbox))
        self.db_button_add.grid(row=3, column=1, padx=5, pady=5)
        self.db_button_remove = customtkinter.CTkButton(self, text='<<', command=lambda: self.move_items(self.right_listbox, self.left_listbox))
        self.db_button_remove.grid(row=4, column=1, padx=5, pady=5)
        
        # Create an entry box that allows for user to input thermo database
        self.db_database = customtkinter.CTkEntry(self, width=30, placeholder_text='Enter custom thermo library', placeholder_text_color='grey')
        self.db_database.grid(row=1, column=2, padx=5, pady=5, columnspan=1, sticky='ew')
        self.db_database_button = customtkinter.CTkButton(self, text='Enter', command=lambda: self.add_database(self.db_database.get()))
        self.db_database_button.grid(row=1, column=3, padx=5, pady=5)
        self.db_database_button.bind('<Return>', command=self.del_text)
    # Define a function to move items between Listboxes
    def move_items(self,left_listbox, right_listbox):
        selected_indices = left_listbox.curselection()
        for index in reversed(selected_indices):
            try:
                o_idx = self.original_index[left_listbox.get(index)]
                right_listbox.insert(o_idx, left_listbox.get(index))
            except KeyError:
                right_listbox.insert("end", left_listbox.get(index))
            left_listbox.delete(index)
    
    # Define a function to search for thermo database
    def search_database(self, event):
        search_term = self.search_thermo.get()
        self.left_listbox.delete(0, "end")
        for item in self.unselected_items:
            if search_term.lower() in item.lower():
                self.left_listbox.insert("end", item)
            
    # Define a function to add thermo database
    def add_database(self, database):
        #self.unselected_items.append(thermo_database)
        self.right_listbox.insert("end", database)     
    
    def del_text(self):
        
        self.db_database.delete(0, "end")