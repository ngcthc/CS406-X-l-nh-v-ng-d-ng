import cv2
import os

# Khởi tạo đường dẫn cho các file cascade
cascade_paths = {}
for object in os.listdir('cascades'):
    if os.path.isdir(os.path.join('cascades', object)):
        cascade_paths[object] = []
        for cascade in os.listdir(os.path.join('cascades', object)):
            cascade_paths[object].append(os.path.join('cascades', object, cascade))

# Khởi tạo bộ phân loại từ các file cascade
cascades = {obj: [cv2.CascadeClassifier(path) for path in paths] for obj, paths in cascade_paths.items()}

# Khởi tạo webcam (để sử dụng video từ webcam)
cap = cv2.VideoCapture('video/jam1.avi')

while True:
    # Đọc video từ webcam
    ret, frame = cap.read()
    if not ret: break

    # Chuyển đổi ảnh sang ảnh xám để tăng hiệu suất cho việc phát hiện
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Phát hiện các đối tượng trong video với từng bộ phân loại
    for obj, cascades_list in cascades.items():
        for cascade in cascades_list:
            objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Vẽ hình chữ nhật xung quanh các đối tượng được phát hiện
            for (x, y, w, h) in objects:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, obj, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Hiển thị video với các bounding box đã vẽ
    cv2.imshow('Video', frame)

    # Thoát vòng lặp nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()