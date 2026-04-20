// API Playground Interactive Execution
document.addEventListener('DOMContentLoaded', function() {
  const playgrounds = document.querySelectorAll('.api-playground');
  
  playgrounds.forEach(container => {
    const endpoint = container.dataset.endpoint;
    const method = container.dataset.method;
    const executeBtn = container.querySelector('.execute-btn');
    const responseSection = container.querySelector('.response-section');
    const responseOutput = container.querySelector('.response-output');
    const inputs = container.querySelectorAll('input');
    
    if (executeBtn) {
      executeBtn.addEventListener('click', async () => {
        // Collect parameters
        const params = {};
        inputs.forEach(input => {
          if (input.value) {
            params[input.name] = input.value;
          }
        });
        
        const apiKey = params['api-key'];
        delete params['api-key'];
        
        if (!apiKey) {
          responseSection.style.display = 'block';
          responseOutput.textContent = 'Error: Please provide an API key';
          responseOutput.classList.add('error');
          return;
        }
        
        // Show loading state
        executeBtn.textContent = 'Executing...';
        executeBtn.disabled = true;
        
        try {
          const baseUrl = 'https://sandbox.hyperswitch.io';
          const response = await fetch(baseUrl + endpoint, {
            method: method,
            headers: {
              'Content-Type': 'application/json',
              'api-key': apiKey
            },
            body: JSON.stringify(params)
          });
          
          const data = await response.json();
          
          responseSection.style.display = 'block';
          responseOutput.textContent = JSON.stringify(data, null, 2);
          responseOutput.classList.remove('error');
          
          if (!response.ok) {
            responseOutput.classList.add('error');
          }
        } catch (error) {
          responseSection.style.display = 'block';
          responseOutput.textContent = 'Error: ' + error.message;
          responseOutput.classList.add('error');
        } finally {
          executeBtn.textContent = 'Execute Request';
          executeBtn.disabled = false;
        }
      });
    }
  });
});