#!/bin/bash

echo "Starting AI Resume Checker..."

# Check if Ollama is running
if ! pgrep -x "ollama" > /dev/null; then
    echo "  Ollama is not running! Please run 'ollama serve' in another terminal."
    echo " Tip: Open new terminal → type 'ollama run mistral' once to download + start."
    exit 1
fi

# Go to backend folder
cd "$(dirname "$0")/backend" || { echo " backend folder not found!"; exit 1; }

# Check if virtual env exists
if [ ! -d "venv" ]; then
    echo " Creating Python virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

echo " Starting Flask server on http://localhost:5000"
python app.py