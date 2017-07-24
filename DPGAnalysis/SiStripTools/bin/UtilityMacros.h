#ifndef DPGAnalysis_SiStripTools_UtilityMacros_h
#define DPGAnalysis_SiStripTools_UtilityMacros_h

class TH1D;
class TProfile2D;
class TFile;
TH1D* projectProfile2DAlongX(TProfile2D* prof2d) ;
TH1D* projectProfile2DAlongY(TProfile2D* prof2d) ;
TH1D* GenericTimeProfileRatio(TFile& ff, const char* modulen, const char* moduled, const char* hnamen, const char* hnamed, const int irun);
TH1D* GenericProfileRatio(TFile& ff, const char* modulen, const char* moduled, const char* foldern, const char* folderd, const char* hnamen, const char* hnamed);

#endif //  DPGAnalysis_SiStripTools_UtilityMacros_h
