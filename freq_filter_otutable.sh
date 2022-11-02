#!/bin/bash

SCRIPTDIR=$(dirname "$(readlink -f "$0")")
python $SCRIPTDIR"/freq_filter_otutable.py" -i $1 -f $2 -ot $3 -ol $4

# sanity check
printf "Conda env: $CONDA_DEFAULT_ENV\n"
printf "Python version: $(python --version |  awk '{print $2}')\n"
printf "Pandas version: $(conda list | egrep pandas | awk '{print $2}')\n"
printf "Numpy version: $(conda list | egrep numpy | awk '{print $2}')\n"
printf "Unzip version: $(unzip -v | head -n1 | awk '{print $2}')\n"
printf "Bash version: ${BASH_VERSION}\n\n"
