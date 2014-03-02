#!/bin/bash

export CRABDIR=$1
export SUFFIX=$2
export HISTFILENAME=$3
export INPUTFILENAME=${HISTFILENAME}_${SUFFIX}.root
export OUTPUTFILENAME=${HISTFILENAME}_${SUFFIX}_merged.root
export TMPFILENAME=logerrorTMP.root
export MAINDIR="rootfiles"
export WORKDIR="."
#export MAINDIR=${TMPDIR}
#export WORKDIR=${TMPDIR}
export PREFIX=${HISTFILENAME}
export TMPFILELIST=${TMPDIR}/filelist.txt

mkdir ${MAINDIR}/backup
cp ${MAINDIR}/${INPUTFILENAME} ${MAINDIR}/backup/${INPUTFILENAME}
mv ${MAINDIR}/${INPUTFILENAME} ${WORKDIR}/${TMPFILENAME}
cd ${WORKDIR}

rm ${TMPFILELIST}
ls ${CRABDIR}/res/${PREFIX}_*.root > ${TMPFILELIST}
root -b "${CMSSW_BASE}/src/TrackingPFG/Utilities/test/mergeHistograms.C"
mv ${TMPFILENAME} ${MAINDIR}/${OUTPUTFILENAME} 
