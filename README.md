# AI Resume Checker

An AI-powered web application that analyzes resumes using **Flask + Ollama + Mistral Model**.  
Upload your PDF resume and get instant, ATS-style feedback including strengths, weaknesses, and actionable improvements.

---

## Features
- AI-based resume analysis using Mistral (via Ollama)
- ATS-style scoring (score out of 10)
- Strengths and weaknesses extraction
- 3 direct improvement suggestions
- PDF text extraction (PyPDF2)
- Lightweight frontend (HTML + CSS + JS)
- Fast Flask backend
- Extremely easy to run locally

---

## Project Structure

ai-resume-checker/
│
├── backend/
│ ├── app.py # Flask API + AI processing
│ ├── requirements.txt # Backend dependencies
│ └── utils/
│ └── resume_parser.py # PDF text extractor
│
├── frontend/
│ ├── index.html # UI for uploading resumes
│ ├── style.css # Clean styling
│ └── script.js # Frontend logic
│
├── run.sh # Optional one-click run script
├── .gitignore
└── README.md


---

## Tech Stack
**Backend**
- Python 3  
- Flask 3  
- PyPDF2  
- Ollama (Mistral Model)

**Frontend**
- HTML  
- CSS  
- JavaScript (Fetch API)

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-resume-checker.git
cd ai-resume-checker

2. Install Python Dependencies

pip install -r backend/requirements.txt

3. Install & Run Ollama

Download and run the Mistral model:

ollama run mistral

Start Ollama server:

ollama serve

Note: Ollama must be running in the background.
4. Start the Backend (Flask)

cd backend
python app.py

5. Open The App

Open your browser at:
http://localhost:5000


Upload your PDF resume → AI analysis appears instantly.
How Resume Analysis Works

    User uploads a PDF file

    Backend extracts text using PyPDF2

    Text is sent to Mistral model (via Ollama)

    AI returns:

        Overall Resume Score

        Key Strengths

        Weak Areas

        Actionable Improvement Tips

Designed to mimic real ATS + HR expert feedback.
API Endpoint

POST /analyze

Form Data

    resume → PDF file

Response

{
  "success": true,
  "feedback": "AI generated analysis..."
}

Sample Resume Content (for testing)

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

    DOCX support

    Downloadable PDF report

    Job description matcher

    Multi-model support (Llama3, Phi3, Gemma, GPT APIs)

    Resume formatting suggestions

    ATS keyword matching

Author

Jagadeesh Goli
AI Developer | Resume Automation | Prompt Engineer
Hindu College of Engineering & Technology
License

MIT License — Free for personal & commercial use.


---

You can copy-paste this directly into your GitHub repo’s `README.md` — it’ll render perfectly in Markdown preview.

