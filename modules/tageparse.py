from tageutils import StateMachine
# Responses
YES_LIST = ('yes', 'yeah', 'ready', 'set', 'ok')
NO_LIST = ('no', 'nah', 'nope')

# Actions
INSPECT_LIST = ('inspect', 'look', 'check')
MOVE_LIST = ('move', 'go', 'walk', 'run')
ACTION_LIST = ('attack', 'kill')

# Directions
DIRECTION_LIST = ('north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'forward',
                  'back')

# Locations
LOCATION_LIST = ('in', 'out', 'inside', 'outside')

# Inverse Adverbs
INVERSE_LIST = ('not')

# inverse

# Test
positive_adj = ["great", "super", "fun", "entertaining", "easy"]
negative_adj = ["boring", "difficult", "ugly", "bad"]

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
        self.set_start("Start")

    def parse_text(self,txt):
        self.action = ""
        self.dobj = ""
        self.iobj = ""
        newState = self.run(txt)
        if newState.upper() == "PARSED_STATE":
            return [self.action, self.dobj, self.iobj]
        elif newState.upper() == "ERROR_STATE":
            return ["ERROR"]

    def start_transition(self, txt):
        split_txt = txt.split(None,1)
        word, txt = split_txt if len(split_txt) > 1 else (txt, "")
        
        if word.lower() == 'i' or word.lower() == "am":
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
        elif word.lower() in INVERSE_LIST:
            newState = "inversed_state"
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



t = TextParser() 
testStrings = ["Move North", "I Move to the north", "run east", "walk to south", "go back", "I go west", "I am ready", "I am not Ready", "ready", "not ready"]   
for test in testStrings:
    print(t.parse_text(test))

