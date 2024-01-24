import cv2
import numpy as np
from datetime import datetime

def initialize_background_subtractor():
    return cv2.createBackgroundSubtractorMOG2(50, 16, True)

def configure_camera(cap):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def capture_frame(cap):
    _, frame = cap.read()
    return frame

def apply_background_subtraction(backSub, frame):
    return backSub.apply(frame)

def threshold_mask(fg_mask):
    _, mask_thr = cv2.threshold(fg_mask, 100, 255, 0)
    return mask_thr

def apply_morphology_operations(mask, kernel_open, kernel_close):
    mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
    mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)
    return mask_close

def find_contours(mask):
    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def filter_contours(contours, area_threshold):
    contours_sel = [cnt for cnt in contours if cv2.contourArea(cnt) > area_threshold]
    return contours_sel

def calculate_relative_area(contours_sel, frame):
    total_area = sum(cv2.contourArea(cnt) for cnt in contours_sel)
    rel_area = total_area / (frame.shape[0] * frame.shape[1]) * 100
    return rel_area

def add_timestamp(frame):
    dt = datetime.now()
    dt_image = dt.strftime('%d.%m.%Y %H:%M:%S')
    cv2.putText(frame, dt_image, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (245, 245, 245), 1)

def save_frame(frame):
    dt_file = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    fname_out = 'images/' + dt_file + '.jpg'
    cv2.imwrite(fname_out, frame)


def camera_on():
    backSub = initialize_background_subtractor()
    cap = cv2.VideoCapture(0)

    configure_camera(cap)

    kernel_open = np.ones((5,5), np.uint8)
    kernel_close = np.ones((9,9), np.uint8)
    area_threshold = 100
    motion_threshold = 0.5

    while True:
        frame = capture_frame(cap)
        fg_mask = apply_background_subtraction(backSub, frame)
        mask_thr = threshold_mask(fg_mask)
        mask_close = apply_morphology_operations(mask_thr, kernel_open, kernel_close)

        contours = find_contours(mask_close)
        contours_sel = filter_contours(contours, area_threshold)
        rel_area = calculate_relative_area(contours_sel, frame)

        if rel_area > motion_threshold:
            frame_with_boxes = frame.copy()
            add_timestamp(frame_with_boxes)
            save_frame(frame_with_boxes)

if __name__ == "__main__":
    try:
        camera_on()
    except:
        print('Error')
