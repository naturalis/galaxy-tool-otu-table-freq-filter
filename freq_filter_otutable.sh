#!/bin/bash

#location for production server
#outlocation=$(mktemp -d /media/GalaxyData/database/files/XXXXXX)
#location for the testserver
#outlocation=$(mktemp -d /media/GalaxyData/files/XXXXXX)
#outlocation=$(mktemp -d /home/galaxy/ExtraRef/XXXXXX)
SCRIPTDIR=$(dirname "$(readlink -f "$0")")
python $SCRIPTDIR"/freq_filter_otutable.py" -i $1 -f $2 -ot $3 -ol $4
