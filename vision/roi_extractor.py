import cv2 as cv
import mediapipe as mp
from .utils import load_image, resize_image

def detect_face_landmark():
    """
    Detects face landmarks in images
    """
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

    image = load_image("danial-craig.jpg")

    height, width = image.shape[:2]
    rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    with face_mesh as fm:
        result = fm.process(rgb_image)
    if not result.multi_face_landmarks:
        return None

    lm = result.multi_face_landmarks[0].landmark
    print("lm: ", lm)

    for facial_landmarks in result.multi_face_landmarks:
        for i in range(0, 468):
            pt1 = facial_landmarks.landmark[i]
            x = int(pt1.x * width)
            y = int(pt1.y * height)
            cv.circle(image, (x, y), 1, (0, 200, 83), -1)

    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

