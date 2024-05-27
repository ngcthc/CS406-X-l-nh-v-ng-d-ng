import streamlit as st
import numpy as np
from ultralytics import YOLO
import cv2

model = YOLO('best.pt')  # Thay đổi đường dẫn file weight tương ứng

def draw_boxes_on_image(image, model):
    mapping = ['apple', 'orange', 'lemon', 
           'avocado', 'cherry', 'coconut', 
           'banana', 'watermelon', 'pineapple', 
           'kiwi', 'tomato', 'mango']
    predictions = model.predict(source=image)
    boxes = predictions[0].boxes.xyxy
    scores = predictions[0].boxes.conf
    labels = predictions[0].boxes.cls
    # Vẽ bounding box lên ảnh
    for box, score, label in zip(boxes, scores, labels):
        x1, y1, x2, y2 = box
        xmin, ymin, xmax, ymax = int(x1), int(y1), int(x2), int(y2)
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)
        text = f'{mapping[int(label)]}: {score:.2f}'
        cv2.putText(image, text, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    
    return image

def main():
    st.title('Demo Fruit Detection')
    
    uploaded_file = st.file_uploader("Chọn ảnh", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Đọc file ảnh từ file_uploader
        image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # Hiển thị ảnh gốc
        st.subheader("Ảnh gốc")
        st.image(image, channels="BGR")

        # Xử lý ảnh
        # processed_image = process_image(image)
        processed_image = draw_boxes_on_image(image, model)

        # Hiển thị ảnh sau khi xử lý
        st.subheader("Ảnh sau khi xử lý")
        st.image(processed_image, channels="BGR")

if __name__ == "__main__":
    main()