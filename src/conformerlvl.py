import customtkinter
from src.levels_base import Levels
from typing import Optional, Union, Tuple

class ConformerLevel(Levels):
    
    def __init__(self,*args, header_name, **kwargs):
        super().__init__(**kwargs)
        
    def store_values(self):
        return super().store_values()