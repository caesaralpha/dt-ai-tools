import sys
from pathlib import Path

# Add the project root to sys.path for module imports
project_root = Path(__file__).resolve().parent.parent
tools_dir = project_root / "tools"
if str(tools_dir) not in sys.path:
    sys.path.append(str(tools_dir))

from video_transcriber import transcribe_video_or_audio
from docling_docs import convert_docs_to_markdown

def test_transcription():
    print("Starting transcription process...")
    
    # Define input and output paths relative to the project root
    input_file = project_root / "data" / "samplevid.mp4"
    output_dir = project_root / "output" / "transcriber_out"
    
    # Ensure input file exists
    if not input_file.is_file():
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)
    
    # Ensure output directory exists or create it
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error creating output directory '{output_dir}': {e}")
        sys.exit(1)
    
    # Call the transcription function
    try:
        transcribe_video_or_audio(
            input_file=str(input_file),
            output_file=str(output_dir)+"/transcript.srt",
            model=project_root /"models"/"vosk-model-en-us-0.42-gigaspeech"
        )
        print("Transcription completed successfully.")
    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        sys.exit(1)

def test_docling():
    print("Starting document conversion process...")
    
    # Define sources and output directory
    sources = [
        str(project_root / "data" / "samplepdf.pdf")
    ]
    output_dir = project_root / "output" / "docling_out"
    
    # Ensure output directory exists or create it
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error creating output directory '{output_dir}': {e}")
        sys.exit(1)
    
    # Call the document conversion function
    try:
        convert_docs_to_markdown(sources, str(output_dir))
        print("Document conversion completed successfully.")
    except Exception as e:
        print(f"An error occurred during document conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # test_transcription()
    test_docling()