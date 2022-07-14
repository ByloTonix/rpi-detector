import cv2
import numpy as np
from datetime import datetime

def camera_on():
    backSub = cv2.createBackgroundSubtractorMOG2(50, 16, True)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        _, frame = cap.read()

        fg_mask = backSub.apply(frame)

        _, mask_thr = cv2.threshold(fg_mask, 100, 255, 0) 
        
        kernel_open = np.ones((5,5), np.uint8)
        mask_open = cv2.morphologyEx(mask_thr, cv2.MORPH_OPEN, kernel_open)

        kernel_close = np.ones((9,9), np.uint8)
        mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)
        
        _, contours, _ = cv2.findContours(mask_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        area_threshold = 100
        contours_sel = [cnt for cnt in contours if cv2.contourArea(cnt) > area_threshold]

        total_area = 0
        for cnt in contours_sel:
            total_area += cv2.contourArea(cnt)
        rel_area = total_area / (frame.shape[0] * frame.shape[1]) * 100

        motion_threshold = 0.5
        if rel_area > motion_threshold:

            frame_boxes = frame.copy()

            dt = datetime.now()
            dt_image = dt.strftime('%d.%m.%Y %H:%M:%S')
            cv2.putText(frame_boxes, dt_image, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (245, 245, 245), 1)

            dt_file = dt.strftime('%d-%m-%Y_%H-%M-%S')
            fname_out = 'images/' + dt_file + '.jpg'
            cv2.imwrite(fname_out, frame_boxes)

if __name__ == "__main__":
    try:
        camera_on()
    except:
        print('Error')