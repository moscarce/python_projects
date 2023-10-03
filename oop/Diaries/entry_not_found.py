class EntryNotFound(Exception):
    def __init__(self):
        super().__init__('Entry not found')