#!/bin/bash
#SBATCH --job-name=dt-tools
#SBATCH --output=logs/dt-tools-%j.out
#SBATCH --error=logs/dt-tools-%j.err

#SBATCH --gpus 1
#SBATCH -p gpu_h100

#SBATCH --time=00:10:00  
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=c.caesaralphairawan@students.uu.nl

# Set the model name from the command line argument


# Activate your conda environment
source /projects/prjs1547/dtenv/bin/activate
echo ">>>>>>>>>>dtenv is activated <<<<<<<<<" 
module load 2023
# Run the Python script
cd /projects/prjs1547/dt-ai-tools/src
python main.py

