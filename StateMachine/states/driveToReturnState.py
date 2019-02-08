from .state import State


class DriveToReturn(State):
    # init attributes of state
    def __init__(self):
        super().__init__("DriveToReturn", "Dump")
        self.transitionReady = False

    # implementation for each state: overridden
    def run(self, moveInstructions):
        print("\n>run() not implemented\n")

        # always begin with no transition
        self.transitionReady = False

        #store initial beacon angle
        #rotate until beacon angle=initialBeaconAngle+180

        #go forward until:
            #the "distance" between the middle and back beacon=the distance between the middle and front beacon
        #rotate until beacon is directly behind robot
        #back up until distance between camera and beacon is small enough


        
        # check if beacon is on left or right side within bounds
        #
        # cannot see side beacon
        # main beacon must be specified size.
        # needs to be procedure to "parallel park" and try again if criteria not met
        # ^^ perhaps make the above the dock state

        self.transitionReady = True

    # implementation for each state: overridden
    def transition(self):
        return self.transitionReady
