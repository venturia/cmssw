#!/bin/bash

export DIRNAME=$1

mv /afs/cern.ch/cms/tracking/output/rootfiles/Tracking_PFG_$DIRNAME.root  /afs/cern.ch/cms/tracking/output/rootfiles/obsolete/Tracking_PFG_$DIRNAME.root 
mv /afs/cern.ch/cms/tracking/workareas/rootfiles_archive/Tracking_PFG_$DIRNAME.root  /afs/cern.ch/cms/tracking/workareas/rootfiles_archive/obsolete/Tracking_PFG_$DIRNAME.root 
rm -rf /afs/cern.ch/cms/tracking/www/plots/$DIRNAME

