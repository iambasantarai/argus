import cv2 as cv
import mediapipe as mp

def init_vision():
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    image = cv.imread("danial-craig.jpg")
    if image is None:
        print("Failed to load image")

    height, width, _ = image.shape
    rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    result = face_mesh.process(rgb_image)
    for facial_landmarks in result.multi_face_landmarks:
        for i in range(0, 468):
            pt1 = facial_landmarks.landmark[i]
            x = int(pt1.x * width)
            y = int(pt1.y * height)
            cv.circle(image, (x, y), 1, (0, 200, 83), -1)

    cv.imshow("Image", image)
    cv.waitKey(0)
