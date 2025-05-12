# generate a function and make it as module to transcribe video by using transcribe-anything
import transcribe_anything
import logging

def transcribe_video(
    url_or_file: str,
    output_dir: str = "output_dir",
    model: str = "large",
    task: str = "transcribe",
    device: str = "cuda"
):
    """
    Transcribe a video using transcribe-anything.

    Args:
        url_or_file (str): URL or file path of the video to transcribe.
        output_dir (str): Directory to save the transcription output.
        model (str): Model size to use (e.g., tiny, small, medium, large).
        task (str): Task to perform (transcribe or translate).
        device (str): Device to use (cuda, cpu, etc.).
    """
    logging.info(f"Starting transcription for {url_or_file}")
    transcribe_anything.transcribe_anything(
        url_or_file=url_or_file,
        output_dir=output_dir,
        task=task,
        model=model,
        device=device
    )
    logging.info(f"Transcription completed. Output saved to {output_dir}")
