import sys
print(f'Python: {sys.version}')
assert sys.version_info >= (3, 11), 'Need Python 3.11+'

try:
    import anthropic
    print('✓ anthropic SDK installed')
except ImportError:
    print('✗ Run: pip install anthropic')

try:
    from sentence_transformers import SentenceTransformer
    print('✓ sentence-transformers installed')
except ImportError:
    print('✗ Run: pip install sentence-transformers')

try:
    import chromadb
    print('✓ chromadb installed')
except ImportError:
    print('✗ Run: pip install chromadb')

import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('ANTHROPIC_API_KEY')
if key and key.startswith('sk-ant'):
    print('✓ API key loaded from .env')
else:
    print('✗ API key missing — check your .env file')

print('\nAll done. Fix any ✗ items before starting Module 1.')