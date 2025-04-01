import cv2
import os

def extract_keyframes(video_path, output_folder, num_frames=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_gap = max(total_frames // num_frames, 1)

    keyframes = []
    for i in range(num_frames):
        frame_no = i * frame_gap
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = cap.read()
        if ret:
            resized = cv2.resize(frame, (320, 180))
            frame_path = os.path.join(output_folder, f"keyframe_{i + 1}.jpg")
            cv2.imwrite(frame_path, resized)
            keyframes.append(frame_path)

    cap.release()
    return keyframes
