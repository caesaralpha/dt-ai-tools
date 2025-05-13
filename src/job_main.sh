#!/bin/bash
#SBATCH --job-name=dt-tools
#SBATCH --output=logs/dt-tools-%j.out
#SBATCH --error=logs/dt-tools-%j.err

#SBATCH --gpus 1
#SBATCH -p gpu_a100

#SBATCH --time=00:30:00  
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=c.caesaralphairawan@students.uu.nl

# conda create -n dtenv python=3.11
# Activate your conda environment
source /projects/prjs1547/venv/bin/activate
# pip install pytranscript
echo ">>>>>>>>>>venv is activated <<<<<<<<<" 
module load 2024 FFmpeg/7.0.2-GCCcore-13.3.0


# Run the Python script
cd /projects/prjs1547/dt-ai-tools/src
python main.py

