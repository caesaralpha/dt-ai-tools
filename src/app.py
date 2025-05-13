import streamlit as st
from pathlib import Path
from docling_docs import convert_docs_to_markdown

# Define paths
project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"
output_dir = project_root / "output" / "docling_out"

# Streamlit UI
st.title("Document Conversion Tool")
st.sidebar.header("Upload and Process Documents")

# File uploader
uploaded_files = st.sidebar.file_uploader(
    "Upload PDF files", type=["pdf"], accept_multiple_files=True
)

# Display uploaded files
if uploaded_files:
    st.write("Uploaded Files:")
    for uploaded_file in uploaded_files:
        st.write(f"- {uploaded_file.name}")

# Process button
if st.sidebar.button("Start Processing"):
    if not uploaded_files:
        st.error("Please upload at least one file before starting.")
    else:
        # Save uploaded files to the data directory
        data_dir.mkdir(parents=True, exist_ok=True)
        for uploaded_file in uploaded_files:
            file_path = data_dir / uploaded_file.name
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Saved: {file_path}")

        # Process the files
        try:
            convert_docs_to_markdown(
                sources=[str(data_dir / file.name) for file in uploaded_files],
                output_dir=str(output_dir),
            )
            st.success("Document conversion completed successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display processed files
if output_dir.exists():
    st.write("Processed Files:")
    for file in output_dir.glob("*.md"):
        st.write(f"- {file.name}")