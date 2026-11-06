# 🎥 Vision-Based Hand Gesture Media Controller

A high-performance, browser-accelerated computer vision application that enables real-time multimedia playback control using natural hand gestures. By shifting AI inference entirely to the client side, this project achieves sub-15ms tracking latency with zero backend server overhead.

### 🌟 Why This Project Stands Out
* **Zero Backend Latency:** Leverages Google MediaPipe Hands via browser WebGL shaders, delivering smooth 60 FPS performance without sending video frames to a server.
* **Precision Heuristics Engine:** Calculates real-time 3D spatial Euclidean distance between landmark points (Thumb Tip & Index Tip) with debounce filtering for reliable play/pause triggering.
* **Continuous Spatial Control:** Maps vertical Y-axis hand movements directly to dynamic linear volume scaling (0% to 100%).
* **Interactive Visual Feedback:** Renders a real-time 21-point hand landmark skeletal mesh over an HTML5 canvas alongside live telemetry metrics.

### 🛠️ Tech Stack & Architecture
* **Frontend UI:** Streamlit (Python) with custom dark-mode styling
* **Computer Vision & ML:** Google MediaPipe Hands, JavaScript, WebGL, HTML5 Canvas
* **Deployment & CI/CD:** GitHub, Streamlit Cloud

### 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/KuthadiRatnakshaya21/vision-media-controller.git

# Navigate into directory
cd vision-media-controller

# Install requirements & run locally
pip install -r requirements.txt
streamlit run app.py
```
