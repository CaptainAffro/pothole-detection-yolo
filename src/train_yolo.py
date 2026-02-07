from ultralytics import YOLO

def main():
    # Change model to yolov8s.pt if you want better accuracy (slower)
    model = YOLO("yolov8n.pt")

    model.train(
        data="data/potholes.yaml",
        imgsz=640,
        epochs=50,
        batch=16,
        project="runs",
        name="yolo_potholes"
    )

if __name__ == "__main__":
    main()
