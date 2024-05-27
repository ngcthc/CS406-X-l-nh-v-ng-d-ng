DANH SÁCH THÀNH VIÊN NHÓM
Nguyễn Ngọc Thức - 21521506
Lê Châu Giang - 21520213
Phạm Thanh Lâm - 21520055
Đoàn Lê Tuấn Thành - 21521438

----

LINK
Link google colab:
https://colab.research.google.com/drive/1FuLEHk85Mmd53xG767vcfs3nNvjFeUXf?usp=sharing
Link data gốc:
https://www.kaggle.com/datasets/aelchimminut/fruits262
Link data nhóm dùng:
https://drive.google.com/file/d/1H0a3_s3tsd9tpWkiR33mGn7O0hbZTMTF/view?usp=sharing
Link download file yolov8s.pt: 
https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt

----

HƯỚNG DẪN BUILD VÀ THỰC THI CODE
Bước 1: Train model yolov8 phát hiện trái cây
    1.1. Tải file yolov8s.pt tại địa chỉ được cung cấp bên trên 
    1.2. Giải nén file dataset.zip ở cùng cấp với file notebook train.ipynb, cấu trúc thư mục như sau:
            ./
            |_dataset
            |    |_train
            |    |_val
            |    |_test
            |_train.ipynb
            |_yolov8s.pt
    1.3. Chạy file notebook
    1.4. Sau khi train xong thì file model sẽ được lưu tại đường dẫn runs\detect\train\weights\best.pt 
    1.5. Copy file best.pt sang thư mục hiện hành
Lưu ý: file train.ipynb được cung cấp dùng để train trên local, bạn có thể tùy chỉnh để train 
trên google colab hoặc kaggle để có tốc độ nhanh hơn

Bước 2: Dùng model đã được train để chạy web demo
    2.1. Copy file best.pt đã được train ở bước trên cùng cấp với file index.py, cấu trúc thư mục như sau: 
            ./
            |_best.pt
            |_index.py
    2.2. Cài thư viện streamlit bằng câu lệnh: pip install streamlit
    2.3. Chạy file index.py
    2.4. Sẽ có một câu lệnh được yêu cầu chạy hiện ra ở terminal 
        Ví dụ trên máy mình là câu lệnh: streamlit run c:\Users\Kaisaac\Documents\VSCode\CS406.O11\project\index.py 
    2.5. Chạy lệnh trên, sau đó server web sẽ được khởi động
    2.6. Lúc này web đã được chạy trên trình duyệt