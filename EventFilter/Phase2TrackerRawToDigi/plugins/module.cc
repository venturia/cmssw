#include "FWCore/Framework/interface/MakerMacros.h"

#include "EventFilter/Phase2TrackerRawToDigi/plugins/Phase2TrackerDigiProducer.h"
#include "EventFilter/Phase2TrackerRawToDigi/plugins/Phase2TrackerDigi_CondData_producer.h"

typedef sistrip::Phase2TrackerDigiProducer Phase2TrackerDigiProducer;
typedef sistrip::Phase2TrackerDigi_CondData_producer Phase2TrackerDigi_CondData_producer;

DEFINE_FWK_MODULE(Phase2TrackerDigiProducer);
DEFINE_FWK_MODULE(Phase2TrackerDigi_CondData_producer);
