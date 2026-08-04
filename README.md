<div align="center">

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/YOLOv8-Ultralytics-7C3AED?style=for-the-badge"/>
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/Status-Complete-22C55E?style=for-the-badge"/>

<br/>

# 🚦 SmartCityEye - AI Powered Traffic Monitoring System

**An AI-powered traffic monitoring application that detects, tracks, and counts vehicles from uploaded videos using YOLOv8, OpenCV, and Flask through a modern glassmorphic web interface.**

</div>

---

## Overview 🔭

SmartCityEye is an end-to-end **computer vision application** designed to automate traffic monitoring from recorded videos. Built using **YOLOv8**, **OpenCV**, and **Flask**, the system performs real-time object detection, assigns persistent IDs to tracked vehicles, prevents duplicate counting, and generates an annotated output video with a live analytics dashboard.

The application features a modern drag-and-drop web interface where users can upload traffic footage, visualize the AI processing pipeline, and download the processed result with bounding boxes, confidence scores, FPS monitoring, and live vehicle statistics.

---

## Features ✨

- **YOLOv8 Object Detection** — accurately detects cars, buses, trucks, motorcycles, and pedestrians
- **Multi-Object Tracking** — assigns persistent IDs to each detected object to prevent duplicate counting
- **Vehicle Analytics Dashboard** — displays live counts for every supported vehicle class along with total detected objects
- **Confidence Score Visualization** — overlays detection confidence and unique tracking IDs on every object
- **Color-Coded Bounding Boxes** — different colors for each object category for improved visualization
- **Drag & Drop Upload Interface** — modern glassmorphic UI supporting quick video uploads
- **AI Processing Pipeline** — interactive loading page visualizing every stage of computer vision inference
- **Processed Video Generation** — exports annotated MP4 videos with all detections rendered frame-by-frame
- **FPS Monitoring** — displays inference performance while processing videos
- **Modern Dark Glass UI** — responsive frontend with animated components and traffic-themed design


# Application Workflow 🖥️ 

```text
Upload Video
      │
      ▼
YOLOv8 Object Detection
      │
      ▼
Multi-Object Tracking
      │
      ▼
Vehicle Counting
      │
      ▼
Dashboard Generation
      │
      ▼
Processed Video
```

---

# Screenshots 📸 

## Home Page
<img width="1470" height="799" alt="Screenshot 2026-08-04 at 2 04 54 PM" src="https://github.com/user-attachments/assets/fc63fa7b-5acf-4abc-9d3b-ee15aac14f5e" />

```
assets/home.png
```

---

## AI Processing 🤖 

<img width="1470" height="799" alt="Screenshot 2026-08-04 at 2 05 52 PM" src="https://github.com/user-attachments/assets/1487e04d-d26e-43f0-9584-162536fdb862" />

```
assets/processing.png
```

---

## 🎥 Final Result

<img width="1470" height="797" alt="Screenshot 2026-08-04 at 2 14 35 PM" src="https://github.com/user-attachments/assets/f896b256-049a-45df-82f5-623b6d41ee8a" />

```
assets/result.png
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Flask | Web Framework |
| YOLOv8 | Object Detection |
| OpenCV | Video Processing |
| Ultralytics | Deep Learning |
| HTML | Frontend |
| CSS | Styling |
| JavaScript | Drag & Drop & UI |

---

# 📂 Project Structure

```text
SmartCityEye
│
├── app.py
├── detector.py
├── counter.py
├── dashboard.py
├── colors.py
├── config.py
├── requirements.txt
│
├── models/
│   └── yolov8s.pt
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── processing.html
│   └── result.html
│
├── uploads/
├── output/
├── videos/
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SmartCityEye.git

cd SmartCityEye
```

---

## Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python3 app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🧠 Detection Pipeline

```text
Input Video

↓

Frame Extraction

↓

YOLOv8 Detection

↓

Object Tracking

↓

Vehicle Counting

↓

Dashboard Overlay

↓

Processed Video
```

---

# 🎯 Detected Classes

| Class | Supported |
|--------|-----------|
| 🚗 Car | ✅ |
| 🚌 Bus | ✅ |
| 🚚 Truck | ✅ |
| 🏍 Motorcycle | ✅ |
| 👤 Person | ✅ |

---

# 📊 Dashboard Displays

- Live Vehicle Counts
- Total Objects
- FPS
- Object IDs
- Confidence Scores

---

# 📈 Performance

- YOLOv8s Object Detection
- Multi-Object Tracking
- CPU Compatible
- Offline Video Processing

---

# 👨‍💻 Author

**SATWIK TELANG**

--- 

<div align="center">

## ⭐ Like this project?

If this project helped or inspired you, please consider giving it a ⭐ on GitHub.

<br>

**Built with ❤️ using Python • Flask • OpenCV • YOLOv8**

</div>
