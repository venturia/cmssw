#!/bin/bash

export DIRNAME=$1

tar cvf ${TMPDIR}/$1.tar $1
gzip ${TMPDIR}/$1.tar
mv ${TMPDIR}/$1.tar.gz tar/$1.tar.gz
#rm -rf $1
