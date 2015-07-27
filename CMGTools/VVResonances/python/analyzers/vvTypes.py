from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 



LNuType = NTupleObjectType("LNuType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("mt",   lambda x : x.mt(), float),       
    NTupleVariable("deltaPhi",   lambda x : x.deltaPhi(), float),       
])


LLType = NTupleObjectType("LLType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("mt",   lambda x : x.mt(), float),       
    NTupleVariable("deltaPhi",   lambda x : x.deltaPhi(), float),       
    NTupleVariable("deltaR",   lambda x : x.deltaR(), float),       
])



JetType = NTupleObjectType("SubJetType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("area",   lambda x : x.jetArea(), float),       
    NTupleVariable("nConstituents",   lambda x : len(x.constituents), int)           
])


FatJetType = NTupleObjectType("FatJetType", baseObjectTypes=[JetType], variables = [
    NTupleVariable("softDropMass",   lambda x : x.softDropJet.mass(), float),       
    NTupleVariable("tau1",   lambda x : x.Ntau[0], float),       
    NTupleVariable("tau2",   lambda x : x.Ntau[1], float),       
    NTupleVariable("tau3",   lambda x : x.Ntau[2], float),       
    NTupleVariable("tau4",   lambda x : x.Ntau[3], float),       
    NTupleVariable("massDropMu",   lambda x : x.massDrop[0], float),       
    NTupleVariable("massDropY",   lambda x : x.massDrop[1], float),       
])

LNuJJType = NTupleObjectType("LNuJJType", baseObjectTypes=[], variables = [
    NTupleSubObject("LV",  lambda x : x['pair'],fourVectorType),
    NTupleSubObject("altLV",  lambda x : x['pair'].leg1.alternateLV+x['pair'].leg2.p4(),fourVectorType),
    NTupleSubObject("rawLV",  lambda x : x['pair'].leg1.rawP4()+x['pair'].leg2.p4(),fourVectorType),
    NTupleVariable("deltaPhi",   lambda x : x['pair'].deltaPhi(), float),       
    NTupleVariable("deltaR",   lambda x : x['pair'].deltaR(), float),       
    NTupleVariable("nJets",   lambda x : len(x['satelliteJets']), int),
    NTupleVariable("DEtaJJ",   lambda x : x['vbfDEta'], float),
    NTupleVariable("MJJ",   lambda x : x['vbfMJJ'], float),
    NTupleSubObject("l1",  lambda x : x['pair'].leg1,LNuType),
    NTupleSubObject("altl1",  lambda x : x['pair'].leg1.alternateLV,fourVectorType),
    NTupleSubObject("l1_l",  lambda x : x['pair'].leg1.leg1,leptonTypeExtra),
    NTupleSubObject("l1_met",  lambda x : x['pair'].leg1.leg2,metType),
    NTupleSubObject("l2",  lambda x : x['pair'].leg2,FatJetType),
    NTupleSubObject("l2_softDrop",  lambda x : x['pair'].leg2.softDropJet,JetType),
    NTupleSubObject("l2_s1",  lambda x : x['pair'].leg2.subjets[0],JetType),
    NTupleVariable("l2_s1_matched",   lambda x : x['pair'].leg2.subjets[0].matched, int),       

    NTupleSubObject("l2_s2",  lambda x : x['pair'].leg2.subjets[1],JetType),          
    NTupleVariable("l2_s2_matched",   lambda x : x['pair'].leg2.subjets[1].matched, int),       


])


LLJJType = NTupleObjectType("LLJJType", baseObjectTypes=[], variables = [
    NTupleSubObject("LV",  lambda x : x['pair'],fourVectorType),
    NTupleVariable("deltaPhi",   lambda x : x['pair'].deltaPhi(), float),       
    NTupleVariable("deltaR",   lambda x : x['pair'].deltaR(), float),       
    NTupleVariable("nJets",   lambda x : len(x['satelliteJets']), int),
    NTupleVariable("DEtaJJ",   lambda x : x['vbfDEta'], float),
    NTupleVariable("MJJ",   lambda x : x['vbfMJJ'], float),
    NTupleSubObject("l1",  lambda x : x['pair'].leg1,LLType),
    NTupleSubObject("l1_l1",  lambda x : x['pair'].leg1.leg1,leptonTypeExtra),
    NTupleSubObject("l1_l2",  lambda x : x['pair'].leg1.leg2,leptonTypeExtra),
    NTupleSubObject("l2",  lambda x : x['pair'].leg2,FatJetType),
    NTupleSubObject("l2_softDrop",  lambda x : x['pair'].leg2.softDropJet,JetType),
    NTupleSubObject("l2_s1",  lambda x : x['pair'].leg2.subjets[0],JetType),
    NTupleVariable("l2_s1_matched",   lambda x : x['pair'].leg2.subjets[0].matched, int),       
    NTupleSubObject("l2_s2",  lambda x : x['pair'].leg2.subjets[1],JetType),          
    NTupleVariable("l2_s2_matched",   lambda x : x['pair'].leg2.subjets[1].matched, int),       
])



JJType = NTupleObjectType("JJType", baseObjectTypes=[], variables = [
    NTupleSubObject("LV",  lambda x : x['pair'],fourVectorType),
    NTupleVariable("deltaPhi",   lambda x : x['pair'].deltaPhi(), float),       
    NTupleVariable("deltaR",   lambda x : x['pair'].deltaR(), float),       
    NTupleVariable("nJets",   lambda x : len(x['satelliteJets']), int),
    NTupleVariable("DEtaJJ",   lambda x : x['vbfDEta'], float),
    NTupleVariable("MJJ",   lambda x : x['vbfMJJ'], float),

    NTupleSubObject("l1",  lambda x : x['pair'].leg1,FatJetType),
    NTupleSubObject("l1_softDrop",  lambda x : x['pair'].leg1.softDropJet,JetType),
    NTupleSubObject("l1_s1",  lambda x : x['pair'].leg1.subjets[0],JetType),
    NTupleVariable("l1_s1_matched",   lambda x : x['pair'].leg1.subjets[0].matched, int),       
    NTupleSubObject("l1_s2",  lambda x : x['pair'].leg1.subjets[1],JetType),          
    NTupleVariable("l1_s2_matched",   lambda x : x['pair'].leg1.subjets[1].matched, int),       

    NTupleSubObject("l2",  lambda x : x['pair'].leg2,FatJetType),
    NTupleSubObject("l2_softDrop",  lambda x : x['pair'].leg2.softDropJet,JetType),
    NTupleSubObject("l2_s1",  lambda x : x['pair'].leg2.subjets[0],JetType),
    NTupleVariable("l2_s1_matched",   lambda x : x['pair'].leg2.subjets[0].matched, int),       
    NTupleSubObject("l2_s2",  lambda x : x['pair'].leg2.subjets[1],JetType),          
    NTupleVariable("l2_s2_matched",   lambda x : x['pair'].leg2.subjets[1].matched, int),       


])


