#!/bin/bash

export SUFFIX=$2
export EOSDIR=$1
export EOSBASEDIR=/store/caf/user/venturia
export INPUTFILENAME=$3_
export INPUTFILENAMEWC=$3_*.root
export OUTPUTFILENAME=$3_${SUFFIX}.root

rm -i ${SCRATCH}/*.root

for completefile in $(cmsLs  ${EOSBASEDIR}/${EOSDIR} | grep ${EOSBASEDIR}/${EOSDIR}/${INPUTFILENAME}) 
do 

if [ `expr "$completefile" : "/store"` != 0 ]; then
    echo $completefile
    export file=$(basename $completefile)

    if [ -f ${SCRATCH}/$file ]; then
	echo "File exist already";
    else
	cmsStageIn ${EOSBASEDIR}/${EOSDIR}/$file ${SCRATCH}/$file
    fi
fi


done
hadd rootfiles/${OUTPUTFILENAME} ${SCRATCH}/${INPUTFILENAMEWC}

