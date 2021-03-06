#include "../includes/common.h"
// #include "../AnalysisCode/common_stuff.C"
// #include "../AnalysisCode/common_stuff.h"

using namespace std;

void PlotWdistributionsMCvsDATA_stack(TString folderMCsig="",TString folderMCEWK="",TString folderMCTT="",TString folderMCQCD="",TString folderDATA=""){

  gStyle->SetOptTitle(0);
  gStyle->SetOptStat(0);
  
  
  cout << "PlotWdistributionsMCvsDATA_stack.C working dir: " << gSystem->WorkingDirectory() << endl;

  TFile *fMCsig=new TFile(Form("%s/WanalysisOnDATA.root",folderMCsig.Data()));
  TFile *fMCEWK=new TFile(Form("%s/WanalysisOnDATA.root",folderMCEWK.Data()));
  TFile *fMCTT=new TFile(Form("%s/WanalysisOnDATA.root",folderMCTT.Data()));
  TFile *fMCQCD=new TFile(Form("%s/WanalysisOnDATA.root",folderMCQCD.Data()));
  TFile *fDATA=new TFile(Form("%s/WanalysisOnDATA.root",folderDATA.Data()));
  
  fMCsig->Print();
  // fMCsig->ls();
  fMCEWK->Print();
  fMCTT->Print();
  fDATA->Print();

  
  TString MuCharge_str[2] = {"Pos" ,"Neg"};
  
  
  for(int c=0; c<2; c++){
  
    TString LegendEvTypeTeX=Form("W%s#rightarrow#mu#nu",MuCharge_str[c].Data());
    
    for(int i=0; i<WMass::etaMuonNSteps; i++){
      TString eta_str = Form("%.1f",WMass::etaMaxMuons[i]); eta_str.ReplaceAll(".","p");
      // for(int j=0; j<2*WMass::WMassNSteps+1; j++){
      for(int j=WMass::WMassNSteps; j<WMass::WMassNSteps+1; j++){
        int jWmass = WMass::WMassCentral_MeV-(WMass::WMassNSteps-j)*WMass::WMassStep_MeV;
        
        for(int k=0;k<3;k++){
          plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hW%s_%sNonScaled_SelRange_8_JetCut_pdf%d-%d%s_eta%s_%d",MuCharge_str[c].Data(),WMass::FitVar_str[k].Data(),WMass::PDF_sets,0,"",eta_str.Data(),jWmass),0,0,0,1,Form(";%s [GeV];Counts",WMass::FitVar_str[k].Data()),-1,-1,1,1);
          plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hW%s_%sNonScaled_8_JetCut_pdf%d-%d%s_eta%s_%d",MuCharge_str[c].Data(),WMass::FitVar_str[k].Data(),WMass::PDF_sets,0,"",eta_str.Data(),jWmass),0,0,0,1,Form(";%s [GeV];Counts",WMass::FitVar_str[k].Data()),-1,-1,1,1);
        }
        
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWPos_METNonScaled_8_JetCut_pdf10042-0_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";MET [GeV];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnvtx_Sig_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";number of vertices;Counts",0,50,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnvtx_noWeights",eta_str.Data(),jWmass),0,0,0,1,";number of vertices;Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnvtx_1_TrgAndGoodVtx",eta_str.Data(),jWmass),0,0,0,1,";number of vertices;Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnvtx_5_RecoCut",eta_str.Data(),jWmass),0,0,0,1,";number of vertices;Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnvtx_6_METCut",eta_str.Data(),jWmass),0,0,0,1,";number of vertices;Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnvtx_7_RecoilCut",eta_str.Data(),jWmass),0,0,0,1,";number of vertices;Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWPos_pt_Sig_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";number of vertices;Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnoTrgMuonsLeadingPt_Sig_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";Z mass [GeV];Counts",50,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hpfMET_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";MET [GeV];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hpfMETphi_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";MET #phi [rad];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWPos_pt_unzoomed_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";W p_{T} [GeV];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWPos_pt_unzoomed_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";W p_{T} [GeV];Counts",-1,100,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWPos_pt_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";W p_{T} [GeV];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWPos_phi_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";W #phi [rad];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWPos_mt_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";W m_{T} [GeV];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWPos_mt_QCD_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";W m_{T} QCD [GeV];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hMupt_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";#mu p_{T} [GeV];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hMueta_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";#mu #eta;Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hMuphi_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";#mu #phi [rad];Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hMulogiso_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";log rel iso;Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hJetpt_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";u1 (GeV);Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hJeteta_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";u2 (GeV);Counts",-1,-1,1);
        // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hJetphi_WPos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";u2 (GeV);Counts",-1,-1,1);

      }

    }
    
    
  }
}

