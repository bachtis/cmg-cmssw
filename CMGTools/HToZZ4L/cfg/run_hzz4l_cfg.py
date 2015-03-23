##########################################################
##       CONFIGURATION FOR EXO MONOJET TREES            ##
## skim condition:   MET > 200 GeV                      ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.HToZZ4L.analyzers.hzz4lCore_modules_cff import * 


#-------- SAMPLES AND TRIGGERS -----------

#-------- SEQUENCE
from CMGTools.HToZZ4L.samples.samples_13TeV_PHYS14 import *

selectedComponents = []
sequence = cfg.Sequence(hzz4lCoreSequence)


    
test = 1
if test == 1:
    comp = GGHZZ4L_PU40bx25
    comp.files = comp.files[:1]
    comp.files = [ 'sync.root' ]
    comp.splitFactor = 1
    comp.fineSplitFactor = 1
    selectedComponents = [ comp ]



# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


