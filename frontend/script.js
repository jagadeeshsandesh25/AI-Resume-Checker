async function analyzeResume() {
  const fileInput = document.getElementById('resumeInput');
  const file = fileInput.files[0];
  const feedbackDiv = document.getElementById('feedback');
  const errorDiv = document.getElementById('error');
  const loadingDiv = document.getElementById('loading');

  if (!file) {
    showError("Please select a PDF resume.");
    return;
  }

  // Reset UI
  feedbackDiv.classList.add('hidden');
  errorDiv.classList.add('hidden');
  loadingDiv.classList.remove('hidden');

  const formData = new FormData();
  formData.append('resume', file);

  try {
    const response = await fetch('/analyze', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();

    loadingDiv.classList.add('hidden');

    if (data.success) {
      feedbackDiv.textContent = data.feedback;
      feedbackDiv.classList.remove('hidden');
    } else {
      showError(data.error || 'Something went wrong.');
    }
  } catch (err) {
    loadingDiv.classList.add('hidden');
    showError('Network error. Is the backend running?');
  }
}

function showError(msg) {
  const errorDiv = document.getElementById('error');
  errorDiv.textContent = msg;
  errorDiv.classList.remove('hidden');
}