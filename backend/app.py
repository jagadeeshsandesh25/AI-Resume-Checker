from flask import Flask, request, jsonify, send_from_directory
from utils.resume_parser import extract_text
import ollama
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__, static_folder="../frontend")

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Serve frontend
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# AI Resume Analysis Endpoint
@app.route('/analyze', methods=['POST'])
def analyze_resume():
    # Check if file is present
    if 'resume' not in request.files:
        return jsonify({"success": False, "error": "No resume file uploaded"}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({"success": False, "error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"success": False, "error": "Only PDF or DOCX files allowed"}), 400

    try:
        # Extract full text from resume (PDF or DOCX)
        resume_text = extract_text(file.stream, file.filename)
        if not resume_text or len(resume_text.strip()) < 50:
            return jsonify({"success": False, "error": "Resume is empty or too short to analyze"}), 400

        # Truncate to avoid Ollama context overflow (mistral: ~8k tokens, but stay safe)
        truncated_text = resume_text[:3500]

        # Craft a strong, structured prompt
        prompt = f"""
You are an expert career coach and ATS (Applicant Tracking System) specialist helping job seekers in India.
Analyze the resume below and provide feedback in clear, encouraging, professional English.

Structure your response under these headings:
1. **Overall Score**: (Rate 1–10)
2. **Key Strengths**: (List 2–3)
3. **Areas to Improve**: (e.g., missing contact info, weak action verbs, poor formatting, no metrics)
4. **3 Actionable Suggestions**: (Specific, practical tips)

Keep it concise, human-friendly, and useful for students or early-career professionals.

Resume text:
{truncated_text}
"""

        # Call Ollama (runs locally on your machine)
        response = ollama.chat(
            model='mistral',
            messages=[{'role': 'user', 'content': prompt}],
            options={'temperature': 0.4}  # Less random, more consistent
        )

        feedback = response['message']['content'].strip()
        return jsonify({"success": True, "feedback": feedback})

    except ValueError as ve:
        # Known parsing errors
        return jsonify({"success": False, "error": str(ve)}), 400
    except Exception as e:
        # Unexpected errors (e.g., Ollama not running)
        return jsonify({"success": False, "error": f"Server error: {str(e)}. Is Ollama running?"}), 500

# Run the app
if __name__ == '__main__':
    print("AI Resume Checker is starting...")
    print("Make sure Ollama is running! (Try: ollama run mistral)")
    print("Visit http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)