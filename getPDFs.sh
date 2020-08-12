#!/usr/bin/env bash

# base_url="https://www.nicoclub.com/service-manual?fsm=Titan/2016%20XD/"
array=(ACC ADP AV BCS BR BRC BRM CCS CHG CO DAS DEF DLK DLN EC EM EX EXL EXT FAX FL FSU FWD GI GW HA HAC HRN IDX INL INT IP LAN LU MA MIR MWI PB PCS PG PWC PWO RAX RSU SB SE SEC SN SR SRC ST STR TM TTS VTL WCS WT WW)
file_ext=".pdf"

# array=( "${array[@]/#/$base_url}" )
# array=( "${array[@]/%/$file_ext}" )

# printf '%s\n' "${array[@]}"

array=( "${array[@]/%/$file_ext}" )

# for i in "${array[@]}"
    # do
        # wget $i
    # done

for i in "${array[@]}"
    do
        echo $i >> pdf.lst
    done
