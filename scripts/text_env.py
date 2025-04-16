import torch
from sentence_transformers import SentenceTransformer

print("PyTorch version:", torch.__version__)
print("Is MPS (Apple GPU) available?", torch.backends.mps.is_available())

model = SentenceTransformer("all-MiniLM-L6-v2")
print("Test embedding:", model.encode("Hello doctor!")[:5])
