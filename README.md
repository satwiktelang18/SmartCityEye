# SmartCityEye - AI Powered Traffic Monitoring & Vehicle Counting using YOLOv8 🚦 

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=28&pause=1000&color=00FF99&center=true&vCenter=true&width=900&lines=AI+Traffic+Monitoring+System;YOLOv8+Object+Detection;Multi-Object+Tracking;Vehicle+Counting+Dashboard;Built+with+Python+%7C+Flask+%7C+OpenCV"/>

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/YOLOv8-Ultralytics-green?style=for-the-badge">
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv">
<img src="https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">

</p>

---

# Overview 📌 

**SmartCityEye** is an AI-powered traffic monitoring system that automatically detects, tracks, and counts vehicles from uploaded traffic videos using **YOLOv8**, **OpenCV**, and **Flask**.

The application assigns a unique ID to every detected object, prevents duplicate counting, displays a real-time dashboard overlay, and generates an annotated output video through a modern web interface.

---

# Features ✨

- 🚗 Vehicle Detection using YOLOv8
- 🎯 Multi-Object Tracking with Unique IDs
- 📊 Live Vehicle Counting Dashboard
- 👤 Person Detection
- 🚚 Truck Detection
- 🚌 Bus Detection
- 🏍 Motorcycle Detection
- 🎥 Processed Video Generation
- 📂 Drag & Drop Video Upload
- 🌐 Modern Flask Web Interface
- 📈 FPS Monitoring
- 🎨 Color-Coded Bounding Boxes

---

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

<img width="1470" height="791" alt="Screenshot 2026-08-04 at 2 08 48 PM" src="https://github.com/user-attachments/assets/cf4ce3f9-2fe0-42ad-a7a8-a4584f33f77f" />

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

If you found this project useful, consider giving it a ⭐ on GitHub!

<p align="center">

Made with ❤️ using Python, Flask, OpenCV & YOLOv8

</p>
