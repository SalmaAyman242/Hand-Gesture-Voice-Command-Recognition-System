import cv2
import mediapipe as mp
import speech_recognition as sr
import threading

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize Speech Recognition
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Open the camera
cap = cv2.VideoCapture(0)

# Variable to store command
command = ""


def listen_for_commands():
    global command
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print("Listening for command...")
            try:
                audio = recognizer.listen(source, timeout=10)
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                if "open hand" in command.lower():
                  print("Opening hand...")
                elif "close hand" in command.lower():
                  print("Closing hand...")
            except sr.UnknownValueError:
                pass  # Ignore unrecognized commands
            except sr.RequestError as e:
                print(f"Could not request results; {e}")


def is_hand_open(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    distance = ((thumb_tip.x - pinky_tip.x) ** 2 + (thumb_tip.y - pinky_tip.y) ** 2) ** 0.5
    return distance > 0.2  # Adjust this threshold as needed


# Start the command listening thread
command_thread = threading.Thread(target=listen_for_commands, daemon=True)
command_thread.start()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the image horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the RGB frame using MediaPipe Hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks if detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Check if hand is open or closed
            hand_status = "Hand Open" if is_hand_open(hand_landmarks) else "Hand Closed"
            cv2.putText(frame, hand_status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0) if hand_status == "Hand Open" else (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Hand Detection', frame)

    # Check for voice command and act accordingly
    if "open hand" in command.lower():
        print("Opening hand...")
    elif "close hand" in command.lower():
        print("Closing hand...")

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()