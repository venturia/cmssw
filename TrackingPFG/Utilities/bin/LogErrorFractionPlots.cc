#include "LogErrorFractionPlots.h"
#include <iostream>
#include "TFile.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TLegend.h"
#include "TObjArray.h"
#include "TGaxis.h"

TObjArray* genericErrorFractions(const char* histname, 
				 const char* denfile, const char* numfile, 
				 const char* denmod, const char* nummod, 
				 const char* title,
				 const int rebin ) {

  TFile fden(denfile);
  TFile fnum(numfile);
  
  fden.cd(denmod);
  TH1F* den = 0;
  if(gDirectory) { 
    den = (TH1F*)gDirectory->Get(histname);  
    std::cout << gDirectory->GetName() << " " << den << std::endl;
  }
  fnum.cd(nummod);
  TH1F* num = 0;
  if(gDirectory) { 
    num = (TH1F*)gDirectory->Get(histname);  
    std::cout << gDirectory->GetName() << " " << num << std::endl;
}

  TObjArray * arr = new TObjArray(2);

  if(den!=0 && num!=0) {
    
    den->SetStats(0);
    num->SetStats(0);
    if(rebin > 0) {
      num->Rebin(rebin);
      den->Rebin(rebin);
    }
    TH1F*  ratio = new TH1F();
    ratio->SetName("ratio");
    den->Copy(*ratio);
    ratio->SetDirectory(0);
    ratio->SetStats(0);
    std::cout << "ratio name " << ratio->GetName() << std::endl;
    ratio->Reset();
    ratio->SetTitle(title);
    ratio->GetXaxis()->SetTitle(den->GetXaxis()->GetTitle());
    ratio->Sumw2();
    ratio->Divide(num,den,1,1,"B");
    ratio->GetYaxis()->SetRangeUser(0.,1.05);
    for(int i=1;i<ratio->GetNbinsX()+1;++i) {
      std::cout << ratio->GetBinContent(i) << " " << ratio->GetBinError(i) << std::endl ;
    }
    if(den->GetEntries()) std::cout << "Events: denominator " << den->GetEntries() << " numerator " << num->GetEntries() 
	      << " fraction " << num->GetEntries()/den->GetEntries() << std::endl;

    arr->Add(ratio);

    TCanvas* out2 = new TCanvas(denmod,denmod);
    //    den->DrawCopy();
    num->SetLineColor(kRed);
    num->SetFillColor(kRed);
    //    num->DrawCopy("same");
    TLegend*  leg = new TLegend(.5,.6,.85,.8,"");
    leg->AddEntry(den->DrawCopy(),"All Events","f");
    leg->AddEntry(num->DrawCopy("same"),title,"f");
    leg->Draw();

    arr->Add(out2);

  }

  return arr;
}

void errorFractionsVsBXLumi(const char* file, const char* denmod, const char* nummod, const char* title) {

  TObjArray* arr = genericErrorFractions("lumi",file,file,denmod,nummod,title,-1);

  std::cout << (*arr)[0] << std::endl;
  new TCanvas("ratio","ratio");
  if((*arr)[0]) (*arr)[0]->Draw();
  if((*arr)[1]) (*arr)[1]->Draw();

}

void errorFractionsVsNpileup(const char* file, const char* denmod, const char* nummod, const char* title) {

  TObjArray* arr = genericErrorFractions("nvtx",file,file,denmod,nummod,title,-1);

  std::cout << (*arr)[0] << std::endl;
  new TCanvas("ratio","ratio");
  if((*arr)[0]) (*arr)[0]->Draw();
  if((*arr)[1]) (*arr)[1]->Draw();

}

void errorFractionsVsAveNpileup(const char* file, const char* denmod, const char* nummod, const char* title, const double xsect) {

  TObjArray* arr = genericErrorFractions("lumi",file,file,denmod,nummod,title,-1);

  std::cout << (*arr)[0] << std::endl;
  new TCanvas("ratio","ratio");
  if((*arr)[0]) (*arr)[0]->Draw();
  if((*arr)[1]) (*arr)[1]->Draw();
  TGaxis* ax = new TGaxis(0.,1.05,50,1.05,0.,50*11223./(xsect*1000),510,"-");
  ax->SetTitle("BX lumi [10^{30}cm^{-2}s^{-1}]");
  ax->SetLabelOffset(-0.005);
  ax->Draw("same");

}

void errorFractionsVsNpixelclus(const char* file, const char* denmod, const char* nummod, const char* title) {

  char denmodfull[300];
  char nummodfull[300];
  sprintf(denmodfull,"%s/EventProcs/Pixel",denmod);
  sprintf(nummodfull,"%s/EventProcs/Pixel",nummod);

  TObjArray* arr = genericErrorFractions("nPixeldigi",file,file,denmodfull,nummodfull,title,2);

  std::cout << (*arr)[0] << std::endl;
  new TCanvas("ratio","ratio");
  if((*arr)[0]) (*arr)[0]->Draw();
  if((*arr)[1]) (*arr)[1]->Draw();

}

void errorFractionsVsNstripclus(const char* file, const char* denmod, const char* nummod, const char* title) {

  char denmodfull[300];
  char nummodfull[300];
  sprintf(denmodfull,"%s/EventProcs/TK",denmod);
  sprintf(nummodfull,"%s/EventProcs/TK",nummod);

  TObjArray* arr = genericErrorFractions("nTKdigi",file,file,denmodfull,nummodfull,title,2);

  std::cout << (*arr)[0] << std::endl;
  new TCanvas("ratio","ratio");
  if((*arr)[0]) (*arr)[0]->Draw();
  if((*arr)[1]) (*arr)[1]->Draw();

}
