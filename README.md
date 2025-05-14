# Edge Detection App

This is a Streamlit-based web application that allows users to upload an image and apply edge detection using the Canny algorithm. Users can adjust parameters such as blur radius, threshold value, and edge strength to customize the edge detection process.

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Features

- **Image Upload**: Users can upload images in JPG, JPEG, and PNG formats.
- **Custom Edge Detection**: Adjust the blur radius, threshold value, and edge strength to fine-tune the edge detection results.
- **Real-time Preview**: The application displays both the original and edge-detected images side by side.
- **Reset Functionality**: Users can reset the image upload and parameters to start fresh.

## Getting Started

### Prerequisites

To run this application, you need the following:

- Python 3.6 or higher
- Streamlit
- OpenCV (cv2)
- NumPy

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/edge-detection-app.git
   cd edge-detection-app
   ```

2. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install streamlit opencv-python-headless numpy
   ```

3. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   The application will be available at `http://localhost:8501` in your web browser.

## Usage

1. **Upload an Image**: Click on the "Upload an image" button and select an image file.
2. **Adjust Parameters**: Use the sliders to adjust the blur radius, threshold value, and edge strength.
3. **View Results**: The application will display the original image alongside the edge-detected version in real-time.
4. **Reset**: Click the "Reset" button to clear the current image and parameters.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your changes: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


