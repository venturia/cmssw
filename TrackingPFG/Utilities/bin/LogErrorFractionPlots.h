class TObjArray;
TObjArray* genericErrorFractions(const char* histname, 
				 const char* denfile, const char* numfile, 
				 const char* denmod, const char* nummod, 
				 const char* title,
				 const int rebin = -1 );

void errorFractionsVsBXLumi(const char* file, const char* denmod, const char* nummod, const char* title);

void errorFractionsVsNpileup(const char* file, const char* denmod, const char* nummod, const char* title);

void errorFractionsVsAveNpileup(const char* file, const char* denmod, const char* nummod, const char* title, const double xsect);

void errorFractionsVsNpixelclus(const char* file, const char* denmod, const char* nummod, const char* title);

void errorFractionsVsNstripclus(const char* file, const char* denmod, const char* nummod, const char* title);
