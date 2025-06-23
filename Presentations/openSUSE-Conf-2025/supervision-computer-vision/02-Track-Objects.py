from supervision.assets import download_assets, VideoAssets
import supervision as sv
import numpy as np
from ultralytics import YOLO

download_assets(VideoAssets.PEOPLE_WALKING)

model = YOLO("yolo11n-seg.pt")
tracker = sv.ByteTrack()
box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()
trace_annotator = sv.TraceAnnotator()
mask_annotator = sv.MaskAnnotator()

def callback(frame: np.ndarray, _: int) -> np.ndarray:
    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)
    detections = detections[detections.class_id == 0]
    detections = tracker.update_with_detections(detections)

    labels = [
        f"#{tracker_id} {results.names[class_id]}"
        for class_id, tracker_id
        in zip(detections.class_id, detections.tracker_id)
    ]

    annotated_frame = box_annotator.annotate(
        frame.copy(), detections=detections)
    annotated_frame = label_annotator.annotate(
        annotated_frame, detections=detections, labels=labels)
    annotated_frame = mask_annotator.annotate(
        annotated_frame, detections=detections)
    return trace_annotator.annotate(
        annotated_frame, detections=detections)

sv.process_video(
    source_path="people-walking.mp4",
    target_path="result.mp4",
    callback=callback
)