'''
    Utility functions for Text Adventure Game Engine
''' 
import os


def transfer_item(item, fromObj, toObj):

    try:
        fromObj.has_inventory()
    except:
        raise TypeError("fromObj has no Inventory")
    
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
