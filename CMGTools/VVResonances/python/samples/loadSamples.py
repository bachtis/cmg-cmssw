import PhysicsTools.HeppyCore.framework.config as cfg
import os
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator



def loadMCFromFile(name):
    samples = []
    kreator = ComponentCreator()
    filename = os.environ['CMSSW_BASE']+"/src/CMGTools/VVResonances/data/"+name
    f=open(filename)
    for line in f:
        comp = line.split(',')
        if len(comp) ==1:
            weight=1.0
        elif len(comp) ==2:
            weight=float(comp[1])
        elif len(comp) ==3:
            weight=float(comp[1])*float(comp[2])
        prefix = comp[0].split('/')[1]
        samples.append(kreator.makeMCComponent(prefix,comp[0],"CMS",".root"))
    return samples
   
    



signalSamples = loadMCFromFile('signal_13TeV_Spring15.txt')
bkgSamples = loadMCFromFile('background_13TeV_Spring15.txt')
bkgSamples50ns = loadMCFromFile('background_13TeV_Spring15_50ns.txt')


mcSamples = signalSamples+bkgSamples

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"


#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012



