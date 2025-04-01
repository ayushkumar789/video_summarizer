# 🎮 AI Video Summarizer

An AI-powered tool that takes long videos and generates **smart, readable summaries** using Whisper, Cohere AI, OpenCV, and MongoDB.

> 🔥 Developed by **Ayush Kumar Panigrahi**

---

## 🚀 Features

- 🎤 Convert speech to text using **Whisper (GPU-accelerated)**
- 🧠 Generate summary using **Cohere AI**
- 🎞️ Extract video **keyframes using OpenCV**
- 📄 Export **PDF & Word** with keyframes and transcript
- 📊 Store video summary and metadata in **MongoDB Atlas**
- 🌀 **Lottie animation**, waveform visualizer, toast alerts
- 🌐 Built using **Flask**, **TailwindCSS**, **Alpine.js**

---

## 📁 Folder Structure

```
video_summarizer/
├── app.py
├── config/
│   └── db.py
├── routes/
│   └── api.py
├── services/
│   ├── audio_processing.py
│   ├── keyframe_extraction.py
│   └── summarization.py
├── utils/
│   ├── pdf_generator.py
│   └── word_generator.py
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   ├── animations/loading.json
│   └── uploads/  # Videos + Keyframes
├── templates/
│   ├── index.html
│   ├── result.html
│   └── download.html
├── .env
└── requirements.txt
```

---

## 🛠️ Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ayushkumar789/video_summarizer.git
cd video_summarizer
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
# Activate it:
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install manually:

```bash
pip install flask python-dotenv pymongo cohere moviepy opencv-python
pip install openai-whisper ffmpeg-python python-docx reportlab
```

---

### 4️⃣ Create a `.env` File

Inside the root project folder:

```env
COHERE_API_KEY=your_cohere_api_key
MONGODB_URI=your_mongodb_connection_string
```

---

## 🔄 Run the App

```bash
python app.py
```

Now open your browser and go to:  
📍 `http://127.0.0.1:5000/`

---

## 📀 MongoDB Atlas Setup

1. Go to [MongoDB Atlas](https://cloud.mongodb.com/)
2. Create a **Free Shared Cluster**
3. Add **your IP to Network Access**
4. Create a **Database User**
5. Copy your **Connection String**
6. Paste it in `.env` as `MONGODB_URI`

---

## 📂 What Gets Stored in MongoDB?

Each summary stores:

- 🎮 Filename
- 📄 Transcript
- 🧠 Summary
- 🞼 Keyframe filenames

> Videos are **not stored**, only metadata.

---

## ✨ UI Features

- ✅ Lottie animation during processing
- ✅ Toast alerts using Alpine.js
- ✅ Waveform visualizer for better feedback
- ✅ Clean Tailwind-based layout

---

## 📤 Export Options

- `summary_report.pdf`
- `summary_report.docx`

---

## 💡 Future Improvements

- 🧠 Add summarizer history viewer
- 🔐 User authentication
- 📱 Turn into Android/iOS app
- ☁️ Deploy to Render, Railway, or Vercel

---

## 👨‍💻 Author

**Ayush Kumar Panigrahi**  
📧 [ayushkumarpanigrahi.info](https://ayushkumarpanigrahi.info)

---

## ⭐ Show Your Support

If you like this project:

- ⭐ Star the repo
- 🍟 Fork it
- 💬 Share with your friends
