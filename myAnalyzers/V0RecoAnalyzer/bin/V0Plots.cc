#include "V0Plots.h"
#include <vector>
#include <string>
#include <map>
#include "TFile.h"
#include "TPad.h"
#include "TStyle.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TF1.h"
#include "DPGAnalysis/SiStripTools/interface/CommonAnalyzer.h"

void V0Plots(const char* fullname, const char* ksmod, const char* lammod, const char* label, const char* postfix, const char* shortname, const char* outtrunk) {
  //  char fullname[300];
  //  sprintf(fullname,"rootfiles/Tracking_PFG_%s.root",filename);

  TFile ff(fullname);
  gStyle->SetOptFit(1);

  char fullpost[300];
  sprintf(fullpost,"%s%s",label,postfix);

  char mname[300];

  sprintf(mname,"%s%s",ksmod,postfix);

  CommonAnalyzer castat(&ff,"",mname);

  TH1F* k0s  = (TH1F*)castat.getObject("ksCandMass");
  if(k0s) {
    if(k0s->GetFunction("ksFit_doubGaus")) {
      k0s->GetFunction("ksFit_doubGaus")->SetLineColor(kRed);
      k0s->GetFunction("ksFit_doubGaus")->SetLineWidth(1);
    }
    k0s->SetMarkerStyle(20);
    
    k0s->Draw("e");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/K0s";
    plotfilename += fullpost;
    plotfilename += "_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    delete k0s;
  }

  gStyle->SetOptStat(11);
  TH1F* k0mass_eta  = (TH1F*)castat.getObject("KsMassBiasVsEta");
  if(k0mass_eta) {
    k0mass_eta->Draw("e");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/K0mass";
    plotfilename += fullpost;
    plotfilename += "_eta_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    delete k0mass_eta;
  }

  TH1F* k0mass_phi  = (TH1F*)castat.getObject("KsMassBiasVsPhi");
  if(k0mass_phi) {
    k0mass_phi->Draw("e");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/K0mass";
    plotfilename += fullpost;
    plotfilename += "_phi_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    delete k0mass_phi;
  }
  //  gStyle->SetOptStat(11);
  TH2F* k0mass_etaphi  = (TH2F*)castat.getObject("KsMassBiasEtaVsPhi");
  if(k0mass_etaphi) {
    {
    k0mass_etaphi->Draw("colz");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/K0mass";
    plotfilename += fullpost;
    plotfilename += "_etaphi_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    }
    {
    k0mass_etaphi->Draw("lego");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/K0mass";
    plotfilename += fullpost;
    plotfilename += "_etaphilego_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    }
    delete k0mass_etaphi;
  }

  gStyle->SetOptStat(1111);


  sprintf(mname,"%s%s",lammod,postfix);

  CommonAnalyzer calam(&ff,"",mname);

  TH1F* lam  = (TH1F*)calam.getObject("lamCandMass");
  if(lam) {
    if(lam->GetFunction("lamFit_doubGaus")) {
      lam->GetFunction("lamFit_doubGaus")->SetLineColor(kRed);
      lam->GetFunction("lamFit_doubGaus")->SetLineWidth(1);
    }
    lam->SetMarkerStyle(20);
    lam->Draw("e");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/Lam";
    plotfilename += fullpost;
    plotfilename += "_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    delete lam;
  }

  gStyle->SetOptStat(11);
  TH1F* lammass_eta  = (TH1F*)calam.getObject("LamMassBiasVsEta");
  if(lammass_eta) {
    lammass_eta->Draw("e");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/Lammass";
    plotfilename += fullpost;
    plotfilename += "_eta_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    delete lammass_eta;
  }

  TH1F* lammass_phi  = (TH1F*)calam.getObject("LamMassBiasVsPhi");
  if(lammass_phi) {
    lammass_phi->Draw("e");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/Lammass";
    plotfilename += fullpost;
    plotfilename += "_phi_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    delete lammass_phi;
  }
  TH2F* lammass_etaphi  = (TH2F*)calam.getObject("LamMassBiasEtaVsPhi");
  if(lammass_etaphi) {
    lammass_etaphi->Draw("colz");
    std::string plotfilename;
    plotfilename += outtrunk;
    plotfilename += shortname;
    plotfilename += "/Lammass";
    plotfilename += fullpost;
    plotfilename += "_etaphi_";
    plotfilename += shortname;
    plotfilename += ".gif";
    gPad->Print(plotfilename.c_str());
    delete lammass_etaphi;
  }

  gStyle->SetOptStat(1111);


}

