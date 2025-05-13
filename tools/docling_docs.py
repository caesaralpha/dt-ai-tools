import subprocess
from pathlib import Path

def convert_docs_to_markdown(sources, output_dir):
    """
    Converts multiple documents (PDFs or URLs) into Markdown format using the docling CLI.

    Args:
        sources (list): A list of document paths or URLs to convert.
        output_dir (str): Directory to save the converted Markdown files.

    Returns:
        None
    """
    # Ensure the output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for source in sources:
        print(f"Converting '{source}' using docling CLI...")
        try:
            # Generate a filename based on the source
            source_name = Path(source).stem if Path(source).is_file() else source.split("/")[-1]
            output_dir = output_path

            # Run the docling CLI command
            subprocess.run(
                ["docling", source, "--output", str(output_dir)],
                check=True,
                text=True
            )

            print(f"Converted '{source}' to '{output_dir}'")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert '{source}': {e}")
