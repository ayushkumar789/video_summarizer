from flask import Blueprint, request, jsonify, render_template
from services.audio_processing import extract_audio
from services.summarization import summarize_text
from services.keyframe_extraction import extract_keyframes
from utils.pdf_generator import generate_pdf
from utils.word_generator import generate_word
import os

api = Blueprint("api", __name__)
UPLOAD_FOLDER = os.path.join("static", "uploads")
KEYFRAME_FOLDER = os.path.join(UPLOAD_FOLDER, "keyframes")

def process_and_export(filename):
    video_path = os.path.join(UPLOAD_FOLDER, filename)
    transcript, _ = extract_audio(video_path)
    summary = summarize_text(transcript)
    keyframes = extract_keyframes(video_path, KEYFRAME_FOLDER)
    keyframes = [f"uploads/keyframes/{os.path.basename(k)}" for k in keyframes]

    pdf_path = os.path.join(UPLOAD_FOLDER, "summary_report.pdf")
    word_path = os.path.join(UPLOAD_FOLDER, "summary_report.docx")

    generate_pdf(transcript, summary, [os.path.join("static", k) for k in keyframes], pdf_path)
    generate_word(transcript, summary, keyframes, word_path)

    return transcript, summary, keyframes, pdf_path, word_path

@api.route("/")
def index():
    return render_template("index.html")

@api.route("/upload", methods=["POST"])
def upload_video():
    if "video" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    video = request.files["video"]
    if video.filename == "":
        return jsonify({"error": "No selected file"}), 400

    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    return jsonify({"message": "File uploaded successfully", "path": video_path})

@api.route("/process/<filename>", methods=["GET"])
def process_video(filename):
    transcript, summary, keyframes, _, _ = process_and_export(filename)
    return render_template("result.html", transcript=transcript, summary=summary, keyframes=keyframes, filename=filename)

@api.route("/download/<filename>", methods=["GET"])
def download_results(filename):
    _, _, _, pdf_path, word_path = process_and_export(filename)
    return render_template("download.html", pdf_path=f"/{pdf_path}", word_path=f"/{word_path}")
