def zones():
    zone = {
        'NORTH CENTRAL':['BENUE','FCT','KOGI','KWARA','NASARAWA','NIGER','PLATEAU'],
        'NORTH EAST':['ADAMAWA','BAUCHI','BORNO','GOMBE','TARABA','YOBE'],
        'NORTH WEST':['KADUNA','KATSINA','KANO','KEBBI','SOKOTO','JIGAWA','ZAMFARA'],
        'SOUTH EAST':['ABIA','ANAMBRA','EBONYI','ENUGU','IMO'],
        'SOUTH SOUTH':['AKWA IBOM','BAYELSA','CROSS RIVER','DELTA','EDO','RIVERS'],
        'SOUTH WEST':['EKITI','LAGOS','OSUN','ONDO','OGUN','OYO']
    }
    return zone


def collect_state():
    state = input('Enter state: ')
    return state.upper()

def check_state():
    zone = zones()
    state = collect_state()
    for keys in zone:
        for values in zone[keys]:
            if state == values:
                return keys
    return 'State not found'



print(check_state())
