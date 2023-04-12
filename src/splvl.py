from src.levels_base import Levels

class SPLevel(Levels):
    
    def __init__(self, *args, header_name='SP Level', **kwargs):
        super().__init__(*args, header_name=header_name, **kwargs)
        
    def store_values(self):
        return super().store_values()