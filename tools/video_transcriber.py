import pytranscript as pt
from pathlib import Path

def transcribe_video_or_audio(input_file, output_file, model="vosk-model-en-us-aspire-0.2", target_language=None, start=0, end=None):
    """
    Transcribes a video or audio file and optionally translates the transcript to a target language.

    Args:
        input_file (str): Path to the input video or audio file.
        output_file (str): Path to save the transcript (e.g., .srt or .txt).
        model (str): Path to the transcription model.
        target_language (str, optional): Language code for translation (e.g., "fr" for French). Defaults to None.
        start (int, optional): Start time in seconds for transcription. Defaults to 0.
        end (int, optional): End time in seconds for transcription. Defaults to None.

    Returns:
        None
    """
    # Ensure the input file exists
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    # Define the temporary audio file path
    temp_audio_path = Path("temp_audio.wav")

    # Delete the temporary file if it already exists
    if temp_audio_path.exists():
        temp_audio_path.unlink()

    # Convert video to a valid WAV file if necessary
    wav_file = pt.to_valid_wav(input_file, str(temp_audio_path), start=start, end=end)

    # Transcribe the audio
    transcript = pt.transcribe(wav_file, model=model, max_size=None)

    # Translate the transcript if a target language is specified
    if target_language:
        transcript, errors = transcript.translate(target_language)

    # Write the transcript to the output file
    transcript.write(output_file)

    print(f"Transcription completed. Transcript saved to '{output_file}'.")