#!/bin/bash

#SBATCH --job-name=S.No:5
#SBATCH --account=tzega
#SBATCH --mail-user=abhishekkt@email.arizona.edu
#SBATCH --partition=standard
#SBATCH --ntasks=90
#SBATCH --ntasks-per-node=90
#SBATCH --nodes=1
#SBATCH --mem=420gb
#SBATCH --time=50:00:00
#SBATCH --output=Sample_MPI_Job_%A.out
#SBATCH --error=Sample_MPI_Job_%A.err

module unload openmpi3 gnu8
module load vasp/5.4.4
cd $SLURM_SUBMIT_DIR
date
mpirun -np 90 vasp_std
date
