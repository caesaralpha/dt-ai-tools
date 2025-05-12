import sys
from pathlib import Path

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
# Import the transcribe_video function from the tools module
from tools import transcribe_video

def main():
    transcribe_video(
        input_source="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        output_dir="output/transcribe_out",
        device="cuda",
        model_size="small"
    )