#!/bin/bash
#SBATCH --job-name=dt-tools
#SBATCH --output=logs/dt-tools-%j.out
#SBATCH --error=logs/dt-tools-%j.err

#SBATCH --gpus 1
#SBATCH -p gpu_a100

#SBATCH --time=00:30:00  
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=c.caesaralphairawan@students.uu.nl
module load 2023
module load Anaconda3/2023.07-2
echo ">>>>>>>>>>Modules loaded <<<<<<<<<"

# conda create -n dtenv python=3.11
# Activate your environment
source activate dtenv
pip install pytranscript


# Run the Python script
cd /projects/prjs1547/dt-ai-tools/src
python main.py

