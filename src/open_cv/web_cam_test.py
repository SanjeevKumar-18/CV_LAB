import cv2  # Import OpenCV library for computer vision tasks

# Open connection to the default webcam (0 = primary camera)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    raise RuntimeError("ERROR: Could not open webcam")

# Infinite loop to read frames continuously
while True:
    ret, frame = cap.read()  # ret = success flag, frame = image array

    # If frame was not captured properly, stop execution
    if not ret:
        print("ERROR: Failed to grab frame")
        break

    # Display the current frame in a window
    cv2.imshow("OpenCV Webcam Test", frame)

    # waitKey(1) waits 1 ms and listens for key press
    # If ESC key (27) is pressed, exit loop
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the webcam resource
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
