# %%
import os

def chunk_text(text, source_file, chunk_size=400, overlap=50):
    """
    Split text into overlapping chunks with metadata.
    
    Args:
        text: The full document text
        source_file: Name of the source file (for metadata)
        chunk_size: Size of each chunk in characters
        overlap: How many characters to repeat between chunks
    
    Returns:
        List of dicts, each with 'text' and 'metadata'
    """
    chunks = []
    chunk_index = 0
    start = 0

    while start < len(text):
        # Define end of this chunk
        end = start + chunk_size

        # Extract the chunk text
        chunk_text_content = text[start:end]

        # Only add if chunk has meaningful content
        if chunk_text_content.strip():
            chunks.append({
                "text": chunk_text_content,
                "metadata": {
                    "source_file": source_file,
                    "chunk_index": chunk_index,
                    "char_start": start,
                    "char_end": end
                }
            })
            chunk_index += 1

        # Move forward by chunk_size minus overlap
        start += chunk_size - overlap

    return chunks


def load_and_chunk_folder(folder_path, chunk_size=400, overlap=50):
    """Load all .txt files from a folder and chunk them."""
    all_chunks = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(folder_path, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            
            chunks = chunk_text(text, filename, chunk_size, overlap)
            all_chunks.extend(chunks)
            print(f"  {filename}: {len(chunks)} chunks")

    return all_chunks


# --- Run it ---
print("Loading and chunking documents...\n")
chunks = load_and_chunk_folder("docs", chunk_size=400, overlap=50)

print(f"\nTotal chunks created: {len(chunks)}")

# Verify overlap is working — print chunks 4 and 5
print("\n--- Chunk 4 ---")
print(repr(chunks[4]["text"]))
print("\n--- Chunk 5 ---")
print(repr(chunks[5]["text"]))
print("\n(The end of Chunk 4 should appear at the start of Chunk 5)")

# Print metadata for chunk 0
print("\n--- Metadata example (Chunk 0) ---")
print(chunks[0]["metadata"])