from constants import constants

class SMTKeyboard:
    def __init__(self,device):
        self.device = device
        self.mode = None
        self.kbd = device
        self.current = {}

    def set_mode(self,mode=None):
        if not mode or mode not in constants.modes:
            mode = 'normal'
        commit =[0xFF]*8
        commit[0] = 1;
        commit[1] = 2;
        commit[2] = 65; # commit
        commit[3] = constants.modes[mode]; # set hardware mode
        commit[4] = 0;
        commit[5] = 0;
        commit[6] = 0;
        commit[7] = 236; # EOR
        self.kbd.send_feature_report(commit)
        self.mode = mode

    def set_color(self,region,color,intensity):
        if not region or not color:
            raise Exception("missing region/color")
        if not intensity:
            intensity="high";
        activate = [0xFF]*8
        activate[0] = 1;
        activate[1] = 2;
        activate[2] = 66; # set
        activate[3] = constants.regions[region];
        activate[4] = constants.colors[color];
        activate[5] = constants.levels[intensity];
        activate[6] = 0;
        activate[7] = 236;  # EOR (end of request)
        self.kbd.send_feature_report(activate)
        self.set_mode(self.mode)
        self.current[region] = {
            "intensity":intensity,
            "color":color
        }
