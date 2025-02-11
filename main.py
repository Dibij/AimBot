import numpy as np
import pyautogui
import win32api, win32con, win32gui
import cv2 as cv
import math 
import time

config_file = r'Aimbot\yolov3.cfg'
weight_file = r'Aimbot\yolov3.weights'

net = cv.dnn.readNetFromDarknet(config_file, weight_file)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

ln = net.getLayerNames()
ln = [ln[i - 1] for i in net.getUnconnectedOutLayers().flatten()]  

hwnd = win32gui.FindWindow(None, "BlueStacks App Player")
rect = win32gui.GetWindowRect(hwnd)
region = rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]

size_scale = 2
aimbot_active = False  # ✅ Aimbot starts OFF

while True:
    # ✅ Press "H" once → Toggle Aimbot ON/OFF
    if win32api.GetAsyncKeyState(ord('H')) & 1:
        aimbot_active = not aimbot_active  # Toggle mode
        print(f"Aimbot {'Activated' if aimbot_active else 'Deactivated'}")

    if not aimbot_active:
        continue  # Skip detection if aimbot is OFF

    frame = np.array(pyautogui.screenshot(region=region))
    frame_height, frame_width = frame.shape[:2]

    blob = cv.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_outputs = net.forward(ln)

    boxes = []
    confidences = []

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            if len(scores) > 0:
                class_id = np.argmax(scores)
                confidence = scores[class_id] if class_id < len(scores) else 0  
            else:
                confidence = 0

            if confidence > 0.7 and class_id == 0:
                box = detection[:4] * np.array([frame_width, frame_height, frame_width, frame_height])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))  

    indices = cv.dnn.NMSBoxes(boxes, confidences, 0.7, 0.6)  

    # ✅ If Aimbot is ON → Auto aim & shoot
    if len(indices) > 0:
        print(f"Detected: {len(indices)}")
        min_dist = 99999  
        min_at = 0
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

            dist = math.sqrt(math.pow(frame_width / 2 - (x + w / 2), 2) + math.pow(frame_height / 2 - (y + h / 2), 2))  
            if dist < min_dist:
                min_dist = dist
                min_at = i

        # Distance of the closest from crosshair
        x = int(boxes[min_at][0] + boxes[min_at][2] / 2 - frame_width / 2)
        y = int(boxes[min_at][1] + boxes[min_at][3] / 2 - frame_height / 2) - boxes[min_at][3] * 0.5  

        # Move mouse and shoot
        scale = 1.7
        x = int(x * scale)
        y = int(y * scale)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = cv.resize(frame, (frame.shape[1] // size_scale, frame.shape[0] // size_scale))
    cv.imshow("frame", frame)

    cv.waitKey(16)  # ✅ 60 FPS cap
