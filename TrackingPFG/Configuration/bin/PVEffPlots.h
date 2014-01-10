#ifndef TrackingPFG_Configuration_PVEffPlots_h
#define TrackingPFG_Configuration_PVEffPlots_h

void compareEfficiencies(const char* file1, const char* sel1, const char* cut1, 
			 const char* file2, const char* sel2, const char* cut2, 
			 const char* histname="ntrk", const char* path="");
void PVEffPlots(const char* filename, const char* denominator, const int rebin=1, const char* histname="ntrk", const char* path="");

#endif // TrackingPFG_Configuration_PVEffPlots_h
