from states.state import State

class DigState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Dig", "ScanDump")
        self.transitionReady = False

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")
        #always begin with no transition
        self.transitionReady = False

        #thread to track distance on IR 
        #position digger        
        #dig
        #when full or timer limit reached, put away digger
        
        self.transitionReady = True

    #implementation for each state: overridden
    def transition(self):
        return self.transitionReady