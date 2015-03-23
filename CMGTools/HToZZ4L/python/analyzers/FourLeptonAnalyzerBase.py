from math import *
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi
from PhysicsTools.HeppyCore.framework.event import *

from CMGTools.HToZZ4L.tools.DiObject import DiObject
from CMGTools.HToZZ4L.tools.DiObjectPair import DiObjectPair
from CMGTools.HToZZ4L.tools.OverlapCleaner import OverlapCleaner
from CMGTools.HToZZ4L.tools.CutFlowMaker  import CutFlowMaker

import os
import itertools

class EventBox(object):
    def __init__(self):
        pass

    def __str__(self):

        header = 'EVENT BOX ---> {type} <------ EVENT BOX'.format( type=self.__class__.__name__)
        varlines = []
        for var,value in sorted(vars(self).iteritems()):
            tmp = value
            # check for recursivity
            recursive = False
            if hasattr(value, '__getitem__'):
                if (len(value)>0 and value[0].__class__ == value.__class__):
                    recursive = True
            if isinstance( value, collections.Iterable ) and \
                   not isinstance(value, (str,unicode)) and \
                   not isinstance(value, TChain) and \
                   not recursive :
                tmp = map(str, value)
            varlines.append( '\t{var:<15}:   {value}'.format(var=var, value=tmp) )
        all = [ header ]
        all.extend(varlines)
        return '\n'.join( all )



        
