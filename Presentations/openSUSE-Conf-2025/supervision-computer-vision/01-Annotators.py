import cv2
from ultralytics import YOLO
from configs import SOURCE_IMAGE_PATH
import supervision as sv

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()
mask_annotator = sv.MaskAnnotator()

model = YOLO("yolo11n-seg.pt")
image = cv2.imread(SOURCE_IMAGE_PATH)
results = model(image)[0]

detections = sv.Detections.from_ultralytics(results)

annotated_images = box_annotator.annotate(scene=image, detections=detections)
annotated_images = label_annotator.annotate(scene=annotated_images, detections=detections)
annotated_images = mask_annotator.annotate(scene=annotated_images, detections=detections)

cv2.imshow("Annotated Image", annotated_images)
cv2.waitKey(0)
cv2.destroyAllWindows()
