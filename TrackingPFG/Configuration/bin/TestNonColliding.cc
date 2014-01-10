#include "TestNonColliding.h"
#include <vector>
#include <string>
#include <iostream>
#include "TFile.h"
#include "TH1F.h"
#include "DPGAnalysis/SiStripTools/interface/CommonAnalyzer.h"
#include "TCanvas.h"

void TestNonColliding(const char* fullname, const char* postfix) {

  //  char fullname[300];
  //  sprintf(fullname,"rootfiles/Tracking_PFG_%s.root",filename);

  TFile ff(fullname);

  // Colliding events

  char modname[300];
  sprintf(modname,"eventtimedistribnoncolliding%s",postfix);
  CommonAnalyzer canoncoll(&ff,"",modname);
  sprintf(modname,"eventtimedistribnoncollidingplus%s",postfix);
  CommonAnalyzer canoncollplus(&ff,"",modname);
  sprintf(modname,"eventtimedistribnoncollidingminus%s",postfix);
  CommonAnalyzer canoncollminus(&ff,"",modname);

  std::vector<unsigned int> runs = canoncoll.getRunList();

  {
    
    
    for(unsigned int i=0;i<runs.size();++i) {
      
      char runpath[100];
      sprintf(runpath,"run_%d",runs[i]);
      canoncoll.setPath(runpath);
      canoncollplus.setPath(runpath);
      canoncollminus.setPath(runpath);

      TH1F* bx = (TH1F*)canoncoll.getObject("bx");
      TH1F* bxplus = (TH1F*)canoncollplus.getObject("bx");
      TH1F* bxminus = (TH1F*)canoncollminus.getObject("bx");
      if (bx!=0 && bxplus != 0 && bxminus!=0) {
	std::cout << runpath << " " << bx->GetEntries() << " = " << bxplus->GetEntries() 
	     << " + " << bxminus->GetEntries() << " ";
	if(bx->GetEntries() == (bxplus->GetEntries() + bxminus->GetEntries())) { std::cout << " OK " <<std::endl; }
	else { std::cout <<"NOT OK !!!" << std::endl;}
      }
      else { 
	std::cout << "No Histo for run " << runpath << std::endl;
      }
      
    }
  }
}
