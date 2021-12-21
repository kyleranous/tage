'''
    Utility functions for Text Adventure Game Engine
''' 
import os


def transfer_item(item, fromObj, toObj):

    try:
        fromObj.has_inventory()
    except:

        raise RuntimeError("fromObj has no Inventory")
    
    # Check that item exists in fromObj
    if fromObj.check_item(item):
        # Check to see if toObj has an Inventory
        if toObj.has_inventory():
            # Transfer Object between inventories
            transArr = fromObj.remove_item(item)
            toObj.add_item(transArr[0], transArr[1])
        else:
            raise RuntimeError("toObj has no Inventory")
    else:
        raise RuntimeError(f"Item {item} Does not exist in fromObj Inventory")
    


def clear_console():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


######################################################

class StateMachine:
    
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise RuntimeError("must call .set_start() before .run()")
        
        if not self.endStates:
            raise RuntimeError("at least one state must be an end_state")

        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                # print("reached ", newState)
                # return payload
                return newState
            else:
                handler = self.handlers[newState.upper()]