import cv2

# Load input image
image = cv2.imread("input_image.jpg")
if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert to grayscale for edge detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a window to display the output
cv2.namedWindow("Image")

# Initialize trackbars for parameters
cv2.createTrackbar("Blur Radius", "Image", 3, 49, lambda x: None)
cv2.createTrackbar("Threshold Value", "Image", 50, 255, lambda x: None)
cv2.createTrackbar("Edge Strength", "Image", 150, 255, lambda x: None)

# Main loop to process and display image in real time
while True:
    # Get current values from trackbars
    blur_radius = cv2.getTrackbarPos("Blur Radius", "Image")
    threshold_value = cv2.getTrackbarPos("Threshold Value", "Image")
    edge_strength = cv2.getTrackbarPos("Edge Strength", "Image")

    # Ensure blur radius is odd
    if blur_radius % 2 == 0:
        blur_radius += 1

    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(gray_image, (blur_radius, blur_radius), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred_image, threshold_value, edge_strength)

    # Display the output
    cv2.imshow("Image", edges)

    # Exit on ESC key press
    if cv2.waitKey(1) == 27:
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
