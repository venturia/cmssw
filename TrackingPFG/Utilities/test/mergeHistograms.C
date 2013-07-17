{

  char* module[6];

  module[0] = new char[100];
  module[1] = new char[100];
  module[2] = new char[100];
  module[3] = new char[100];
  module[4] = new char[100];
  module[5] = new char[100];

  sprintf(module[0],"logerroranalyzer");
  sprintf(module[1],"logerrortoomanyclusters");
  sprintf(module[2],"logerrortoomanyseeds");
  sprintf(module[3],"logerrortracking");
  sprintf(module[4],"logerrortoomanytriplets");
  sprintf(module[5],"logerroranyerror");

  for(unsigned int i=0;i<6;++i) {

    TH1F merged("ncatmod_merged","Error categories and modules",10,0,10);
    merged.SetBit(TH1::kCanRebin);
    
    char tmpfilename[300];
    sprintf(tmpfilename,"%s",gSystem->Getenv("TMPFILENAME"));
    char filelist[300];
    sprintf(filelist,"%s",gSystem->Getenv("TMPFILELIST"));
    //    char module[100];
    //    sprintf(module,"%s",gSystem->Getenv("MODULE"));
    ifstream streamfilelist(filelist);
    char filename[400];
    while(streamfilelist >> filename) {
      cout << "Reading file " << filename << endl;
      TFile ff(filename);
      int res = ff.cd(module[i]);
      if(res) {
	TH1F* ncatmod = gDirectory.Get("ncatmod");
	if(ncatmod) {
	  cout << ncatmod->GetNbinsX() << endl;
	  for(unsigned int bin = 1; bin < ncatmod->GetNbinsX()+1 ; ++bin) {
	    if(ncatmod->GetBinContent(bin)) {
	      cout << ncatmod->GetXaxis()->GetBinLabel(bin) << " " << ncatmod->GetBinContent(bin) << endl;
	      merged.Fill(ncatmod->GetXaxis()->GetBinLabel(bin),ncatmod->GetBinContent(bin));
	    }
	  }
	}
      }
      
    }
    
    TFile fout(tmpfilename,"update");
    fout.cd(module[i]);
    merged.Write();
    fout.Close();
  }
}