class FourLeptonAnalyzerBase( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(FourLeptonAnalyzerBase,self).__init__(cfg_ana,cfg_comp,looperName)

    def declareHandles(self):
        super(FourLeptonAnalyzerBase, self).declareHandles()

    def beginLoop(self, setup):
        super(FourLeptonAnalyzerBase,self).beginLoop(setup)

    def process(self, event):
        self.readCollections( event.input )



    def leptonID_tight(self,lepton):
        if abs(lepton.sip3D())>4:
            return False
        if abs(lepton.pdgId())==13:
            if not ((lepton.physObj.isGlobalMuon() or lepton.physObj.isTrackerMuon()) and lepton.physObj.isPFMuon()):
                return False

        elif abs(lepton.pdgId())==11:
            if not lepton.mvaIDZZ():
                return False
        return True    


    def leptonID_loose(self,lepton):
        if abs(lepton.sip3D())>4:
            return False
        if abs(lepton.pdgId())==13:
            if lepton.physObj.isTrackerMuon() and not (lepton.physObj.isGlobalMuon()):
                if not (lepton.physObj.numberOfMatchedStations())>0:
                    return False
        return True    


    def leptonID(self,lepton):
        return self.leptonID_tight(lepton)


    def muonIsolation(self,lepton):
        return lepton.absIso(0.5)/lepton.pt()<0.4

    def electronIsolation(self,lepton):
        return lepton.absIsoFromEA("04")/lepton.pt()<0.5

    def diLeptonMass(self,dilepton):
        return dilepton.M()>12.0 and dilepton.M()<120.

    def fourLeptonMassZ1Z2(self,fourLepton):
        return self.diLeptonMass(fourLepton.leg1) and self.diLeptonMass(fourLepton.leg1)

    def fourLeptonMassZ1(self,fourLepton):
        return fourLepton.leg1.M()>40.0

    def stupidCut(self,fourLepton):
        #if not 4mu/4e  pass 
        if abs(fourLepton.leg1.leg1.pdgId())!=abs(fourLepton.leg2.leg1.pdgId()):
            return True

        #find Alternative pairing.Do not forget FSR
        alternate =DiObjectPair(fourLepton.leg1.leg1, fourLepton.leg2.leg2,fourLepton.leg1.leg2,fourLepton.leg2.leg1)
        if (abs(alternate.leg1.M()-91.118)<  abs(fourLepton.leg1.M()-91.118)) and  alternate.leg2.M()<12.:
            return False
        return True




    def fourLeptonPtThresholds(self, fourLepton):
        leading_pt = fourLepton.sortedPtLeg(0).pt() 
        subleading_pt = fourLepton.sortedPtLeg(1).pt() 
        return leading_pt>20  and subleading_pt>10


    def fourLeptonIsolation(self,fourLepton):
        ##First ! attach the FSR photons of this candidate to the leptons!
        



        leptons = fourLepton.daughterLeptons()
        photons = fourLepton.daughterPhotons()

        


        for l in leptons:
            l.fsrPhotons=[]
            for g in photons:
                if deltaR(g.eta(),g.phi(),l.eta(),l.phi())<0.4:
                    l.fsrPhotons.append(g)
            if abs(l.pdgId())==11:
                if not self.electronIsolation(l):
                    return False
            if abs(l.pdgId())==13:
                if not self.muonIsolation(l):
                    return False
        return True        

    def ghostSuppression(self, fourLepton):
        leptons = fourLepton.daughterLeptons()
        for l1,l2 in itertools.combinations(leptons,2):
            if deltaR(l1.eta(),l1.phi(),l2.eta(),l2.phi())<0.02:
                return False
        return True    



    def qcdSuppression(self, fourLepton):
        return fourLepton.minOSPairMass()>4.0

        

    def findOSSFQuads(self, leptons,photons):
        '''Make combinatorics and make permulations of four leptons
           Cut the permutations by asking Z1 nearest to Z and also 
           that plus is the first
           Include FSR if in cfg file
        '''
        out = []
        for l1, l2,l3,l4 in itertools.permutations(leptons, 4):
            if (l1.pdgId()+l2.pdgId())!=0: 
                continue;
            if (l3.pdgId()+l4.pdgId())!=0:
                continue;
            if (l1.pdgId()<l2.pdgId())!=0: 
                continue;
            if (l3.pdgId()<l4.pdgId())!=0: 
                continue;

            quadObject =DiObjectPair(l1, l2,l3,l4)
            self.attachFSR(quadObject,photons)
            if abs(quadObject.leg1.M()-91.118)>abs(quadObject.leg2.M()-91.118):
                continue;
            out.append(quadObject)

        return out



    def attachFSR(self,quad,photons):
        #first attach photons to the closest leptons
        attachData={}
        
        legs=[quad.leg1.leg1,quad.leg1.leg2,quad.leg2.leg1,quad.leg2.leg2]

        assocPhotons=[]
        for g in photons:
            for l in legs:
                DR=deltaR(l.eta(),l.phi(),g.eta(),g.phi())
                if DR>0.5:
                    continue;
                
                if hasattr(g,'DR'):
                    if DR<g.DR:
                        g.DR=DR
                        g.nearestLepton = l
                else:        
                    g.DR=DR
                    g.nearestLepton = l
                assocPhotons.append(g)

        
        #Now we have the association . Check criteria
        #First on Z1
        z1Photons=[]
        z2Photons=[]

        z1Above4=False
        z2Above4=False
        for g in assocPhotons:
            if g.nearestLepton in [quad.leg1.leg1,quad.leg1.leg2]:
                mll = quad.leg1.M()
                mllg = (quad.leg1.leg1.p4()+quad.leg1.leg2.p4()+g.p4()).M()
                if mllg<4 or mllg>100:
                    continue
                if abs(mllg-91.188)>abs(mll-91.188):
                    continue
                z1Photons.append(g)
                if g.pt()>4:
                    z1Above4 = True

            if g.nearestLepton in [quad.leg2.leg1,quad.leg2.leg2]:
                mll = quad.leg2.M()
                mllg = (quad.leg2.leg1.p4()+quad.leg2.leg2.p4()+g.p4()).M()
                if mllg<4 or mllg>100:
                    continue
                if abs(mllg-91.188)>abs(mll-91.188):
                    continue
                z2Photons.append(g)
                if g.pt()>4:
                    z2Above4 = True
                
            

        if len(z1Photons)>0:
            if z1Above4: #Take the highest pt
                fsr = max(z1Photons,key=lambda x: x.pt())
                quad.leg1.setFSR(fsr)
            else:    #Take the smallest DR
                fsr = min(z1Photons,key=lambda x: x.DR)
                quad.leg1.setFSR(fsr)
        if len(z2Photons)>0:
            if z2Above4: #Take the highest pt
                fsr = max(z2Photons,key=lambda x: x.pt())
                quad.leg2.setFSR(fsr)
            else:    #Take the smallest DR
                fsr = min(z2Photons,key=lambda x: x.DR)
                quad.leg2.setFSR(fsr)

        quad.updateP4()        
        #cleanup for next combination!        
        for g in assocPhotons:
            del g.DR
            del g.nearestLepton
            
                


