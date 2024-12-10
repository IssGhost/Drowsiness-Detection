import cv2

cap = cv2.VideoCapture(0)  # Adjust index as needed
if not cap.isOpened():
    print("Cannot access the camera")
else:
    print("Camera accessed successfully")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    cv2.imshow('Test Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
