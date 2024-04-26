import cv2
import numpy as np


def read_video():
    frame_count = 0
    total_sum = None
    cap = cv2.VideoCapture("../files/ants/ants_in_my_telly.mp4")

    fps = cap.get(cv2.CAP_PROP_FPS)

    start_frame_number = int(11 * fps)
    stop_frame_number = int(13.5 * fps)

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)

    while cap.isOpened():
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        subframe = frame[180:715, 885:1270]
        cv2.imshow('frame', subframe)

        if cv2.waitKey(1) == ord('q'):
            break

        if cap.get(cv2.CAP_PROP_POS_FRAMES) >= stop_frame_number:
            break

        gray_frame = cv2.cvtColor(subframe, cv2.COLOR_BGR2GRAY).astype(np.float64)

        # Add the frame to the total sum
        if total_sum is None:
            total_sum = np.zeros_like(gray_frame, dtype=np.float64)
        total_sum += gray_frame

        # Increment frame count
        frame_count += 1

    cap.release()

    avg_frame = (total_sum / frame_count).astype(np.uint8)
    print(avg_frame)

    cv2.imshow('Average', avg_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


read_video()
