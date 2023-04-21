from functools import partial
import cv2

from handpipe import tracking_multi_hand_landmarks
from automouse import move_by_landmark


def recap_video_detect():
    """
    :return: Gerencia a câmera aplicando a marcação e movimento do mouse através de pacotes.
    """
    cap = cv2.VideoCapture(0)

    while True:
        success, image = cap.read()
        move_landmark_recap = partial(move_by_landmark, width_screen=1920, height_screen=1080)
        tracking_multi_hand_landmarks(image=image, fun=move_landmark_recap)
        cv2.imshow("Video Detection Mouse", image)
        cv2.waitKey(1)

        if cv2.getWindowProperty("Video Detection Mouse", cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()
