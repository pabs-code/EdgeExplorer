import cv2
import streamlit as st
import numpy as np
import base64


class EdgeDetectionApp:
    def __init__(self):
        st.title("Edge Detection App")
        self.image = None
        self.gray_image = None

    def upload_image(self):
        uploaded_file = st.file_uploader(
            "Upload an image", type=["jpg", "jpeg", "png"], key="file_uploader"
        )
        if uploaded_file is not None:
            self.image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
            self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def display_images(self, original_image, edge_image):
        if original_image is not None:
            col1, col2 = st.columns(2)
            with col1:
                self.display_image(original_image, "Original Image")
            with col2:
                if edge_image is not None:
                    self.display_image(edge_image, "Edge Detected Image")

    def display_image(self, image, title="Input Image"):
        if image is not None:
            # Center-align the image
            st.markdown(
                f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{self.encode_image_to_base64(image)}" alt="{title}" width="auto" height="auto"></div>',
                unsafe_allow_html=True,
            )

    def encode_image_to_base64(self, image):
        ret, buffer = cv2.imencode(".png", image)
        return base64.b64encode(buffer).decode("utf-8")

    def edge_detection(self, blur_radius, threshold_value, edge_strength):
        if self.gray_image is not None:
            # Ensure blur radius is odd
            if blur_radius % 2 == 0:
                blur_radius += 1

            # Apply Gaussian Blur
            blurred_image = cv2.GaussianBlur(
                self.gray_image, (blur_radius, blur_radius), 0
            )

            # Apply Canny Edge Detection
            edges = cv2.Canny(blurred_image, threshold_value, edge_strength)
            return edges
        return None

    def main(self):
        self.upload_image()

        if self.image is not None:
            # Sliders for parameters
            blur_radius = st.slider(
                "Blur Radius",
                min_value=3,
                max_value=49,
                value=3,
                step=2,
                key="blur_radius",
            )
            threshold_value = st.slider(
                "Threshold Value",
                min_value=0,
                max_value=255,
                value=100,
                key="threshold_value",
            )
            edge_strength = st.slider(
                "Edge Strength",
                min_value=0,
                max_value=255,
                value=150,
                key="edge_strength",
            )

            # Edge detection in real-time
            edges = self.edge_detection(blur_radius, threshold_value, edge_strength)
            self.display_images(self.image, edges)

            # Reset button
            if st.button("Reset"):
                self.upload_image()
                self.display_images(self.image, None)
        else:
            st.warning("Please upload an image to proceed.")


if __name__ == "__main__":
    app = EdgeDetectionApp()
    app.main()
