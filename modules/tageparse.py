from modules.tageutils import StateMachine


# Responses
YES_LIST = ('yes', 'yeah', 'ready', 'set', 'ok')
NO_LIST = ('no', 'nah', 'nope')

# Actions
INSPECT_LIST = ('inspect', 'look', 'check')
MOVE_LIST = ('move', 'go', 'walk', 'run')
MANIPULATE_LIST = ('pick', 'drop', 'put', 'store', 'take')
ATTACK_LIST = ('attack', 'kill')

# Directions
DIRECTION_LIST = ('north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'forward',
                  'back')

# Locations
LOCATION_LIST = ('in', 'out', 'inside', 'outside')

# Inverse Adverbs
INVERSE_LIST = ('not')

# Loop Lists
START_LOOP_LIST = ('i', 'am', 'want', 'to', 'we', )


class TextParser(StateMachine):

    def __init__(self):
        StateMachine.__init__(self)
        self.action = ""
        self.dobj = ""
        self.iobj = ""
        self.add_state("Start", self.start_transition)
        self.add_state("parsed_state", None, end_state=1)
        self.add_state("error_state", None, end_state=1)
        self.add_state("moving_state", self.moving_state_transition)
        self.add_state("inversed_state", self.inversed_state_transition)
        self.add_state("inspection_state", self.inspection_state_transition)
        self.add_state("take_item_state", self.take_item_state_transition)
        self.add_state("drop_item_state", self.drop_item_state_transition)
        self.add_state("put_item_state", self.put_item_state_transition)
        self.add_state("stow_item_state", self.stow_item_state_transition)
        self.set_start("Start")

    def parse_text(self,txt):
        self.action = ""
        self.dobj = ""
        self.iobj = ""
        newState = self.run(txt)
        if newState.upper() == "PARSED_STATE":
            return [self.action.rstrip(), self.dobj.rstrip(), self.iobj.rstrip()]
        elif newState.upper() == "ERROR_STATE":
            return ["ERROR"]

    def start_transition(self, txt):
        split_txt = txt.split(None,1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")
        
        word = word.replace(',', '')

        if word.lower() in START_LOOP_LIST:
            newState = "start"
        elif word.lower() in YES_LIST:
            self.action = "YES"
            newState = "parsed_state"
        elif word.lower() in NO_LIST:
            self.action = "NO"
            newState = "parsed_state"
        elif word.lower() in MOVE_LIST:
            self.action = "MOVE"
            newState = "moving_state"
        elif word.lower() in INSPECT_LIST:
            self.action = "INSPECT"
            newState = "inspection_state"
        elif word.lower() in INVERSE_LIST:
            newState = "inversed_state"
        elif word.lower() in MANIPULATE_LIST:
            if word.lower() == "pick" or word.lower() == "take":
                newState = "take_item_state"
            elif word.lower() == "drop":
                newState = "drop_item_state"
            elif word.lower() == "put":
                newState = "put_item_state"
            elif word.lower() == "store":
                newState = "stow_item_state"
        else:
            newState = "error_state"
    
        return (newState, txt)

    def inversed_state_transition(self, txt):
        split_txt = txt.split(None, 1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")

        if word.lower() in YES_LIST:
            self.action = "NO"
            newState = "parsed_state"
        else:
            self.action = "ERROR"
        
        return (newState, txt)

    def moving_state_transition(self, txt):
        split_txt = txt.split(None, 1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")

        if word.lower() in DIRECTION_LIST:
            self.dobj = word.upper()
            newState = "parsed_state"
        elif word.lower() == "to" or word.lower() == 'the':
            newState = "moving_state"
        else:
            newState = "error_state"
        
        return (newState, txt)
    
    def inspection_state_transition(self, txt):
        split_txt = txt.split(None, 1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")

        if word.lower() == "at" or word.lower() == "the":
            newState = "inspection_state"
        elif word.lower() in LOCATION_LIST:
            self.iobj = word.upper()
            newState = "inspection_state"
        else:
            objString = word + " " + txt
            self.dobj = objString.upper()
            newState = "parsed_state"
        
        return (newState, txt)

    def take_item_state_transition(self, txt):
        split_txt = txt.split(None, 1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")
        self.action = "TAKE"
        if word.lower() == "up":
            newState = "take_item_state"
        else:
            objStr = word + " " + txt
            self.dobj = objStr.upper()
            newState = "parsed_state"
        
        return (newState, txt)
    
    def drop_item_state_transition(self, txt):
        split_txt = txt.split(None, 1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")

        self.action = "DROP"
        objStr = word + " " + txt
        self.dobj = objStr.upper()
        newState = "parsed_state"

        return (newState, txt)
    
    def put_item_state_transition(self, txt):
        split_txt = txt.split(None, 1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")

        if word.lower() == "down":
            newState = "drop_item_state"
        elif word.lower() == "away":
            newState = "stow_item_state"
        else:
            newState = "error_state"
        
        return (newState, txt)

    def stow_item_state_transition(self, txt):
        split_txt = txt.split(None, 1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")

        self.action = "STOW"
        objStr = word + " " + txt
        self.dobj = objStr.upper()
        newState = "parsed_state"

        return (newState, txt)
