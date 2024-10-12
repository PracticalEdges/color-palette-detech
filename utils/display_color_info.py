from utils.rgb_to_hex import rgb_to_hex
import streamlit as st

def display_color_info(color_percentages: list[float]) -> None:
    try:
        st.subheader("Color Information")
        color_labels = ["Primary Color", "Secondary Color", "Tertiary Color"]

        print(color_percentages)

        for i in range(min(3, len(color_percentages))):
            color, percentage = color_percentages[i]
            hex_color = rgb_to_hex(color)
            st.write(
                f"{color_labels[i]}: RGB {tuple(color)} - Hex {hex_color} - {percentage:.2f}%"
            )
    except Exception as e:
        print(f"Error displaying color information: {e}")