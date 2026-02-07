from ultralytics import YOLO

def main():
    model = YOLO("runs/yolo_potholes/weights/best.pt")  # update after training
    model.predict(source=0, show=True, conf=0.25)

if __name__ == "__main__":
    main()
