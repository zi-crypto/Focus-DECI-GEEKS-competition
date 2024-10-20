# Facial Landmarks Recognition Software

## Project Overview

This project was developed as part of the **DECI GEEKS** competition in Egypt, where we, as a team, implemented a Facial Landmarks Recognition Software aimed at detecting when students are drowsy during classes. The software monitors facial expressions, specifically focusing on the eyes, to determine if they are closing and alerting the student to wake up if needed. This application can help improve attention spans in online and physical classrooms.

## Key Features

- **Real-time Eye Tracking**: Detects facial landmarks using advanced machine learning algorithms.
- **Drowsiness Detection**: Analyzes eye closure and blinking rates to assess when a student is about to fall asleep.
- **Alert System**: Provides an audible alert to wake up the student when drowsiness is detected.
- **Non-Intrusive**: Works seamlessly in the background without disrupting the learning process.

## Technologies Used

Our project uses several advanced technologies and frameworks, including:

- **OpenCV**: For capturing video frames and facial recognition through webcam integration.
- **Dlib**: A key library for detecting facial landmarks (e.g., eyes, nose, mouth) using a pre-trained model.
- **Python**: The core language of the project, which integrates all libraries and controls data flow.
- **Machine Learning**: We utilized machine learning techniques to train and enhance the detection model.
- **TensorFlow**: To power the back-end processes, assisting in deep learning tasks.
- **NumPy**: For efficient numerical computations in data handling.
- **Matplotlib**: For visualizing the behavior of the eye-tracking and detection algorithm.
- **Flask**: Used to create a lightweight web interface for demonstration purposes.
  
## Installation

To get this project running on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/zi-crypto/Focus-DECI-GEEKS-competition.git
    ```
   
2. **Install dependencies** from python file

3. **Run the software**:
    ```bash
    python app.py
    ```

## Usage

1. **Launch the application**: Upon starting, the software will access your webcam to begin live tracking.
2. **Monitor in real-time**: The application will analyze the eye movements in real-time and detect signs of drowsiness.
3. **Receive alerts**: If the eyes are closed for a prolonged period or the system detects abnormal blinking, an audible alarm will be triggered.

## System Architecture

1. **Input Capture**: Webcam captures real-time video feed.
2. **Facial Landmark Detection**: Dlib's model detects 68 facial landmarks.
3. **Eye Aspect Ratio (EAR) Calculation**: Measures the distance between the vertical and horizontal eye landmarks to determine if eyes are closing.
4. **Drowsiness Decision**: If the EAR value falls below a threshold for a set period, the system detects drowsiness.
5. **Alert Trigger**: An alert is issued when the student is about to fall asleep.

## Future Improvements

- **Emotion Detection**: Extend the system to detect student engagement levels based on facial expressions.
- **Mobile Integration**: Develop a mobile version of the software for more portability.
- **AI-Powered Alerts**: Enhance the alert system with personalized responses based on individual behavior patterns.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

- **Ziad Amer** - Lead Developer and Machine Learning Engineer

## Acknowledgments

- We thank the organizers of the **DECI GEEKS** competition for the opportunity to showcase our project.
- Special thanks to all the open-source communities whose libraries made this project possible.
