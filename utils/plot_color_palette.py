import matplotlib.pyplot as plt
import streamlit as st

def plot_color_palette(color_percentages: list[float], title: str) -> None:
    try:
        colors = [color[0] for color in color_percentages]
        percentages = [color[1] for color in color_percentages]

        fig, ax = plt.subplots(1, figsize=(8, 2), subplot_kw=dict(xticks=[], yticks=[]))
        ax.imshow([colors], extent=[0, len(colors), 0, 1])
        ax.set_title(title)

        for i, (color, percentage) in enumerate(zip(colors, percentages)):
            ax.text(i, 1.5, f"{percentage:.2f}%", color="black", ha="center")

        st.pyplot(fig)
    except Exception as e:
        print(f"Error plotting color palette: {e}")