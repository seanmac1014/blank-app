import streamlit as st
from PIL import Image
import math

# Function to calculate the angle between two lines
def calculate_angle(x1, y1, x2, y2, x3, y3):
    angle1 = math.atan2(y2 - y1, x2 - x1)
    angle2 = math.atan2(y3 - y1, x3 - x1)
    angle_deg = (math.degrees(angle2 - angle1)) % 360
    return angle_deg if angle_deg <= 180 else 360 - angle_deg

# Streamlit app interface
st.title('Virtual Goniometer')

# Image uploader
uploaded_image = st.file_uploader("Upload an image for joint ROM measurement", type=["jpg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # User inputs for line coordinates (could be sliders or text inputs)
    st.write("Enter the coordinates for the joint angle measurement")
    
    # Example using sliders for coordinates
    x1 = st.slider("x1", 0, img.size[0], 100)
    y1 = st.slider("y1", 0, img.size[1], 100)
    x2 = st.slider("x2", 0, img.size[0], 200)
    y2 = st.slider("y2", 0, img.size[1], 200)
    x3 = st.slider("x3", 0, img.size[0], 300)
    y3 = st.slider("y3", 0, img.size[1], 300)

    # Calculate and display the angle
    angle = calculate_angle(x1, y1, x2, y2, x3, y3)
    st.write(f"Calculated Angle: {angle} degrees")
