# import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# PLOTTING SETTINGS - BLACK
pink = (250/255, 215/255, 225/255)
theme = "black" # pink for no 

colors = [ theme, "xkcd:pink red", "xkcd:blue" ]
markers = ["*", "^", "o"]
strokes = ['-', ':', "--"]

plt.rcParams['axes.prop_cycle'] = plt.cycler(color = colors) + plt.cycler(marker = markers) +  plt.cycler(linestyle = strokes)
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['errorbar.capsize'] = 2
plt.rcParams["font.family"] = "Times"
plt.rcParams["legend.frameon"] = False
plt.rcParams["text.color"] = theme
plt.rcParams["axes.facecolor"] = (0, 0, 0, 0)
plt.rcParams["axes.edgecolor"] = theme
plt.rcParams["axes.labelcolor"] = theme
plt.rcParams["xtick.color"] = theme
plt.rcParams["ytick.color"] = theme
plt.rcParams["xtick.major.width"] = 0.6
plt.rcParams["ytick.major.width"] = 0.6
plt.rcParams["axes.linewidth"] = 0.6

# %% ACTUAL WORK



State = np.array( [0, # SynthE 1
                   1, # SynthT 2
                   0, # Hold 3
                   0, # BloodE 4
                   0, # BloodT 5
                   0, # BloodP 6
                   0, # BrainE 7
                   0, # BrainT 8
                   0, # BrainP 9
                   1, # PulseGnRH 10
                   1, # AromataseActivity 11
                   0, # Excitation 12
                   0, # Time
                   ])



# GnRH upregualtes E sythasis see "Control of aromatase in hippocampal neurons"
# additionally, presence of E decreases aromatase activity

                         # thing being impacted                  
Multiplier = np.array( [[1, 0,   1, 100,   0, 0,   0,   0, 0, 0, 0, 0, 0], # SynthE 1
                        [0, 1,   0,   0, 100, 1,   0,   0, 0, 0, 0, 0, 0], # SynthT 2
                        [0, 0,   1,   0,   0, 0,   0,   0, 0, 0, 0, 0, 0], # HoldE 3
                        [0, 0,   0,   0,   0, 0, 0.8,   0, 0, 0, 0, 0, 0], # BloodE 4
                        [0, 0,   0,   0,   0, 0,   0, 0.8, 0, 0, 0, 0, 0], # BloodT 5
                        [0, 0,   0,   0,   0, 1,   0,   0, 0, 0, 0, 0, 0], # HoldT 6
                        [0, 0,   0,   0,   0, 0,   0,   0, 0, 0, 0, 0, 0], # BrainE 7
                        [0, 0,   0,   0,   0, 0,   0,   0, 0, 0, 0, 0, 0], # BrainT 8
                        [0, 0,   0,   0,   0, 0,   0,   0, 0, 0, 0, 0, 0], # BrainP 9
                        [0, 0,   1,  30,  30, 1,   0,   0, 0, 1, 0, 0, 0], # PulseGnRH 10
                        [0, 0,   0,   0,   0, 0,   2,  -2, 0, 0, 1, 0, 0], # AromataseActivity 11
                        [0, 0,   0,   0,   0, 0,   0,   0, 0, 0, 0, 0, 0], # Excitation 12
                        [0, 0,   0,   0,   0, 0,   0,   0, 0, 0, 0, 0, 1], # Time
                        ])


Adder = np.array( [0, # SynthE 1
                   0, # SynthT 2
                   -1, # HoldE 3
                   -100, # BloodE 4
                   -100, # BloodT 5
                   -1, # HoldT 6
                   0, # BrainE 7
                   0, # BrainT 8
                   0, # BrainP 9
                   0, # PulseGnRH 10
                   0, # AromataseActivity 11
                   0, # Excitation 12
                   1, # Time
                   ])

History = State

for i in range(15):

    State = np.matmul( State, Multiplier, )
    State = np.add( State, Adder)
    State[State<0] = 0
    
    History = np.vstack( (History, State) )
np.set_printoptions(threshold=np.inf)
print( History )





