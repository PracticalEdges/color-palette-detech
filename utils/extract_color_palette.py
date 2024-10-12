from sklearn.cluster import KMeans
from collections import Counter
import numpy as np
from PIL import Image
import streamlit as st

def extract_color_palette(image: Image, num_colors: int = 5) -> list[tuple[any, float]]:
    try:
        image = image.resize((200, 200))
        image_array = np.array(image)

        if image_array.shape[-1] != 3:
            st.error("Image does not have 3 channels (RGB)")
            raise ValueError("Image does not have 3 channels (RGB)")

        image_array = image_array.reshape((-1, 3))
        kmeans = KMeans(n_clusters=num_colors)
        kmeans.fit(image_array)
        colors = kmeans.cluster_centers_.astype(int)
        counts = Counter(kmeans.labels_)
        total_count = sum(counts.values())
        color_percentages = [
            (colors[i], counts[i] / total_count * 100) for i in range(num_colors)
        ]
        color_percentages.sort(key=lambda x: x[1], reverse=True)
        return color_percentages
    except Exception as e:
        print(f"Error extracting color palette: {e}")
        return None
