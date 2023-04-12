from src.database_base import DataBase

class ThermoDatabase(DataBase):
    
    def __init__(self, *args, header_name="Thermo Database", **kwargs):
        super().__init__(*args, header_name=header_name, **kwargs)
        
    
    def move_items(self, left_listbox, right_listbox):
        return super().move_items(left_listbox, right_listbox)
    
    def search_database(self, event):
        return super().search_database(event)
    
    def add_database(self, database):
        return super().add_database(database)
    