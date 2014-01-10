#include "D0PhiPlots.h"
#include <vector>
#include <string>
#include <map>
#include "TPad.h"
#include "TFile.h"
#include "TH2F.h"
#include "TH2D.h"
#include "TH1F.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "DPGAnalysis/SiStripTools/interface/CommonAnalyzer.h"
#include "TCanvas.h"
#include "TSystem.h"
#include "TStyle.h"

void D0PhiPlots(const char* fullname,const char* module, const char* label, const char* postfix, const char* shortname, const char* outtrunk) {

  char modfull[300];
  sprintf(modfull,"%s%s",module,postfix);
  char labfull[300];
  sprintf(labfull,"%s%s",label,postfix);


  //  char fullname[300];
  //  sprintf(fullname,"rootfiles/Tracking_PFG_%s.root",filename);

  TFile ff(fullname);

  // Colliding events

  
  CommonAnalyzer castat(&ff,"",modfull);

      TProfile* dxyvsphi  = (TProfile*)castat.getObject("hdxyvsphi");
      if (dxyvsphi) {
	dxyvsphi->Draw();
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/dxyvsphi_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->Print(plotfilename.c_str());
	delete dxyvsphi;
      }
      TProfile2D* dxyvsphivsz  = (TProfile2D*)castat.getObject("hdxyvsphivsz");
      if (dxyvsphivsz) {
	dxyvsphivsz->Draw("colz");
	dxyvsphivsz->GetYaxis()->SetRangeUser(-10,10);
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/dxyvsphivsz_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->Print(plotfilename.c_str());
	delete dxyvsphivsz;
      }
      TProfile2D* dxyvsphivsznocorr  = (TProfile2D*)castat.getObject("hdxyvsphivsznocorr");
      if (dxyvsphivsznocorr) {
	dxyvsphivsznocorr->Draw("colz");
	dxyvsphivsznocorr->GetYaxis()->SetRangeUser(-10,10);
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/dxyvsphivsznocorr_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->Print(plotfilename.c_str());
	delete dxyvsphivsznocorr;
      }
      TH2D* dxyvsphi2D  = (TH2D*)castat.getObject("hdxyvsphi2D");
      if (dxyvsphi2D) {
	dxyvsphi2D->Draw("colz");
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/dxyvsphi2D_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->Print(plotfilename.c_str());
	delete dxyvsphi2D;
      }
}
