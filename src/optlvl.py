from src.levels_base import Levels

class OptLevel(Levels):
    
    def __init__(self, *args, header_name='Conformer Level', **kwargs):
        super().__init__(*args, header_name=header_name, **kwargs)
        
    def store_values(self):
        return super().store_values()