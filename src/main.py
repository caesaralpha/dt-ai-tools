from tools import transcribe_video

def main():
    transcribe_video(
        input_source="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        output_dir="output/transcribe_out",
        device="cuda",
        model_size="small"
    )