from docling.document_converter import DocumentConverter
from pathlib import Path

def convert_docs_to_markdown(sources, output_dir):
    """
    Converts multiple documents (PDFs or URLs) into Markdown format and saves them to files.

    Args:
        sources (list): A list of document paths or URLs to convert.
        output_dir (str): Directory to save the converted Markdown files.

    Returns:
        None
    """
    # Ensure the output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Initialize the DocumentConverter
    converter = DocumentConverter()

    for source in sources:
        try:
            # Convert the document
            result = converter.convert(source)
            markdown_content = result.document.export_to_markdown()

            # Generate a filename based on the source
            source_name = Path(source).stem if Path(source).is_file() else source.split("/")[-1]
            output_file = output_path / f"{source_name}.md"

            # Save the Markdown content to a file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(markdown_content)

            print(f"Converted '{source}' to '{output_file}'")
        except Exception as e:
            print(f"Failed to convert '{source}': {e}")