///////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////

void plotAndSaveHisto1D(TFile*f1, TString str1, TFile*f2, TString str2, int logx, int logy, int logz, int scaleMCtoDATA){

  TH1D*h1=(TH1D*)f1->Get(str1.Data());
  h1->SetLineColor(2);
  TH1D*h2=(TH1D*)f2->Get(str2.Data());
  
  TCanvas *c1 = new TCanvas("c"+str1);
  c1->SetLogx(logx);
  c1->SetLogy(logy);
  c1->SetLogz(logz);
  
  if(scaleMCtoDATA){
    h1->DrawNormalized();
    h2->DrawNormalized("same");
  }else{
    h1->Draw();
    h2->Draw("same");    
  }
  
  c1->SaveAs(str1+".png");
  
}


void plotAndSaveHisto1D_stack(TString LegendEvTypeTeX, TFile*fMCsig, TFile*fMCEWK, TFile*fMCTT, TFile*fMCQCD, TFile*fDATA, TString HistoName_st, int logx, int logy, int logz, int scaleMCtoDATA, TString title,double xmin, double xmax, int rebinfactor, int PullOrRatio=0){

  std::cout << "retrieving hMCsig= " << HistoName_st.Data() << std::endl;
  TH1D*hMCsig=(TH1D*)fMCsig->Get(HistoName_st.Data());
  fMCsig->Print();
  hMCsig->Rebin(rebinfactor);
  // std::cout << "hMCsig= " << hMCsig->Print() << std::endl;
  hMCsig->SetLineColor(kOrange-3);
  TH1D*hMCsig2=(TH1D*)hMCsig->Clone("hMCsig2");
  hMCsig->SetFillColor(kOrange-2);
  hMCsig2->SetLineStyle(2);
  hMCsig2->SetLineWidth(2);
  TH1D*hMCEWK=(TH1D*)fMCEWK->Get(HistoName_st.Data());
  // std::cout << "hMCEWK= " << hMCEWK->Print() << std::endl;
  hMCEWK->SetFillColor(kOrange+7);
  hMCEWK->SetLineColor(kOrange+10);
  hMCEWK->Rebin(rebinfactor);
  TH1D*hMCTT=(TH1D*)fMCTT->Get(HistoName_st.Data());
  // std::cout << "hMCTT= " << hMCTT->Print() << std::endl;
  hMCTT->SetFillColor(kGreen);
  hMCTT->SetLineColor(kGreen+2);
  hMCTT->Rebin(rebinfactor);
  TH1D*hMCQCD=(TH1D*)fMCQCD->Get(HistoName_st.Data());
  // std::cout << "hMCQCD= " << hMCQCD->Print() << std::endl;
  hMCQCD->SetFillColor(kViolet-5);
  hMCQCD->SetLineColor(kViolet+2);
  hMCQCD->Rebin(rebinfactor);
  TH1D*hDATA=(TH1D*)fDATA->Get(HistoName_st.Data());
  hDATA->SetMarkerColor(1);
  hDATA->SetLineColor(1);
  hDATA->SetMarkerStyle(20);
  hDATA->SetMarkerSize(0.7);
  hDATA->Rebin(rebinfactor);

  TH1D MCsum=(*hMCsig)+(*hMCEWK)+(*hMCTT)+(*hMCQCD);
  
  std::cout << "Total DATA/MC scaling factor = " << hDATA->Integral()/MCsum.Integral() << std::endl;
  if(scaleMCtoDATA){
    hMCsig2->Scale(hDATA->Integral()/MCsum.Integral());
    hMCsig->Scale(hDATA->Integral()/MCsum.Integral());
    hMCEWK->Scale(hDATA->Integral()/MCsum.Integral());
    hMCTT->Scale(hDATA->Integral()/MCsum.Integral());
    hMCQCD->Scale(hDATA->Integral()/MCsum.Integral());
    MCsum.Scale(hDATA->Integral()/MCsum.Integral());
  }
  
  double fsig = hMCsig->Integral()/MCsum.Integral()*100;
  double fewk = hMCEWK->Integral()/MCsum.Integral()*100;
  double ftt = hMCTT->Integral()/MCsum.Integral()*100;
  double fqcd = hMCQCD->Integral()/MCsum.Integral()*100;

  THStack *hs= new THStack("hs","test stacked histograms");
  hs->Add(hMCTT);
  hs->Add(hMCQCD);
  hs->Add(hMCEWK);
  hs->Add(hMCsig);

  std::cout << "Integral hDATA= " << hDATA->Integral() << " hMCsig= " << hMCsig->Integral() << " hMCEWK= " << hMCEWK->Integral() << " hMCTT= " << hMCTT->Integral() << " hMCQCD= " << hMCQCD->Integral() << " MCsum= " << MCsum.Integral() << std::endl;
  // std::cout << "Entries hDATA= " << hDATA->GetEntries() << " hMCsig= " << hMCsig->GetEntries() << " hMCEWK= " << hMCEWK->GetEntries() << " hMCTT= " << hMCTT->GetEntries() << " MCsum= " << MCsum.GetEntries() << std::endl;
  // Double_t TH1::Chi2TestX(const TH1* h2,  Double_t &chi2, Int_t &ndf, Int_t &igood, Option_t *option,  Double_t *res) const
  Double_t chi2; Int_t ndf; Int_t igood;
  std::cout << "DATA-MC chi2: " << hDATA->Chi2TestX((TH1D*)&MCsum,chi2,ndf,igood,"") << std::endl;
  std::cout << "chi2= " << chi2 << " ndf= " << ndf << " norm chi2= " << (chi2/ndf) << " prob= " << TMath::Prob(chi2,ndf) << " igood= " << igood << std::endl;
  std::cout << std::endl;
  TLatex *t = new TLatex();
  t->SetNDC();
  // t->SetTextAlign(22);
  t->SetTextFont(63);
  t->SetTextSizePixels(17);

  // h1->SetLineColor(2);
  
  TCanvas *c1 = new TCanvas("c"+HistoName_st,"c"+HistoName_st,800,800);
  TPad *pad1 = new TPad("pad1", "",0,0.25,1,1);
  pad1->SetLogx(logx);
  pad1->SetLogy(logy);
  pad1->SetLogz(logz);
  pad1->SetTickx(1);
  pad1->SetTicky(1);
  pad1->SetBottomMargin(0);
  pad1->SetTopMargin(0.075);
  pad1->Draw();
  TPad *pad2 = new TPad("pad2", "",0,0,1,0.25);
  pad2->SetLogx(logx);
  pad2->SetTickx(1);
  pad2->SetTicky(1);
  pad2->SetTopMargin(0);
  pad2->SetBottomMargin(0.35);
  pad2->Draw();

  pad1->cd();  
  if(logy!=1)
    hDATA->GetYaxis()->SetRangeUser(0.11,hDATA->GetMaximum()*1.2);
  else
    hDATA->GetYaxis()->SetRangeUser(1,hDATA->GetMaximum()*10);
  
  hDATA->SetTitle(title.Data());
  hDATA->GetXaxis()->SetRangeUser(xmin==-1?hDATA->GetXaxis()->GetBinLowEdge(1):xmin,xmax==-1?hDATA->GetXaxis()->GetBinCenter(hDATA->GetNbinsX()):xmax);
  hDATA->GetYaxis()->SetTitle(Form("Counts / %.2f",hDATA->GetBinWidth(1)));
  hDATA->Draw("pe");
  hs->Draw("same histo");
  hMCsig2->Draw("same histo");
  hDATA->Draw("same pe");
  pad1->RedrawAxis();
  
  TLegend *leg = new TLegend(0.6,0.7,0.85,0.9,"4.75 fb^{-1} at #sqrt{7} TeV","brNDC");
  leg->SetBorderSize(0);
  leg->SetTextFont(62);
  leg->SetLineColor(1);
  leg->SetLineStyle(1);
  leg->SetLineWidth(1);
  leg->SetFillColor(0);
  leg->SetFillStyle(1001);
  leg->AddEntry(hDATA,"DATA","pl");
  leg->AddEntry(hMCsig,Form("%s (%.1f \%%)",LegendEvTypeTeX.Data(), fsig),"f");
  leg->AddEntry(hMCEWK,Form("EWK (%.1f \%%)",fewk),"f");
  leg->AddEntry(hMCQCD,Form("QCD (%.1f \%%)",fqcd),"f");
  leg->AddEntry(hMCTT,Form("TT (%.1f \%%)",ftt),"f");
  leg->Draw();
  
  t->DrawLatex(0.15,0.85,Form("norm chi2= %.2f, prob %.3e",(chi2/ndf),TMath::Prob(chi2,ndf)));
  
  pad2->cd();
  TH1D*hPullOrRatio=(TH1D*)hDATA->Clone("hPullOrRatio");
  if(PullOrRatio==0){
    for(int i=1;i<hPullOrRatio->GetNbinsX()+1;i++){
      hPullOrRatio->SetBinContent(i,hDATA->GetBinError(i)>0?(hDATA->GetBinContent(i)-MCsum.GetBinContent(i))/hDATA->GetBinError(i):0);
      // std::cout << Form("%f",hDATA->GetBinError(i)>0?(hDATA->GetBinContent(i)-MCsum.GetBinContent(i))/hDATA->GetBinError(i):0) << std::endl;
    }  
  }else{
    hPullOrRatio->Divide(((TH1D*)&MCsum));
  }
    
  hPullOrRatio->GetXaxis()->SetLabelSize(0.04*0.75/0.25);
  hPullOrRatio->GetXaxis()->SetTitleOffset(1);
  hPullOrRatio->GetXaxis()->SetTitleSize(0.04*0.75/0.25);
  hPullOrRatio->GetYaxis()->SetTitle(PullOrRatio==0?"Pull":"Ratio");
  hPullOrRatio->GetYaxis()->SetLabelSize(0.04*0.75/0.25);
  hPullOrRatio->GetYaxis()->SetTitleOffset(0.35);
  hPullOrRatio->GetYaxis()->SetTitleSize(0.04*0.75/0.25);
  hPullOrRatio->GetYaxis()->SetNdivisions(410);
  // hPullOrRatio->GetYaxis()->SetRangeUser(-14.9,14.9);
  if(PullOrRatio==0)
    hPullOrRatio->GetYaxis()->SetRangeUser(-5.9,5.9);
  else
    hPullOrRatio->GetYaxis()->SetRangeUser(0.9,1.1);
  
  hPullOrRatio->Draw("p histo");
  TLine*l0=new TLine(xmin==-1?hDATA->GetXaxis()->GetBinLowEdge(1):xmin,!PullOrRatio?0:1,xmax==-1?hDATA->GetXaxis()->GetBinCenter(hDATA->GetNbinsX()):xmax,!PullOrRatio?0:1);l0->SetLineColor(kGray);
  TLine*lp5=new TLine(xmin==-1?hDATA->GetXaxis()->GetBinLowEdge(1):xmin,!PullOrRatio?5:1.05,xmax==-1?hDATA->GetXaxis()->GetBinCenter(hDATA->GetNbinsX()):xmax,!PullOrRatio?5:1.05);lp5->SetLineColor(kGray);
  TLine*lm5=new TLine(xmin==-1?hDATA->GetXaxis()->GetBinLowEdge(1):xmin,!PullOrRatio?-5:0.95,xmax==-1?hDATA->GetXaxis()->GetBinCenter(hDATA->GetNbinsX()):xmax,!PullOrRatio?-5:0.95);lm5->SetLineColor(kGray);
  l0->Draw("same");
  lp5->Draw("same");
  lm5->Draw("same");
  hPullOrRatio->Draw("p same histo");
  
  TString extra_ouput_str = "";
  if(logx)extra_ouput_str+="_logx";
  if(logy)extra_ouput_str+="_logy";
  if(logz)extra_ouput_str+="_logz";
  if(scaleMCtoDATA)extra_ouput_str+="_norm";
  if(xmin!=-1)extra_ouput_str+=Form("_xmin%.f",xmin);
  if(xmax!=-1)extra_ouput_str+=Form("_xmax%.f",xmax);
  c1->SaveAs(HistoName_st+extra_ouput_str+".png");
}
