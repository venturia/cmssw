#include "PVEffPlots.h"
#include <iostream>
#include "TFile.h"
#include "TH1F.h"
#include "DPGAnalysis/SiStripTools/interface/CommonAnalyzer.h"
#include "TCanvas.h"

void compareEfficiencies(const char* file1, const char* sel1, const char* cut1, 
			 const char* file2, const char* sel2, const char* cut2, 
			 const char* histname, const char* path) {

  char fullname[300];

  sprintf(fullname,"rootfiles/PVEff_PFG_%s.root",file1);
  TFile ff1(fullname);

  sprintf(fullname,"rootfiles/PVEff_PFG_%s.root",file2);
  TFile ff2(fullname);


  char num1[100];
  sprintf(num1,"%s%s",sel1,cut1);
  char num2[100];
  sprintf(num2,"%s%s",sel2,cut2);

  CommonAnalyzer cadenom1(&ff1,"",sel1,path);
  CommonAnalyzer cadenom2(&ff2,"",sel2,path);
  CommonAnalyzer canum1(&ff1,"",num1,path);
  CommonAnalyzer canum2(&ff2,"",num2,path);

  char cname[1000];
  sprintf(cname,"%s_%s_%s_%s_%s_%s_%s",file1,file2,sel1,sel2,cut1,cut2,histname);
  new TCanvas(cname,cname);

  TH1F* ratio1 = canum1.getBinomialRatio(cadenom1,histname);
  TH1F* ratio2 = canum2.getBinomialRatio(cadenom2,histname);

  if(ratio1!=0 && ratio2!=0) {
    
    ratio1->SetMarkerStyle(20);      ratio2->SetMarkerStyle(20);
    ratio1->SetMarkerSize(0.5);      ratio2->SetMarkerSize(0.5);
    ratio2->SetMarkerColor(kRed);
    ratio2->SetLineColor(kRed);
    ratio1->Draw("e");
    ratio2->Draw("esame");
  }
  else {
    std::cout << " ratio not found" << std::endl;
  }
  
}

void PVEffPlots(const char* filename, const char* denominator, const int rebin, const char* histname, const char* path) {

  
  char fullname[300];
  sprintf(fullname,"rootfiles/PVEff_PFG_%s.root",filename);
  
  TFile ff(fullname);


  //  char denominator[100];
  char numerator[100];

  //  sprintf(denominator,"trackcountTrigSel");

  CommonAnalyzer cadenom(&ff,"",denominator,path);

  char cname[300];
  sprintf(cname,"%s_%s_%s",filename,denominator,histname);
  new TCanvas(cname,cname);

  for(int cut=1;cut<7;++cut) {
    
    sprintf(numerator,"%sCut%d",denominator,cut);
    std::cout << numerator << std::endl;
    CommonAnalyzer canum(&ff,"",numerator,path);

    TH1F* ratio = canum.getBinomialRatio(cadenom,histname,rebin);

    if(ratio) {
      
      std::cout << numerator << " ratio found" << std::endl;
      ratio->SetMarkerStyle(19+cut);
      ratio->SetMarkerSize(0.5);
      ratio->SetMarkerColor(cut);
      ratio->SetLineColor(cut);
      if(cut==1) {
	ratio->Draw("el");
      }
      else {
	ratio->Draw("elsame");
      }
      
    }
    else {
      std::cout << numerator << " ratio not found" << std::endl;
    }
    
  }
  
}

