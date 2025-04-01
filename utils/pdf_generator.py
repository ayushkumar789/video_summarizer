from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(transcript, summary, keyframes, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("<b>Video Transcription:</b>", styles["Title"]))
    content.append(Spacer(1, 12))
    content.append(Paragraph(transcript, styles["BodyText"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("<b>Summary:</b>", styles["Title"]))
    content.append(Spacer(1, 12))
    content.append(Paragraph(summary, styles["BodyText"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("<b>Keyframes:</b>", styles["Title"]))
    content.append(Spacer(1, 12))
    for frame in keyframes:
        content.append(Image(frame, width=320, height=180))
        content.append(Spacer(1, 12))

    doc.build(content)
