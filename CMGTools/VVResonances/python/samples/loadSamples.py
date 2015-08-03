import PhysicsTools.HeppyCore.framework.config as cfg
import os

#Load backgrounds from common place
from CMGTools.RootTools.samples.samples_13TeV_74X import QCDPt,WJetsToLNuHT,GJetsHT,TTs,TTJets_50ns,TTJets_LO_50ns,WJetsToLNu_50ns,QCDPt_50ns
background_25ns = QCDPt+WJetsToLNuHT+GJetsHT+TTs
background_50ns = [TTJets_50ns,TTJets_LO_50ns,WJetsToLNu_50ns]+QCDPt_50ns

#Load signal from here 
from CMGTools.VVResonances.samples.signal_13TeV_74X import signalSamples

mcSamples = background_25ns+background_50ns+signalSamples
from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"



#load triggers
from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import triggers_1e,triggers_1mu_iso,triggers_1mu_noniso,triggers_HT,triggers_dijet_fat



#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 1000 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012
    comp.triggers = triggers_1e+triggers_1mu_noniso+triggers_1mu_iso+triggers_HT+triggers_dijet_fat



