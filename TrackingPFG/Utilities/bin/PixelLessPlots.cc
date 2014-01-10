#include "PixelLessPlots.h"
#include <vector>
#include <string>
#include <map>
#include "TPad.h"
#include "TFile.h"
#include "TH2F.h"
#include "TH1F.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "DPGAnalysis/SiStripTools/interface/CommonAnalyzer.h"
#include "TCanvas.h"
#include "TSystem.h"
#include "TStyle.h"
#include "TLegend.h"

void PixelLessPlotsForWeb(const char* fullname, const char* module1, const char* module2, const char* label, const char* postfix, const char* title, const char* shortname) {

  char modfull1[300];
  sprintf(modfull1,"%s%s",module1,postfix);
  char modfull2[300];
  sprintf(modfull2,"%s%s",module2,postfix);
  char labfull[300];
  sprintf(labfull,"%s%s",label,postfix);

  char titlefull[300];
  sprintf(titlefull,"%s_%s",title,postfix);

  //  char fullname[300];
  //  sprintf(fullname,"rootfiles/Tracking_PFG_%s.root",filename);

  TFile ff(fullname);

  // Colliding events

  
  CommonAnalyzer castat1(&ff,"",modfull1);
  CommonAnalyzer castat2(&ff,"",modfull2);

      TH1F* htibtidratio1  = (TH1F*)castat1.getObject("htibtidratio");
      TH1F* htibtidratio2  = (TH1F*)castat2.getObject("htibtidratio");
      if (htibtidratio1 && htibtidratio2 ) {
	htibtidratio1->Draw();
	htibtidratio2->SetLineColor(kRed);
	htibtidratio2->Draw("same");
	TLegend leg(.55,.6,.85,.8,titlefull);
	leg.AddEntry(htibtidratio1,"All Events","l");
	leg.AddEntry(htibtidratio2,"First vertex abs(z)<12 cm","l");
	leg.Draw();
	std::string plotfilename;
	plotfilename += "htibtidratio_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->SetLogy(1);
	gPad->Print(plotfilename.c_str());
	gPad->SetLogy(0);
	delete htibtidratio1;
	delete htibtidratio2;
      }
      TH1F* htobtecratio1  = (TH1F*)castat1.getObject("htobtecratio");
      TH1F* htobtecratio2  = (TH1F*)castat2.getObject("htobtecratio");
      if (htobtecratio1 && htobtecratio2 ) {
	htobtecratio1->Draw();
	htobtecratio2->SetLineColor(kRed);
	htobtecratio2->Draw("same");
	TLegend leg(.55,.6,.85,.8,titlefull);
	leg.AddEntry(htobtecratio1,"All Events","l");
	leg.AddEntry(htobtecratio2,"First vertex abs(z)<12 cm","l");
	leg.Draw();
	std::string plotfilename;
	plotfilename += "htobtecratio_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->SetLogy(1);
	gPad->Print(plotfilename.c_str());
	gPad->SetLogy(0);
	delete htobtecratio1;
	delete htobtecratio2;
      }
      TH1F* hpxllessratio1  = (TH1F*)castat1.getObject("hpxllessratio");
      TH1F* hpxllessratio2  = (TH1F*)castat2.getObject("hpxllessratio");
      if (hpxllessratio1 && hpxllessratio2 ) {
	hpxllessratio1->Draw();
	hpxllessratio2->SetLineColor(kRed);
	hpxllessratio2->Draw("same");
	TLegend leg(.55,.6,.85,.8,titlefull);
	leg.AddEntry(hpxllessratio1,"All Events","l");
	leg.AddEntry(hpxllessratio2,"First vertex abs(z)<12 cm","l");
	leg.Draw();
	std::string plotfilename;
	plotfilename += "hpxllessratio_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->SetLogy(1);
	gPad->Print(plotfilename.c_str());
	gPad->SetLogy(0);
	delete hpxllessratio1;
	delete hpxllessratio2;
      }

}

void PixelLessPlots(const char* fullname,const char* module, const char* label, const char* postfix, const char* shortname, const char* outtrunk) {

  char modfull[300];
  sprintf(modfull,"%s%s",module,postfix);
  char labfull[300];
  sprintf(labfull,"%s%s",label,postfix);


  //  char fullname[300];
  //  sprintf(fullname,"rootfiles/Tracking_PFG_%s.root",filename);

  TFile ff(fullname);

  // Colliding events

  
  CommonAnalyzer castat(&ff,"",modfull);

      TH1F* htibtidratio  = (TH1F*)castat.getObject("htibtidratio");
      if (htibtidratio) {
	htibtidratio->Draw();
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/htibtidratio_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->SetLogy(1);
	gPad->Print(plotfilename.c_str());
	gPad->SetLogy(0);
	delete htibtidratio;
      }
      TH1F* htobtecratio  = (TH1F*)castat.getObject("htobtecratio");
      if (htobtecratio) {
	htobtecratio->Draw();
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/htobtecratio_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->SetLogy(1);
	gPad->Print(plotfilename.c_str());
	gPad->SetLogy(0);
	delete htobtecratio;
      }
      TH1F* hpxllessratio  = (TH1F*)castat.getObject("hpxllessratio");
      if (hpxllessratio) {
	hpxllessratio->Draw();
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/hpxllessratio_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->SetLogy(1);
	gPad->Print(plotfilename.c_str());
	gPad->SetLogy(0);
	delete hpxllessratio;
      }
      TProfile* htibtidratiovsz  = (TProfile*)castat.getObject("htibtidratiovsz");
      if (htibtidratiovsz) {
	htibtidratiovsz->Draw();
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/htibtidratiovsz_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->Print(plotfilename.c_str());
	delete htibtidratiovsz;
      }
      TProfile* htobtecratiovsz  = (TProfile*)castat.getObject("htobtecratiovsz");
      if (htobtecratiovsz) {
	htobtecratiovsz->Draw();
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/htobtecratiovsz_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->Print(plotfilename.c_str());
	delete htobtecratiovsz;
      }
      TProfile* hpxllessratiovsz  = (TProfile*)castat.getObject("hpxllessratiovsz");
      if (hpxllessratiovsz) {
	hpxllessratiovsz->Draw();
	std::string plotfilename;
	plotfilename += outtrunk;
	plotfilename += shortname;
	plotfilename += "/hpxllessratiovsz_";
	plotfilename += labfull;
	plotfilename += "_";
	plotfilename += shortname;
	plotfilename += ".gif";
	gPad->Print(plotfilename.c_str());
	delete hpxllessratiovsz;
      }

}
