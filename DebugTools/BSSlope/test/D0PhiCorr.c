TH1D* plots(TFile* file, const char* modname, const char* name, const int first, const int last, const int rebin)  {

  if(file->cd(modname)) {

    TProfile2D* dxyvsphivsz = (TProfile2D*)gDirectory->Get("hdxyvsphivsz");

    if(dxyvsphivsz) {
      dxyvsphivsz->RebinX(rebin);
      TH1D* projall = dxyvsphivsz->ProjectionX(name,first,first);
      return projall;

    }
    else {
      cout << "2d histo not found " << endl;
    } 
  }
  return 0;

}

double d0vsphi(double* x, double* par) {

  double xx = x[0];
  double res = 0.;

  //  double dy = par[0]+sqrt(2.)/3.14159*(par[2]+par[3])/2.;
  //  double dx = par[1]+(par[2]-par[3])/2.;
  double dy = par[0];
  double dx = par[1];
  //  double dx = par[1];

  if(cos(xx) > 0) {

    res = - dy*cos(xx) + dx*sin(xx) + par[2]*(1-sin(xx));

  }
  else {

    res = - dy*cos(xx) + dx*sin(xx) - par[3]*(1-sin(xx));


  }

  return res;

}


