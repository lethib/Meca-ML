#!/bin/bash

folder=$(pwd | cut -d "/" -f 4)

#OAR -n lammps-reaxff-0,0
#OAR -l /nodes=1/core=32,walltime=10:00:00
#OAR --stdout lammps.%jobid%.out
#OAR --stderr pytest.%jobid%.err
#OAR --project pr-atosimul

# load environment
source /applis/site/guix-start.sh

# lancement du code

mpirun -np `cat $OAR_FILE_NODES|wc -l` lmp -in in_olderV2.$folder-0,0.txt
