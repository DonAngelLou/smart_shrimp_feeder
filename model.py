from ultralytics import YOLO  

# Load YOLOv8-Seg model
model = YOLO("yolov8s.pt")  

# Train the model
model.train(
    data="./data.yaml",  
    epochs=50,               # Adjust epochs based on training performance
    imgsz=640,               # Image size
    batch=4,                 # Adjust batch size based on available memory
    workers=2,               # Number of CPU workers for data loading
    device="cpu",            # Change to "cuda" if using a GPU
    hsv_h=0.015,             # HSV color jitter
    hsv_s=0.7,               # Saturation variation
    hsv_v=0.4,               # Brightness variation
    flipud=0.5,              # Flip upside down
    fliplr=0.5,              # Flip left-right
    mosaic=1.0,              # Mosaic augmentation (combining multiple images)
    mixup=0.2,               # Mixup augmentation (overlaying images)              # Apply blur randomly
    perspective=0.0005       # Apply perspective changes
)

# Export the trained model in ONNX format
model.export(format="onnx")
