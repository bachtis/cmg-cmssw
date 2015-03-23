import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.core.all import *
from PhysicsTools.Heppy.analyzers.objects.all import *
from PhysicsTools.Heppy.analyzers.gen.all import *
from CMGTools.HToZZ4L.analyzers.FourLeptonAnalyzer import *
from CMGTools.HToZZ4L.analyzers.FourLeptonAnalyzer2P2F import *
from CMGTools.HToZZ4L.analyzers.FourLeptonAnalyzer3P1F import *
from CMGTools.HToZZ4L.analyzers.FourLeptonAnalyzerSS import *
from CMGTools.HToZZ4L.analyzers.FourLeptonEventSkimmer import *

from CMGTools.HToZZ4L.analyzers.FSRPhotonMaker import *
from CMGTools.HToZZ4L.analyzers.GenFSRAnalyzer import *
from CMGTools.HToZZ4L.analyzers.fourLeptonTree import *

import os


PDFWeights = []

genAna = cfg.Analyzer(
    GeneratorAnalyzer, name="GeneratorAnalyzer",
    # BSM particles that can appear with status <= 2 and should be kept
    stableBSMParticleIds = [ 1000022 ],
    # Particles of which we want to save the pre-FSR momentum (a la status 3).
    # Note that for quarks and gluons the post-FSR doesn't make sense,
    # so those should always be in the list
    savePreFSRParticleIds = [ 1,2,3,4,5, 11,12,13,14,15,16, 21 ],
    # Make also the list of all genParticles, for other analyzers to handle
    makeAllGenParticles = True,
    # Make also the splitted lists
    makeSplittedGenLists = True,
    allGenTaus = False,
    # Print out debug information
    verbose = False,
    )


genFSRAna = cfg.Analyzer(
    GenFSRAnalyzer, name="GenFSRAnalyzer"
    )


# Find the initial events before the skim
skimAnalyzer = cfg.Analyzer(
    SkimAnalyzerCount, name='skimAnalyzerCount',
    useLumiBlocks = False,
    )

# Pick individual events (normally not in the path)
eventSelector = cfg.Analyzer(
    EventSelector,name="EventSelector",
    toSelect = []  # here put the event numbers (actual event numbers from CMSSW)
    )
# Apply json file (if the dataset has one)
jsonAna = cfg.Analyzer(
    JSONAnalyzer, name="JSONAnalyzer",
    )

# Filter using the 'triggers' and 'vetoTriggers' specified in the dataset
triggerAna = cfg.Analyzer(
    TriggerBitFilter, name="TriggerBitFilter",
    )
# Create flags for trigger bits
triggerFlagsAna = cfg.Analyzer(
    TriggerBitAnalyzer, name="TriggerFlags",
    processName = 'HLT',
    triggerBits = {
        # "<name>" : [ 'HLT_<Something>_v*', 'HLT_<SomethingElse>_v*' ] 
    }
    )


# Select a list of good primary vertices (generic)
vertexAna = cfg.Analyzer(
    VertexAnalyzer, name="VertexAnalyzer",
    vertexWeight = None,
    fixedWeight = 1,
    verbose = False
    )


# This analyzer actually does the pile-up reweighting (generic)
pileUpAna = cfg.Analyzer(
    PileUpAnalyzer, name="PileUpAnalyzer",
    true = True,  # use number of true interactions for reweighting
    makeHists=False
    )

pdfwAna = cfg.Analyzer(
    PDFWeightsAnalyzer, name="PDFWeightsAnalyzer",
    PDFWeights = [ pdf for pdf,num in PDFWeights ]
    )



lepAna = cfg.Analyzer(
    LeptonAnalyzer, name="leptonAnalyzer",
    # input collections
    muons='slimmedMuons',
    electrons='slimmedElectrons',
    rhoMuon= 'fixedGridRhoFastjetAll',
    rhoElectron = 'fixedGridRhoFastjetAll',
    # energy scale corrections and ghost muon suppression (off by default)
    doMuScleFitCorrections=False, # "rereco"
    doRochesterCorrections=False,
    doElectronScaleCorrections=False, # "embedded" in 5.18 for regression
    doSegmentBasedMuonCleaning=True,
    # inclusive very loose muon selection
    inclusive_muon_id  = "",
    inclusive_muon_pt  = 5,
    inclusive_muon_eta = 2.4,
    inclusive_muon_dxy = 0.5,
    inclusive_muon_dz  = 1.0,
    # loose muon selection
    loose_muon_id     = "",
    loose_muon_pt     = 5,
    loose_muon_eta    = 2.4,
    loose_muon_dxy    = 0.5,
    loose_muon_dz     = 1,
    loose_muon_isoCut = lambda muon : True,
    # inclusive very loose electron selection
    inclusive_electron_id  = "",
    inclusive_electron_pt  = 7,
    inclusive_electron_eta = 2.5,
    inclusive_electron_dxy = 0.5,
    inclusive_electron_dz  = 1.0,
    inclusive_electron_lostHits = 1.0,
    # loose electron selection
    loose_electron_id     = "",
    loose_electron_pt     = 7,
    loose_electron_eta    = 2.5,
    loose_electron_dxy    = 0.5,
    loose_electron_dz     = 1.0,
    loose_electron_isoCut = lambda x: True,
    loose_electron_lostHits = 1.0,
    # muon isolation correction method (can be "rhoArea" or "deltaBeta")
    mu_isoCorr = "deltaBeta" ,
    mu_effectiveAreas = "Phys14_25ns_v1", #(can be 'Data2012' or 'Phys14_25ns_v1')
    # electron isolation correction method (can be "rhoArea" or "deltaBeta")
    ele_isoCorr = "rhoArea" ,
    el_effectiveAreas = "Phys14_25ns_v1" , #(can be 'Data2012' or 'Phys14_25ns_v1')
    ele_tightId = "Cuts_2012" ,
    # Mini-isolation, with pT dependent cone: will fill in the miniRelIso, miniRelIsoCharged, miniRelIsoNeutral variables of the leptons (see https://indico.cern.ch/event/368826/ )
    doMiniIsolation = False, # off by default since it requires access to all PFCandidates 
    packedCandidates = 'packedPFCandidates',
    miniIsolationPUCorr = 'rhoArea', # Allowed options: 'rhoArea' (EAs for 03 cone scaled by R^2), 'deltaBeta', 'raw' (uncorrected), 'weights' (delta beta weights; not validated)
    miniIsolationVetoLeptons = None, # use 'inclusive' to veto inclusive leptons and their footprint in all isolation cones
    # minimum deltaR between a loose electron and a loose muon (on overlaps, discard the electron)
    min_dr_electron_muon = 100.0,
    # do MC matching 
    do_mc_match = True, # note: it will in any case try it only on MC, not on data
    match_inclusiveLeptons = False, # match to all inclusive leptons
    )


