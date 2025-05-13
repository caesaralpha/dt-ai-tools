#!/bin/bash
#SBATCH --job-name=dt-tools
#SBATCH --output=logs/dt-tools-%j.out
#SBATCH --error=logs/dt-tools-%j.err

#SBATCH --gpus 1
#SBATCH -p gpu_a100

#SBATCH --time=00:30:00  
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=c.caesaralphairawan@students.uu.nl

module load 2023 CUDA/12.4.0 PyTorch/2.1.2-foss-2023a torchvision/0.16.0-foss-2023a-CUDA-12.1.1
module list
echo ">>>>>>>>>>Modules loaded <<<<<<<<<"

# Activate your conda environment
source /projects/prjs1547/dtenv/bin/activate
echo ">>>>>>>>>>dtenv is activated <<<<<<<<<" 


# Run the Python script
transcribe-anything https://www.youtube.com/watch?v=dQw4w9WgXcQ --device cuda --output_dir /projects/prjs1547/dt-ai-tools/output/transcriber_out
# cd /projects/prjs1547/dt-ai-tools/src
# python main.py

