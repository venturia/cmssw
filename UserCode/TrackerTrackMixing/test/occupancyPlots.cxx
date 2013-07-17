TTree *data = _file0->Get("Events");
TTree *mc   = _file1->Get("Events");
TList   labels;
TArrayD ratio_d, ratio_m;
TArrayD ratio_rms_d, ratio_rms_m;
TH1 *globalRatios;
TString outDir = "testplots";
TString bins = "(48,0,120)";

void aliasNtk(TTree *t, TString tracks="generalTracks", TString alias="ntracks") {
    TString altk = t->GetAlias(tracks);
    altk.ReplaceAll(".obj", ".@obj.size()");
    t->SetAlias(alias,altk);
}
void occupancyPlots(int a=1) {
    //gROOT->ProcessLine(".x ~/Scratch/DATA/tdrstyle.C");
    gROOT->ProcessLine(".x ~/cpp/tdrstyle.cc");
    gStyle->SetOptStat(0);
    gStyle->SetPadRightMargin(0.03);
    
    //aliasNtk(data); 
    //aliasNtk(mc);
    data->SetAlias("ntracks", data->GetAlias("NTKhp"));
    mc->SetAlias("ntracks", mc->GetAlias("NTKhp"));
    //data->SetAlias("ntracks","recoTracks_generalTracks__RECO1.@obj.size()");
    //mc->SetAlias("ntracks","recoTracks_generalTracks__RECO1.@obj.size()");
    c1 = new TCanvas("c1","c1");

    if (a) pAll();
}
void pAll() {
    labels.Clear();
    ratio_d.Set(200);
    ratio_m.Set(200);
    ratio_rms_d.Set(200);
    ratio_rms_m.Set(200);

    p("ALL");
    p("STRIP");
    p("PIXEL");
    p("PXB",3);
    p("PXF",2);
    p("TIB",4);
    p("TOB",6);
    p("TID",3);
    p("TEC",9);
    summary();
}

void p(const char *what, int max=0) {
    char buff[255];
    p4(what,true);
    for (int i = 1; i <= max; ++i) {
        sprintf(buff,"%s%d",what,i);
        p4(buff,false);
    }
}

void summary() {
    TH1 *hd = new TH1F("hd","hd",labels.GetSize(), 0., labels.GetSize());
    TH1 *hm = new TH1F("hm","hm",labels.GetSize(), 0., labels.GetSize());
    int b = 1;
    TObjString *obj; TIter next(&labels);
    for (int b = 1; obj = (TObjString*) next(); ++b) {
        hd->GetXaxis()->SetBinLabel(b,obj->GetString());
        hm->GetXaxis()->SetBinLabel(b,obj->GetString());
        if (obj->GetString() == "") continue;
        hd->SetBinContent(b, ratio_d[b-1]);
        hm->SetBinContent(b, ratio_m[b-1]);
        hd->SetBinError(b, ratio_rms_d[b-1]);
        hm->SetBinError(b, ratio_rms_m[b-1]);
    }
    hd->SetLineColor(kRed); hd->SetMarkerColor(kRed); hd->SetLineWidth(2); hd->SetMarkerStyle(20); hd->SetMarkerSize(1.2);
    hm->SetLineColor(kBlue); hm->SetMarkerColor(kBlue); hm->SetLineWidth(2); hm->SetMarkerStyle(24); hm->SetMarkerSize(1.6);
    hm->GetYaxis()->SetTitle("fraction of on-track clusters");
    hm->GetYaxis()->SetTitleOffset(1.4);
    hm->GetYaxis()->SetTitleSize(.05);
    hm->GetXaxis()->SetTitleSize(.05);
    hm->GetYaxis()->SetLabelSize(.04);
    hm->GetXaxis()->SetLabelSize(.04);

    hm->Draw("E");
    hd->Draw("E SAME");
    TLegend *l = new TLegend(.75,.8,.9,.9);
    l->AddEntry(hd,"Data");
    l->AddEntry(hm,"MC");
    l->SetTextFont(42);
    l->SetTextSize(.04);
    l->SetFillColor(kWhite);
    l->Draw("SAME");

    c1->Print(outDir+"/00_Summary.png");
}