## Jets Analyzer (generic)
jetAna = cfg.Analyzer(
    JetAnalyzer, name='jetAnalyzer',
    jetCol = 'slimmedJets',
    jetPt = 25.,
    jetEta = 4.7,
    jetEtaCentral = 2.4,
    jetLepDR = 0.4,
    jetLepArbitration = (lambda jet,lepton : lepton), # you can decide which to keep in case of overlaps; e.g. if the jet is b-tagged you might want to keep the jet
    minLepPt = 10,
    relaxJetId = False,  
    doPuId = False, # Not commissioned in 7.0.X
    recalibrateJets = "MC", # True, False, 'MC', 'Data'
    mcGT     = "PHYS14_25_V2",
    jecPath = "%s/src/CMGTools/RootTools/data/jec/" % os.environ['CMSSW_BASE'],
    shiftJEC = 0, # set to +1 or -1 to get +/-1 sigma shifts
    smearJets = False,
    shiftJER = 0, # set to +1 or -1 to get +/-1 sigma shifts  
    cleanJetsFromFirstPhoton = False,
    cleanJetsFromTaus = False,
    cleanJetsFromIsoTracks = False,
    doQG = False,
    )


metAna = cfg.Analyzer(
    METAnalyzer, name="metAnalyzer",
    doTkMet = False,
    doMetNoMu = False,
    doMetNoPhoton = False,
    recalibrate = False,
    candidates='packedPFCandidates',
    candidatesTypes='std::vector<pat::PackedCandidate>',
    dzMax = 0.1,
    )



fsrPhotonMaker = cfg.Analyzer(
    FSRPhotonMaker, name="fsrPhotonMaker",
    leptons="selectedLeptons",
    electronID = lambda x: x.mvaIDZZ()
)


fourLeptonAnalyzerSignal = cfg.Analyzer(
    FourLeptonAnalyzer, name="fourLeptonAnalyzerSignal",
    tag = "Signal"
)

fourLeptonAnalyzer2P2F = cfg.Analyzer(
    FourLeptonAnalyzer2P2F, name="fourLeptonAnalyzer2P2F",
    tag = "2P2F"
)

fourLeptonAnalyzer3P1F = cfg.Analyzer(
    FourLeptonAnalyzer3P1F, name="fourLeptonAnalyzer3P1F",
    tag = "3P1F"
)

fourLeptonAnalyzerSS = cfg.Analyzer(
    FourLeptonAnalyzerSS, name="fourLeptonAnalyzerSS",
    tag = "SS"
)

fourLeptonEventSkimmer = cfg.Analyzer(
    FourLeptonEventSkimmer, name="fourLeptonEventSkimmer",
    required = ['bestFourLeptonsSignal','bestFourLeptons2P2F','bestFourLeptons3P1F','bestFourLeptonsSS']

)

treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='fourLeptonTreeProducer',
     vectorTree = False,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     globalVariables = hzz_globalVariables,
     globalObjects = hzz_globalObjects,
     collections = hzz_collections,
     defaultFloatType = 'F',
)




# Core sequence of all common modules
hzz4lCoreSequence = [
    skimAnalyzer,
    genAna,
#    genFSRAna,
   #eventSelector,
    jsonAna,
    triggerAna,
    pileUpAna,
    vertexAna,
    lepAna,
    jetAna,
    metAna,
    triggerFlagsAna,
    fsrPhotonMaker,
    fourLeptonAnalyzerSignal, 
    fourLeptonAnalyzer2P2F,
    fourLeptonAnalyzer3P1F,
    fourLeptonAnalyzerSS,
    fourLeptonEventSkimmer,
    treeProducer
]
