document.getElementById('emailForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const prompt = document.getElementById('userPrompt').value;
    const tone = document.getElementById('toneSelector').value;
  
    const response = await fetch('/generate-email', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, tone }),
    });
  
    const data = await response.json();
    document.getElementById('output').innerHTML = `<p>${data.email}</p>`;
  });
  