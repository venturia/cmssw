#!/bin/bash

export DIRNAME=$1

cp tar/$1.tar.gz $1.tar.gz 
gunzip $1.tar
tar xvf $1.tar 
rm  $1.tar
