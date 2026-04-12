# SecureMemo

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Kivy](https://img.shields.io/badge/Kivy-5E2B84?style=for-the-badge) ![KivyMD](https://img.shields.io/badge/KivyMD-4CAF50?style=for-the-badge) ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)

> A secure desktop memo application with task management, notes, password protection, and facial recognition login -- built with Kivy and KivyMD for a Material Design experience.

## Features

### Task Management

- **Create Tasks**: Add tasks with title, description, date, time, and priority level
- **Priority System**: 4-level priority slider for task categorization
- **Task Completion**: Mark tasks as done with animated transitions
- **Task History**: View and manage completed tasks separately
- **Bulk Operations**: Delete all ongoing tasks at once
- **Persistent Storage**: Tasks saved to text-based database files

### Notes System

- **Rich Notes**: Create and save text notes
- **Notes Editing**: Edit existing notes
- **Timestamped**: Each note includes creation/modification datetime
- **Card-Based Display**: Material Design cards for note display
- **Delete Notes**: Remove individual notes

### Security

- **Password Protection**: Set and change password to lock the application
- **Facial Recognition Login**: Train the app to recognize your face for biometric authentication
- **Face Data Management**: Collect, update, or remove facial data through settings
- **Secure Unhide**: Password or face verification required to access main content

### Notifications

- **Scheduled Alerts**: Get notified when task deadlines approach
- **Toggle Control**: Enable or disable notifications from settings
- **Background Process**: Notification service runs independently

### Appearance

- **Dark/Light Theme**: Automatic theme switching after 6 PM (configurable)
- **Theme Picker**: MDThemePicker for custom color palette selection
- **Motivational Quotes**: Random inspirational quotes on app startup
- **Animated Transitions**: Smooth slide animations for task/note cards

## Architecture

```
+----------------------------------------------+
|              KivyMD UI Layer                |
|  ScreenManager -> Multiple Screens           |
|  +----------+ +---------+ +--------------+   |
|  | Login    | | Main    | | Settings     |   |
|  | Screen   | | Screen  | | Screen       |   |
|  +----------+ +---------+ +--------------+   |
+----------------------------------------------+
|              Application Logic               |
|  +----------+ +---------+ +--------------+   |
|  | Task Mgr | | Notes   | | Notification |   |
|  | Module   | | Module  | | Module       |   |
|  +----------+ +---------+ +--------------+   |
+----------------------------------------------+
|              Security Layer                  |
|  +------------------+ +------------------+   |
|  | Password Auth    | | Facial Recognize |   |
|  | (text file)      | | (Keras + OpenCV) |   |
|  +------------------+ +------------------+   |
+----------------------------------------------+
|              Storage Layer                   |
|  +-----------+ +-----------+ +------------+  |
|  | tasks_db  | | notes_db  | | themes.txt |  |
|  | finished  | | password  | | quotes     |  |
|  +-----------+ +-----------+ +------------+  |
+----------------------------------------------+
```

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.8+ |
| UI Framework | Kivy, KivyMD |
| Computer Vision | OpenCV (cv2) |
| ML / Face Recognition | Keras, SciPy, NumPy |
| Data Processing | NumPy, Matplotlib |
| Subprocess | subprocess (notification daemon) |

## Security Features

### Password Authentication

- Text file-based password storage (`database_files/password.txt`)
- Password setting, changing, and removal
- Wrong password detection with dialog feedback

### Facial Recognition

- **Data Collection**: Captures 15 facial images via webcam
- **Face Detection**: Haar Cascade frontal face detector
- **Feature Encoding**: Keras model produces embedding vectors
- **Matching**: Cosine distance comparison with threshold (0.225)
- **Liveness**: Continuous verification loop (15 frames, 1.5s intervals)

| Step | Process | Duration |
|------|---------|----------|
| 1 | Face detection via Haar Cascade | Instant |
| 2 | Face crop and resize to 224x224 | Instant |
| 3 | Keras model inference | ~50ms |
| 4 | Cosine distance computation | Instant |
| 5 | Threshold comparison (< 0.225) | Instant |

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Webcam (for facial recognition)

### Installation

```bash
git clone https://github.com/nntrivi2001/SecureMemo.git
cd SecureMemo
pip install kivy kivymd opencv-python keras numpy matplotlib scipy
```

### Usage

```bash
python main.py
```

### First-Time Setup

1. **Set a Password**: On first launch, navigate to settings and set a password
2. **Collect Facial Data** (optional):
   - Go to Settings -> Set Facial Recognition
   - Stand in front of the webcam
   - The app captures 15 face images automatically
3. **Start Using**: Create tasks, notes, and manage your schedule

## Project Structure

```
SecureMemo/
|-- main.py                 # Main application entry point, UI, and core logic
|-- task_add.py             # Task creation popup UI
|-- task_display.py         # Task card display component
|-- task_store.py           # Task database operations (CRUD)
|-- notes_add.py            # Notes creation popup UI
|-- notes_display.py        # Notes card display component
|-- notes_store.py          # Notes database operations (CRUD)
|-- notification.py         # Background notification scheduler
|-- mycamera.py             # Webcam integration utilities
|-- icon.py                 # Application icon handling
|-- get_face_image.py       # Facial data collection helper
|-- database_files/         # Persistent storage
|   |-- tasks_db.txt        # Active tasks database
|   |-- finished_tasks_db.txt   # Completed tasks history
|   |-- password.txt        # Password storage
|   |-- theme.txt           # Theme preference (On/Off)
|   |-- quotes_generator.txt    # Motivational quotes
|-- kv_files/               # Kivy language UI definitions
|   |-- main_screen_kv.kv   # Main screen layout definition
|-- model/                  # ML models
|   |-- inference_model.h5  # Facial recognition Keras model
|-- face_dataset/           # Collected facial images for training
|-- image_files/            # UI image assets
|-- face_dataset.rar        # Archived facial dataset
|-- .gitignore
|-- .gitattributes
|-- README.md
```

## Component Documentation

| Module | Responsibility |
|--------|----------------|
| `main.py` | App entry point, ScreenManager, all business logic, UI bindings |
| `task_add.py` | Popup dialog for creating new tasks (title, desc, date, time, priority) |
| `task_display.py` | MDCard component for displaying tasks with swipe animations |
| `task_store.py` | Text-file-based task persistence (save, load, delete) |
| `notes_add.py` | Popup dialog for creating notes |
| `notes_display.py` | MDCard component for displaying notes |
| `notes_store.py` | Text-file-based notes persistence |
| `notification.py` | Standalone notification scheduler via subprocess |
| `mycamera.py` | Webcam/camera helper utilities |

## Facial Recognition Setup

### Training Your Face

1. Navigate to Settings in the app
2. Click "Set Facial Recognition"
3. The camera will activate and capture 15 images automatically
4. Images are saved to `database_files/facial_dataset/`
5. The Keras model will use these for verification

### Verification Process

1. On app launch, enter password or use facial recognition
2. Click the face verification button
3. Stand in front of the webcam
4. The system captures frames and compares against stored facial data
5. If cosine distance < 0.225, access is granted

### Managing Facial Data

| Action | Steps |
|--------|-------|
| Update face data | Settings -> Change Facial -> Enter password -> Re-capture |
| Remove face data | Settings -> Remove Face -> Enter password -> Confirm |

## Customization

### Theme

- Toggle automatic theme switching in settings
- Use MDThemePicker for manual color selection
- Theme preference saved to `database_files/theme.txt`

### Quotes

- Add your own quotes to `database_files/quotes_generator.txt`
- Format: `quote text;author name`

### Notifications

- Enable/disable in settings
- Notification schedule managed by `notification.py`

This project is open source and available for educational and research purposes.
