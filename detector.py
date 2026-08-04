import os
import time
import cv2
from ultralytics import YOLO

import config
from counter import ObjectCounter
from dashboard import draw_dashboard
from colors import COLORS


# ----------------------------
# Load Model
# ----------------------------
model = YOLO("models/yolov8s.pt")

counter = ObjectCounter()

# ----------------------------
# Open Video
# ----------------------------
cap = cv2.VideoCapture(config.VIDEO_PATH)

if not cap.isOpened():
    print("Error opening video.")
    exit()

# ----------------------------
# Output Folder
# ----------------------------
os.makedirs("output", exist_ok=True)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_fps = cap.get(cv2.CAP_PROP_FPS)

if video_fps == 0:
    video_fps = 30

writer = cv2.VideoWriter(
    "output/processed_video.mp4",
    cv2.VideoWriter_fourcc(*"avc1"),
    video_fps,
    (width, height)
)

prev_time = time.time()

# ----------------------------
# Main Loop
# ----------------------------
while True:

    success, frame = cap.read()

    if not success:
        break

    results = model.track(
    frame,
    persist=True,
    conf=0.15,
    iou=0.45,
    imgsz = 640,
    verbose=False
)

    annotated = frame.copy()

    boxes = results[0].boxes

    if boxes is not None and boxes.id is not None:

        ids = boxes.id.int().cpu().tolist()
        classes = boxes.cls.int().cpu().tolist()
        confidences = boxes.conf.cpu().tolist()
        coordinates = boxes.xyxy.int().cpu().tolist()

        for object_id, class_id, confidence, box in zip(
            ids,
            classes,
            confidences,
            coordinates
        ):

            class_name = model.names[class_id]

            if class_name not in config.ALLOWED_CLASSES:
                continue

            counter.add(object_id, class_name)

            x1, y1, x2, y2 = box

            color = COLORS.get(class_name, (255, 255, 255))

            # Bounding Box
            cv2.rectangle(
                annotated,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            # Label
            label = f"{class_name.upper()} #{object_id} ({confidence:.2f})"

            cv2.putText(
                annotated,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                color,
                2
            )

    # ----------------------------
    # FPS
    # ----------------------------
    current_time = time.time()

    fps = 1 / max(current_time - prev_time, 0.0001)

    prev_time = current_time

    # ----------------------------
    # Dashboard
    # ----------------------------
    draw_dashboard(
        annotated,
        counter.counts(),
        counter.total(),
        fps
    )

    # ----------------------------
    # Save Frame
    # ----------------------------
    writer.write(annotated)

    # ----------------------------
    # Show Frame
    # ----------------------------

    # Preview disabled when running from Flask

# ----------------------------
# Cleanup
# ----------------------------
cap.release()
writer.release()

print("\nProcessing Completed!")

print("Saved to : output/processed_video.mp4")

# Tell Flask we're done
with open("output/status.txt", "w") as f:
    f.write("done")