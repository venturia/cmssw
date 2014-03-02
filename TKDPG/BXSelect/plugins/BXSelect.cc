#include "TKDPG/BXSelect/plugins/BXSelect.h"

#include "DPGAnalysis/SiStripTools/interface/EventWithHistory.h"

BXSelect::BXSelect(const edm::ParameterSet & iConfig) {
  selectBXs_ = iConfig.getParameter<std::vector<unsigned int> >("SelectBXs");
  selectionWindow_ = iConfig.getParameter<unsigned int>("SelectionWindow");
}


BXSelect::~BXSelect() {
}


bool BXSelect::filter(edm::Event & iEvent, const edm::EventSetup & iSetup) {
  int bx = iEvent.bunchCrossing();
  for (unsigned int i = 0; i < selectBXs_.size(); ++i) {
    if (abs(bx - (int) selectBXs_.at(i)) < int(selectionWindow_)) return true;
  }
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(BXSelect);
