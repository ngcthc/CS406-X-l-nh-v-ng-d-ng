import cv2
import os

def remove_parent_bboxes(bboxes):
    # Sắp xếp các bounding box theo diện tích giảm dần
    bboxes.sort(key=lambda x: x[2] * x[3], reverse=True)

    # Danh sách các bounding box không bị chứa bởi bbox mẹ
    cleaned_bboxes = []

    for i, bbox_outer in enumerate(bboxes):
        is_parent = False
        for j, bbox_inner in enumerate(bboxes):
            if i != j:
                # Xác định xem bbox_outer có chứa bbox_inner hay không
                if (bbox_inner[0] >= bbox_outer[0] and bbox_inner[1] >= bbox_outer[1]
                        and bbox_inner[0] + bbox_inner[2] <= bbox_outer[0] + bbox_outer[2]
                        and bbox_inner[1] + bbox_inner[3] <= bbox_outer[1] + bbox_outer[3]):
                    is_parent = True
                    break
        if not is_parent:
            cleaned_bboxes.append(bbox_outer)

    return cleaned_bboxes

def detect_objects_in_image(image, cascade_folder, color, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50), maxSize=(1500, 1500), remove_parent=False, remove_nested=False):
    # Kiểm tra và lấy danh sách các file cascade trong thư mục
    cascade_files = [os.path.join(cascade_folder, file) for file in os.listdir(cascade_folder) if file.endswith('.xml')]

    # Khởi tạo các bộ phân loại cho các file cascade
    classifiers = [cv2.CascadeClassifier(file) for file in cascade_files]

    # Chuyển đổi ảnh sang ảnh xám để tăng hiệu suất
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Phát hiện và vẽ khung xung quanh các đối tượng
    objects = []
    for classifier in classifiers:
        objects.extend(classifier.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize, maxSize=maxSize))

    if remove_parent: objects = remove_parent_bboxes(objects)
    # if remove_nested: objects = remove_nested_bboxes(objects)

    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)

    return image  # Trả về tấm ảnh đã vẽ khung xung quanh các đối tượng phát hiện được

# Đọc ảnh đầu vào
image_path = 'img\\test8.jpg'
img = cv2.imread(image_path)

# Phát hiện khuôn mặt người trong ảnh
img = detect_objects_in_image(img, 'cascades/face', color=(255, 0, 0), minSize=(10, 10), maxSize=(60, 60), remove_parent=True)

# Phát hiện người đi bộ trong ảnh
img = detect_objects_in_image(img, 'cascades/pedestrian', color=(0, 255, 0) , minSize=(50, 50))

# Phát hiện xe hơi trong ảnh
img = detect_objects_in_image(img, 'cascades/car', color=(0, 0, 255), minSize=(90,90))

# Hiển thị ảnh với các khung xung quanh các đối tượng phát hiện được
cv2.imshow('Objects Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()