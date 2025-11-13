AI Resume Checker

A lightweight AI-powered web application that analyzes resumes using Flask, Ollama, and the Mistral model.
Upload a PDF resume and instantly receive ATS-style scoring, strengths, weaknesses, and clear improvement suggestions.

Features

AI-driven resume analysis using Mistral (via Ollama)

ATS-style score (0–10)

Strength and weakness extraction

Actionable improvement recommendations

PDF text extraction using PyPDF2

Minimal and clean HTML/CSS/JS frontend

Fast Flask backend

Simple local setup

Project Structure
ai-resume-checker/
│
├── backend/
│   ├── app.py                # Flask API + AI logic
│   ├── requirements.txt      # Backend dependencies
│   └── utils/
│       └── resume_parser.py  # PDF text extractor
│
├── frontend/
│   ├── index.html            # Upload UI
│   ├── style.css             # Styling
│   └── script.js             # Frontend logic
│
├── run.sh                    # Optional one-click run script
├── .gitignore
└── README.md

Tech Stack
Backend

Python 3

Flask

PyPDF2

Ollama + Mistral Model

Frontend

HTML

CSS

JavaScript (Fetch API)

Installation and Setup
1. Clone the Repository
git clone https://github.com/your-username/ai-resume-checker.git
cd ai-resume-checker

2. Install Required Python Packages
pip install -r backend/requirements.txt

3. Install and Run Ollama

Download the Mistral model:

ollama run mistral


Start the Ollama server:

ollama serve


Ensure Ollama is running in the background.

4. Start the Flask Backend
cd backend
python app.py

5. Open the Application

Open your browser and visit:

http://localhost:5000


Upload a PDF resume — analysis will appear instantly.

How It Works

The user uploads a PDF resume.

The backend extracts text using PyPDF2.

The extracted text is sent to the Mistral model via Ollama.

The model returns:

Overall resume score

Key strengths

Weak areas

Improvement suggestions

This pipeline is designed to mimic real ATS behavior and HR-style evaluation.

API Endpoint
POST /analyze

Form Data:

resume → PDF file

Response Example:

{
  "success": true,
  "feedback": "AI generated analysis..."
}

Sample Resume Content (For Testing)
John Doe
Email: john@example.com
Phone: 9876543210

Skills: Python, JavaScript, Leadership

Experience:
- Built a chat app using Flask
- Intern at Tech Startup

Education:
B.Tech in Computer Science, ABC College

Future Enhancements

DOCX file support

Export AI feedback as a downloadable PDF report

Job description matching

Multi-model support (Llama3, Phi3, Gemma, GPT APIs)

Resume formatting analysis

ATS keyword matching

Author

Jagadeesh Goli
AI Developer | Resume Automation | Prompt Engineer
Hindu College of Engineering & Technology

License

MIT License — free for personal and commercial use.
