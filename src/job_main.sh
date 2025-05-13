#!/bin/bash
#SBATCH --job-name=dt-tools
#SBATCH --output=logs/dt-tools-%j.out
#SBATCH --error=logs/dt-tools-%j.err

#SBATCH --gpus 1
#SBATCH -p gpu_a100

#SBATCH --time=00:30:00  
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=c.caesaralphairawan@students.uu.nl

# Define the base project path as a parameter
BASE_PATH="/projects/prjs1547"

# Setup cache location for pip, huggingface, vosk, and transformers, all under $BASE_PATH/cache
if [ ! -d "$BASE_PATH/cache/" ]; then
    mkdir -p "$BASE_PATH/cache/"
fi
export HF_HOME="$BASE_PATH/cache/"
export TRANSFORMERS_CACHE="$BASE_PATH/cache/"
export VOSK_CACHE="$BASE_PATH/cache/"
export PIP_CACHE_DIR="$BASE_PATH/cache/"

# Activate your conda environment
source "$BASE_PATH/venv/bin/activate"
echo ">>>>>>>>>>venv is activated <<<<<<<<<" 
module load 2024 FFmpeg/7.0.2-GCCcore-13.3.0 CUDA/12.6.0
# pip install docling

# Run the Python script
cd "$BASE_PATH/dt-ai-tools/src"
# srun python main.py
python main.py