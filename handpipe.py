from numpy import ndarray
import cv2
import mediapipe as mp


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


def tracking_multi_hand_landmarks(image: ndarray, fun: callable):
    """
    :param image: Imagem capturada pelo opencv.
    :param fun: função aplicada quando o dedo indicador é detectado na tela.
    :return: Desenha a marcação na imagem destacando quando uma mão humana é detectada.
    """
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 8:
                    fun(lm=lm)
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

                mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)