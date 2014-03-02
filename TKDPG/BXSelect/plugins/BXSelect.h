#ifndef BXSelect_BXSelect
#define BXSelect_BXSelect

// -*- C++ -*-
//
// Package:    BXSelect
// Class:      BXSelect
// 
/**\class BXSelect BXSelect.cc Steven/BXSelect/src/BXSelect.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Steven LOWETTE
//         Created:  Sat Dec  5 17:32:20 CET 2009
// $Id: BXSelect.h,v 1.1 2009/12/06 12:48:15 lowette Exp $
//
//


#include <memory>
#include <vector>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


class BXSelect : public edm::EDFilter {

  public:

    explicit BXSelect(const edm::ParameterSet &);
    ~BXSelect();

  private:

    virtual void beginJob() {}
    virtual bool filter(edm::Event &, const edm::EventSetup &);
    virtual void endJob() {}

    std::vector<unsigned int> selectBXs_;
    unsigned int selectionWindow_;

};

#endif
