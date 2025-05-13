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
module load CUDA/12.4.0 
module list
echo ">>>>>>>>>>Modules loaded <<<<<<<<<"

conda create -n dtenv python=3.11
# Activate your environment
source activate dtenv
pip install transcribe-anything
# Check whether the GPU is available
srun python -uc "import torch; print('GPU available?', torch.cuda.is_available())"

# # Activate your conda environment
# source /projects/prjs1547/dtenv/bin/activate
# # pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
# echo ">>>>>>>>>>dtenv is activated <<<<<<<<<" 


# Run the Python script
transcribe-anything https://www.youtube.com/watch?v=dQw4w9WgXcQ --device cuda --output_dir /projects/prjs1547/dt-ai-tools/output/transcriber_out
# cd /projects/prjs1547/dt-ai-tools/src
# python main.py

