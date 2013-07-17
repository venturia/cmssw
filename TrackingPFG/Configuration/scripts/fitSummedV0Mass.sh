#!/bin/bash

export SUFFIX=$1
export INPUTFILENAME=Tracking_PFG_${SUFFIX}.root
export OUTPUTFILENAME=Tracking_PFG_${SUFFIX}_fittedV0.root
export TMPFILENAME=allTracking.root
export MAINDIR="rootfiles"
export WORKDIR="."
#export MAINDIR=${TMPDIR}
#export WORKDIR=${TMPDIR}

mkdir ${MAINDIR}/backup
cp ${MAINDIR}/${INPUTFILENAME} ${MAINDIR}/backup/${INPUTFILENAME}
mv ${MAINDIR}/${INPUTFILENAME} ${WORKDIR}/${TMPFILENAME}
cd ${WORKDIR}
root -b -q /afs/cern.ch/cms/tracking/output/macros/fitSummedV0Mass.C
mv ${TMPFILENAME} ${MAINDIR}/${OUTPUTFILENAME} 
#rm ${TMPFILENAME}

