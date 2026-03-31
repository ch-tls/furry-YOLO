from ultralytics import  YOLO

model = YOLO(r"fur005-960.pt")
model.predict(
    source=r"",
    save=True,
    show=False,
    imgsz=960,
)