void p4(TString what, bool addToSummary) {
    TH1 *h, *h1, *h2, *h3, *h4;

    // first plot once to get the limits
    data->Draw(what+":ntracks>>h"+bins,"","PROF");
    h = (TH1*) gROOT->FindObject("h");
    h->SetLineColor(kRed); h->SetMarkerColor(kRed); h->SetLineWidth(2); h->SetMarkerStyle(21); h->SetMarkerSize(1.2);
    h->GetXaxis()->SetTitle("number of tracks");
    h->GetYaxis()->SetTitle("number of clusters ("+what+")");
    h->GetYaxis()->SetTitleOffset(1.4);
    h->GetYaxis()->SetTitleSize(.05);
    h->GetXaxis()->SetTitleSize(.05);
    h->GetYaxis()->SetLabelSize(.04);
    h->GetXaxis()->SetLabelSize(.04);


    mc->Draw(what+":ntracks>>h1"+bins,"","PROF");
    h1 = (TH1*) gROOT->FindObject("h1");
    h1->SetLineColor(kBlue); h1->SetMarkerColor(kBlue); h1->SetLineWidth(2); h1->SetMarkerStyle(25); h1->SetMarkerSize(1.5);

    data->Draw(what+":ntracks>>h2"+bins,"","PROF");
    h2 = (TH1*) gROOT->FindObject("h2");
    h2->SetLineColor(kRed); h2->SetMarkerColor(kRed); h2->SetLineWidth(2); h2->SetMarkerStyle(21); h2->SetMarkerSize(1.2);

    mc->Draw(what+"on:ntracks>>h3"+bins,"","PROF");
    h3 = (TH1*) gROOT->FindObject("h3");
    h3->SetLineColor(kBlue); h3->SetMarkerColor(kBlue); h3->SetLineWidth(2); h3->SetMarkerStyle(24); h3->SetMarkerSize(1.6);

    data->Draw(what+"on:ntracks>>h4"+bins,"","PROF");
    h4 = (TH1*) gROOT->FindObject("h4");
    h4->SetLineColor(kRed); h4->SetMarkerColor(kRed); h4->SetLineWidth(2); h4->SetMarkerStyle(20); h4->SetMarkerSize(1.2);

    h->Draw("");
    h1->Draw("SAME");
    h2->Draw("SAME");
    h3->Draw("SAME");
    h4->Draw("SAME");

    TLegend *l = new TLegend(.2,.7,.65,.9);
    l->AddEntry(h2,"Data - All");
    l->AddEntry(h1,"MC - All");
    l->AddEntry(h4,"Data - On Track");
    l->AddEntry(h3,"MC - On Track");
    l->SetTextFont(42);
    l->SetTextSize(.04);
    l->SetFillColor(kWhite);
    l->Draw("SAME");

    c1->Print((addToSummary ? outDir+"/0_" : outdir+"/" ) +what+".png");
    
    // first plot once to get the limits
    data->Draw(what+"on/"+what+":ntracks>>hd"+bins,"ntracks>5","PROF");
    TH1 *hd = (TH1*) gROOT->FindObject("hd");
    hd->SetLineColor(kRed); hd->SetMarkerColor(kRed); hd->SetLineWidth(2); hd->SetMarkerStyle(20); hd->SetMarkerSize(1.2);

    mc->Draw(what+"on/"+what+":ntracks>>hm"+bins,"ntracks>5","PROF");
    TH1 *hm = (TH1*) gROOT->FindObject("hm");
    hm->SetLineColor(kBlue); hm->SetMarkerColor(kBlue); hm->SetLineWidth(2); hm->SetMarkerStyle(24); hm->SetMarkerSize(1.6);

    if (addToSummary) {
        ratio_d[labels.GetSize()] = hd->GetMean(2);
        ratio_m[labels.GetSize()] = hm->GetMean(2);
        ratio_rms_d[labels.GetSize()] = hd->GetRMS(2);
        ratio_rms_m[labels.GetSize()] = hm->GetRMS(2);
        labels.Add(new TObjString(what));
    }
    
    TLegend *l = new TLegend(.2,.2,.45,.3);
    l->AddEntry(hd,"Data");
    l->AddEntry(hm,"MC");

    hm->GetXaxis()->SetTitle("number of tracks");
    hm->GetYaxis()->SetTitle("fraction of on-track clusters ("+what+")");
    hm->GetYaxis()->SetTitleOffset(1.4);
    hm->GetYaxis()->SetTitleSize(.05);
    hm->GetXaxis()->SetTitleSize(.05);
    hm->GetYaxis()->SetLabelSize(.04);
    hm->GetXaxis()->SetLabelSize(.04);

    hm->Draw("");
    hd->Draw("SAME");

    l->SetTextFont(42);
    l->SetTextSize(.04);
    l->SetFillColor(kWhite);
    l->Draw("SAME");

    c1->Print((addToSummary ? outDir+"/0_" : outDir+"/" ) +what+"ratio.png");

}
