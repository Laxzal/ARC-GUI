import tkinter as tk
import customtkinter
from radiobutton import projectInfo
from src.ess_settings import essSettings
from typing import Optional, Union, Tuple
from src.jobtype import jobType
from src.conformerlvl import ConformerLevel
from src.splvl import SPLevel
from src.tsguesslvl import TSGuessLevel
from src.optlvl import OptLevel
from src.freqlvl import FreqLevel
from src.compmethd import CompositeMethod
from src.scanlvl import ScanLevel
from src.irclvl import IRCLevel
from src.orbitalvl import OrbitalLevel
from src.thermodb import ThermoDatabase
from src.kineticdb import KinteticsDatabase
from src.species import Species
from src.reactions import Reactions
class App(customtkinter.CTk):

    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("1600x1200")
        self.title("ARC GUI")

        app = TabApp(master=self)
        app.pack(fill="both", expand=True)

class TabApp(customtkinter.CTkTabview):
    def __init__(self, master: tk.Widget, **kwargs):
        super().__init__(master)


        # opt frew composit_method, scan irc orbitals

        self.add("Project Information")
        self.add("ESS Settings")
        self.add("Job Type")
        self.add("Levels")
        # self.add("Database [RMG]")
        self.add("Species Generator [RMG]")
        self.add('Reactions')


        self.tab_view = projectInfo(master=self.tab("Project Information"))
        self.tab_view.pack(fill="both", expand=True,anchor="center")
        self.tab_view2 = essSettings(master=self.tab("ESS Settings"), header_name="Gassian")
        self.tab_view2.pack(fill="both", expand=True,anchor="center")
        self.tab_view3 = essSettings(master=self.tab("ESS Settings"), header_name="Q-Chem")
        self.tab_view3.pack(fill="both", expand=True,anchor="center")
        self.tab_view4 = essSettings(master=self.tab("ESS Settings"), header_name="Molpro")
        self.tab_view4.pack(fill="both", expand=True,anchor="center")
        self.tab_view5 = essSettings(master=self.tab("ESS Settings"), header_name="Orca")
        self.tab_view5.pack(fill="both", expand=True,anchor="center")
        self.tab_view6 = essSettings(master=self.tab("ESS Settings"), header_name="TeraChem")
        self.tab_view6.pack(fill="both", expand=True,anchor="center")

        self.tab_view7 = jobType(master=self.tab("Job Type"))
        self.tab_view7.pack(side=tk.TOP, anchor="center")
        
        self.tab_view8 = ConformerLevel(master=self.tab("Levels"), header_name="Conformer Level")
        #self.tab_view8.pack(fill='none', expand=False, anchor="nw")
        self.tab_view8.grid(row=0, column= 0)
        self.tab_view9 = SPLevel(master= self.tab("Levels"), header_name="Single Point Level")
        self.tab_view9.grid(row=0, column = 1)

        self.tab_view10 = TSGuessLevel(master=self.tab("Levels"), header_name="TS Guess Level")
        #self.tab_view10.pack(fill="none", expand=False, anchor="nw")
        self.tab_view10.grid(row=0, column=2)
        self.tab_view11 = OptLevel(master=self.tab("Levels"), header_name="Opt Level")
        #self.tab_view11.pack(fill="none", expand=False, anchor="nw")
        self.tab_view11.grid(row=1, column=0)
        
        self.tab_view12 = FreqLevel(master=self.tab("Levels"), header_name="Freq Level")
        #self.tab_view12.pack(fill='none', expand=False,  anchor="nw", side=tk.TOP)
        self.tab_view12.grid(row=1, column=1)
        
        self.tab_view13 = CompositeMethod(master=self.tab("Levels"), header_name="Composite Method")
        self.tab_view13.grid(row=1, column=2)
        
        self.tab_view14 = ScanLevel(master=self.tab("Levels"), header_name="Scan Level")
        self.tab_view14.grid(row=2, column=0)
        
        self.tab_view15= IRCLevel(master=self.tab("Levels"), header_name="IRC Level")
        self.tab_view15.grid(row=2, column=1)
        
        self.tab_view16 = OrbitalLevel(master=self.tab("Levels"), header_name="Orbital Level")
        self.tab_view16.grid(row=2, column=2)
        
        # self.tab_view17 = ThermoDatabase(master=self.tab("Database [RMG]"), header_name='Thermo Database')
        # self.tab_view17.grid(row=0, column=0)
        
        # self.tab_view18 = KinteticsDatabase(master=self.tab("Database [RMG]"), header_name="Kinetics Database")
        # self.tab_view18.grid(row=1, column=0)
        
        self.tab_view19 = Species(master=self.tab("Species Generator [RMG]"), header_name="Species Generator")
        #self.tab_view19.grid(row=0, column=0)
        self.tab_view19.pack(fill='both', expand=True)
        
        self.tab_view20 = Reactions(master=self.tab("Reactions"), header_label="Reactions", species = self.tab_view19)
        self.tab_view20.pack(fill='both', expand=True)


app = App()
app.mainloop()