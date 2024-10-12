import streamlit as st
from PIL import Image

from utils.is_image_url import is_image_url
from utils.extract_color_palette import extract_color_palette
from utils.open_image_url import open_image_url
from utils.plot_color_palette import plot_color_palette
from utils.display_color_info import display_color_info

st.title("Color Pattern Recognition in HCI")
st.sidebar.title("Input Options")
input_option = st.sidebar.selectbox(
    "Choose an input method", ("Image URL", "Upload Image")
)

if input_option == "Image URL":
    st.sidebar.write("Provide the URL for two images to compare")
    url1 = st.sidebar.text_input("Image URL 1")
    url2 = st.sidebar.text_input("Image URL 2")

    if st.sidebar.button("Extract and Compare"):
        if url1 and url2:
            is_image1_a_image = is_image_url(url1)
            is_image2_a_image = is_image_url(url2)

            print(is_image1_a_image, is_image2_a_image)

            if is_image1_a_image and is_image1_a_image:
                image1 = open_image_url(url1)
                image2 = open_image_url(url2)

                st.image(
                    image1,
                    caption="Image 1",
                    use_column_width=True,
                )
                st.image(
                    image2,
                    caption="Image 2",
                    use_column_width=True,
                )

                colors1 = extract_color_palette(image1)
                colors2 = extract_color_palette(image2)

                plot_color_palette(colors1, "Color Palette from Website 1")
                plot_color_palette(colors2, "Color Palette from Website 2")

                display_color_info(colors1)
                display_color_info(colors2)
            else:
                st.error("Unable to extract images from one or both images.")
        else:
            st.warning("Please enter both website URLs.")
elif input_option == "Upload Image":
    st.sidebar.write("Upload images of the websites to compare")
    uploaded_file1 = st.sidebar.file_uploader(
        "Upload Image 1", type=["jpg", "png", "jpeg"]
    )
    uploaded_file2 = st.sidebar.file_uploader(
        "Upload Image 2", type=["jpg", "png", "jpeg"]
    )

    if st.sidebar.button("Compare Uploaded Images"):
        if uploaded_file1 and uploaded_file2:
            image1 = Image.open(uploaded_file1)
            image2 = Image.open(uploaded_file2)

            st.image(image1, caption="Uploaded Image 1", use_column_width=True)
            st.image(image2, caption="Uploaded Image 2", use_column_width=True)

            colors1 = extract_color_palette(image1)
            colors2 = extract_color_palette(image2)

            plot_color_palette(colors1, "Color Palette from Image 1")
            plot_color_palette(colors2, "Color Palette from Image 2")

            display_color_info(colors1)
            display_color_info(colors2)
        else:
            st.warning("Please upload both images.")
