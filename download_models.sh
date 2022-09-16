#!/bin/bash

fileid="16p4iHgh0sDTxjIzydHFD2YaHAiahs-bw"
filename=resources.tar.gz
modeldir="./backend/model/"

wget --save-cookies cookies.txt 'https://docs.google.com/uc?export=download&id='$fileid -O- \
     | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1/p' > confirm.txt
wget --load-cookies cookies.txt -O $filename \
     'https://docs.google.com/uc?export=download&id='$fileid'&confirm='$(<confirm.txt)

rm -f confirm.txt cookies.txt

mkdir -p $modeldir
tar zxvf $filename --directory $modeldir
rm $filename

echo Download finished.