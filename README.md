Hand Gesture and Voice Command Recognition System

This project is a real-time interactive system that integrates computer vision and speech recognition to detect hand gestures and respond to voice commands simultaneously. The primary objective is to create a foundation for natural human-computer interaction, where users can control devices or applications through both gestures and spoken words.

The system leverages OpenCV for capturing video input from a webcam and displaying the processed frames. For gesture recognition, it uses MediaPipe Hands, a highly efficient hand-tracking framework that identifies key hand landmarks in real time. By analyzing the relative positions of the thumb and pinky fingertips, the program determines whether the hand is in an open or closed state. The status is then displayed live on the video feed with color-coded labels, offering instant visual feedback.

In parallel, the system employs the SpeechRecognition library to capture and interpret spoken commands via a microphone. Using Google’s speech-to-text API, it listens for specific keywords such as “open hand” or “close hand.” To ensure smooth performance, the speech recognition component is run in a separate thread using Python’s threading module, allowing voice input and video processing to operate simultaneously without delays.

The integration of gestures and voice expands the system’s versatility. While currently configured to display visual and textual responses, the framework can easily be extended to control robotic arms, smart home devices, assistive technologies, or virtual environments. For example, combining hand gestures with voice commands could make the system useful for accessibility applications, particularly for individuals with limited mobility.

Technologies used in this project include Python, OpenCV, MediaPipe, SpeechRecognition, Google Speech API, and multithreading. Together, they form a lightweight yet powerful platform for multimodal interaction.

Overall, this project highlights practical skills in computer vision, voice processing, and concurrent programming, demonstrating how artificial intelligence can bridge human communication and machine control. It serves as a valuable step toward more intuitive and inclusive human-computer interaction systems.
