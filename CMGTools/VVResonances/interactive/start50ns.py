import ROOT

from CMGTools.VVResonances.plotting.TreePlotter import TreePlotter
from CMGTools.VVResonances.plotting.MergedPlotter import MergedPlotter
from CMGTools.VVResonances.plotting.StackPlotter import StackPlotter
 

#create the W+jets plotters
wjPlotters=[]


WJets = TreePlotter('samples/WJetsToLNu_50ns.root','tree')
WJets.setupFromFile('samples/WJetsToLNu_50ns.pck')
WJets.addCorrectionFactor('xsec','xsec',0.0,'lnN')
WJets.addCorrectionFactor('genWeight','genWeight',0.0,'lnN')

WJets.setFillProperties(1001,ROOT.kAzure-9)


qcdPlotters=[]

for sample in [
"QCD_Pt1000to1400_50ns","QCD_Pt120to170_50ns","QCD_Pt1400to1800_50ns","QCD_Pt170to300_50ns","QCD_Pt1800to2400_50ns","QCD_Pt2400to3200_50ns","QCD_Pt300to470_50ns","QCD_Pt3200_50ns","QCD_Pt470to600_50ns","QCD_Pt600to800_50ns","QCD_Pt800to1000_50ns","QCD_Pt80to120_50ns"
    ]:
    qcdPlotters.append(TreePlotter('samples/'+sample+'.root','tree'))
    qcdPlotters[-1].setupFromFile('samples/'+sample+'.pck')
    qcdPlotters[-1].addCorrectionFactor('xsec','xsec',0.0,'lnN')
    qcdPlotters[-1].addCorrectionFactor('genWeight','genWeight',0.0,'lnN')

QCD = MergedPlotter(qcdPlotters)
QCD.setFillProperties(1001,ROOT.kAzure-9)

#QCD.setFillProperties(1001,ROOT.kGreen-5)




dataPlotters=[]
for sample in [
    'SingleElectron_Run2015B','SingleMuon_Run2015B','JetHT_Run2015B'
    ]:
    dataPlotters.append(TreePlotter('samples/'+sample+'.root','tree'))


data = MergedPlotter(dataPlotters)


#WWZ = TreePlotter('samples/WprimeToWZToWhadZhad_narrow_2000.pck','tree')
#WWZ.setupFromFile('samples/WprimeToWZToWhadZhad_narrow_2000.pck')
#WWZ.setFillProperties(0,ROOT.kWhite)
#WWZ.setLineProperties(1,ROOT.kOrange+12,3)


#RSGWWLNuQQ..addCorrectionFactor('xsec',0.001,0.0,'lnN')


#Stack
lnujStack = StackPlotter()
lnujStack.addPlotter(WJets,"W+jets","W+Jets","background")
#vvStack.addPlotter(QCD,"QCD","QCD","background")
#vvStack.addPlotter(RSGWWLNuQQ,"RSG2000","RSGWW #rightarrow l#nu QQ","signal")
lnujStack.addPlotter(data,"data_obs","Data","data")

jjStack = StackPlotter()
#lnujStack.addPlotter(WJets,"W+jets","W+Jets","background")
jjStack.addPlotter(QCD,"QCD","QCD","background")
#vvStack.addPlotter(RSGWWLNuQQ,"RSG2000","RSGWW #rightarrow l#nu QQ","signal")
jjStack.addPlotter(data,"data_obs","Data","data")
