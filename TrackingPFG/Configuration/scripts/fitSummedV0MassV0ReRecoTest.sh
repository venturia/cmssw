#!/bin/bash

export SUFFIX=$1
export INPUTFILENAME=V0ReRecoTest_${SUFFIX}.root
export OUTPUTFILENAME=V0ReRecoTest_${SUFFIX}_fittedV0.root
export TMPFILENAME=allTracking.root
export MAINDIR="rootfiles"
export WORKDIR="."
#export MAINDIR=${TMPDIR}
#export WORKDIR=${TMPDIR}

mkdir ${MAINDIR}/backup
cp ${MAINDIR}/${INPUTFILENAME} ${MAINDIR}/backup/${INPUTFILENAME}
mv ${MAINDIR}/${INPUTFILENAME} ${WORKDIR}/${TMPFILENAME}
cd ${WORKDIR}
root -b -q /afs/cern.ch/cms/tracking/output/macros/fitSummedV0MassV0ReRecoTest.C
mv ${TMPFILENAME} ${MAINDIR}/${OUTPUTFILENAME} 
#rm ${TMPFILENAME}

