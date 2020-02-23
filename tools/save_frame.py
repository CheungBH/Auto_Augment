import cv2

video_path = ''
cnt = 0
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("multiple/{}.jpg".format(cnt), frame)
    else:
        break