from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 






ZZType = NTupleObjectType("ZType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("hasFSR",   lambda x : x.hasFSR(), int),
    NTupleVariable("z1_hasFSR",   lambda x : x.leg1.hasFSR(), int),
    NTupleVariable("z2_hasFSR",   lambda x : x.leg2.hasFSR(), int),
    NTupleSubObjectType("z1",  lambda x : x.leg1,fourVectorType),
    NTupleSubObjectType("z2",  lambda x : x.leg2,fourVectorType),
    NTupleSubObjectType("z1_l1",  lambda x : x.leg1.leg1,leptonType),
    NTupleSubObjectType("z1_l2",  lambda x : x.leg1.leg2,leptonType),
    NTupleSubObjectType("z2_l1",  lambda x : x.leg2.leg1,leptonType),
    NTupleSubObjectType("z2_l2",  lambda x : x.leg2.leg2,leptonType)
])



hzz_globalVariables = [
            NTupleVariable("rho",  lambda ev: ev.rho, float, help="kt6PFJets rho"),
            NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"),

]

hzz_globalObjects = {
           "met" : NTupleObject("met", metType)
}


hzz_collections = {
    "bestFourLeptonsSignal"         : NTupleCollection("zz",ZZType, 1, help="Four Lepton Candidates"),    
    "bestFourLeptons2P2F"         : NTupleCollection("zz2P2F",ZZType, 1, help="Four Lepton Candidates 2Pass 2 Fail"),    
    "bestFourLeptons3P1F"         : NTupleCollection("zz3P1F",ZZType, 1, help="Four Lepton Candidates 3 Pass 1 Fail"),   
    "bestFourLeptonsSS"         : NTupleCollection("zzSS",ZZType, 1, help="Four Lepton Candidates SS")   

}


