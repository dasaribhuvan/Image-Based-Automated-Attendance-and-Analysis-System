import os
import pickle
import numpy as np

EMBED_DIR = "embeddings"
LEARNING_THRESHOLD = 0.70
MAX_EMBEDDINGS = 50   # prevent unlimited growth

def incremental_update(student_id, new_embedding, similarity_score):
    """
    Update stored embeddings only if confidence is high
    """
    if similarity_score < LEARNING_THRESHOLD:
        print("⚠ Confidence too low — skipping incremental update")
        return

    file_path = os.path.join(EMBED_DIR, f"{student_id}.pkl")

    if not os.path.exists(file_path):
        print("❌ Student embedding file not found")
        return

    with open(file_path, "rb") as f:
        embeddings = pickle.load(f)

    embeddings = embeddings.reshape(embeddings.shape[0], -1)

    # Append new embedding
    embeddings = np.vstack([embeddings, new_embedding.reshape(1, -1)])

    # Keep only latest embeddings
    if len(embeddings) > MAX_EMBEDDINGS:
        embeddings = embeddings[-MAX_EMBEDDINGS:]

    with open(file_path, "wb") as f:
        pickle.dump(embeddings, f)

    print(f"🔁 Incremental learning applied for {student_id}")
