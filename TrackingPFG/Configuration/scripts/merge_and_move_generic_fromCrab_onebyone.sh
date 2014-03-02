#!/bin/bash

export SUFFIX=$2
export CRABDIR=$1
export INPUTFILENAME=$3_*_*.root
export OUTPUTFILENAME=$3_${SUFFIX}.root

#hadd rootfiles/${OUTPUTFILENAME} ${CRABDIR}/res/${INPUTFILENAME}

i=0;
for fil in `ls ${CRABDIR}/res/${INPUTFILENAME}`; do
echo $fil $i;
#echo $i;
if [ $i == 0 ] 
then 
echo "first"
hadd ${SCRATCH}/${OUTPUTFILENAME}_temp_new $fil 
else
echo "not first"
hadd ${SCRATCH}/${OUTPUTFILENAME}_temp_new $fil ${SCRATCH}/${OUTPUTFILENAME}_temp_old
fi
echo "Moving ${SCRATCH}/${OUTPUTFILENAME}_temp_new to ${SCRATCH}/${OUTPUTFILENAME}_temp_old";
mv ${SCRATCH}/${OUTPUTFILENAME}_temp_new ${SCRATCH}/${OUTPUTFILENAME}_temp_old
i=1;
done
echo "Copying ${SCRATCH}/${OUTPUTFILENAME}_temp_old to rootfiles/${OUTPUTFILENAME}";
cp ${SCRATCH}/${OUTPUTFILENAME}_temp_old rootfiles/${OUTPUTFILENAME}