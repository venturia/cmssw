#!/bin/bash

rm /afs/cern.ch/cms/tracking/www/plots/files.list
ls /afs/cern.ch/cms/tracking/output/rootfiles/Tracking_PFG_*.root > /afs/cern.ch/cms/tracking/www/plots/files.list
rm /afs/cern.ch/cms/tracking/www/plots/files_archived.list
ls /afs/cern.ch/cms/tracking/workareas/rootfiles_archive/Tracking_PFG_*.root > /afs/cern.ch/cms/tracking/www/plots/files_archived.list

rm /afs/cern.ch/cms/tracking/www/plots/files_bspv.list
ls /afs/cern.ch/cms/tracking/output/rootfiles/BSPVertexing_PFG_*.root > /afs/cern.ch/cms/tracking/www/plots/files_bspv.list

rm /afs/cern.ch/cms/tracking/www/plots/files_pv.list
ls /afs/cern.ch/cms/tracking/output/rootfiles/Vertexing_PFG_*.root > /afs/cern.ch/cms/tracking/www/plots/files_pv.list

