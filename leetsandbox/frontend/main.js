document.addEventListener('DOMContentLoaded', () => {
    // Dynamically set API URL based on hostname
    const isLocal = window.location.hostname === '127.0.0.1' || window.location.hostname === 'localhost';
    const API_BASE_URL = isLocal ? 'http://127.0.0.1:8001' : 'https://leetsandbox-api.onrender.com'; // <-- IMPORTANT

    const problemTitle = document.getElementById('problem-title');
    const inputFields = document.getElementById('input-fields');
    const constraintsContainer = document.getElementById('constraints-notice-container');
    const runForm = document.getElementById('run-form');
    const runButton = document.getElementById('run-button');
    const outputPre = document.getElementById('output');

    const urlParams = new URLSearchParams(window.location.search);
    const slug = urlParams.get('slug');

    if (!slug) {
        problemTitle.textContent = 'No Problem Specified';
        inputFields.innerHTML = '<p>Please select a problem from the main page.</p>';
        return;
    }

    problemTitle.textContent = slug.replace(/-/g, ' ');

    // Fetch problem details to build the form
    fetch(`${API_BASE_URL}/problems`)
        .then(response => response.json())
        .then(problems => {
            const problem = problems.find(p => p.slug === slug);
            if (!problem) {
                throw new Error(`Problem with slug "${slug}" not found.`);
            }
            
            // If a link exists, make the title a clickable link
            if (problem.link) {
                const link = document.createElement('a');
                link.href = problem.link;
                link.target = '_blank'; // Open in new tab
                link.rel = 'noopener noreferrer';
                link.textContent = problemTitle.textContent;
                problemTitle.innerHTML = '';
                problemTitle.appendChild(link);

                // Add the constraints notice
                const notice = document.createElement('p');
                notice.className = 'constraints-notice';
                notice.innerHTML = `Note: The provided solution is optimized for the original problem's constraints. Please <a href="${problem.link}" target="_blank" rel="noopener noreferrer">check the constraints</a> for details on input ranges.`;
                constraintsContainer.appendChild(notice);
            }

            buildForm(problem.params);
        })
        .catch(handleError);

    function buildForm(params) {
        inputFields.innerHTML = '';
        inputFields.removeAttribute('aria-busy');
        for (const [name, type] of Object.entries(params)) {
            const label = document.createElement('label');
            label.htmlFor = `param-${name}`;
            label.textContent = `${name} (${type}):`;

            let input;
            const lowerType = type.toLowerCase();

            if (lowerType.includes('list') || lowerType.includes('array')) {
                input = document.createElement('textarea');
                // Provide a more relevant placeholder based on the list's type
                if (lowerType.includes('int')) {
                    input.placeholder = 'e.g., [1, 2, 3]';
                } else if (lowerType.includes('str')) {
                    input.placeholder = 'e.g., ["a", "b", "c"]';
                } else {
                    input.placeholder = 'e.g., [1, "item", 3]';
                }
            } else {
                input = document.createElement('input');
                input.type = 'text';
                if (lowerType === 'int') {
                    input.placeholder = 'e.g., 123';
                } else {
                     input.placeholder = 'e.g., "hello world"';
                }
            }
            input.id = `param-${name}`;
            input.name = name;
            input.required = true;

            inputFields.appendChild(label);
            inputFields.appendChild(input);
        }
    }

    runForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const inputs = {};
        const formData = new FormData(runForm);

        for (const [name, value] of formData.entries()) {
            try {
                // Attempt to parse values that look like JSON arrays/objects
                // or numbers, otherwise treat as a string.
                if (value.trim().startsWith('[') || value.trim().startsWith('{')) {
                    inputs[name] = JSON.parse(value);
                } else if (!isNaN(value) && value.trim() !== '') {
                    inputs[name] = Number(value);
                }
                else {
                    inputs[name] = value;
                }
            } catch (err) {
                // If JSON.parse fails, treat it as a plain string.
                inputs[name] = value;
            }
        }
        
        const payload = { slug, inputs };
        executeCode(payload);
    });

    function executeCode(payload) {
        setLoadingState(true);
        outputPre.textContent = 'Running...';

        fetch(`${API_BASE_URL}/run`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        })
        .then(response => response.json())
        .then(data => {
            let resultText = `Status: ${data.status}\nExec Time: ${data.exec_ms}ms\n\n`;
            if (data.status === 'OK') {
                resultText += `Output:\n${data.stdout}`;
            } else {
                resultText += `Error:\n${data.stderr}`;
            }
            outputPre.textContent = resultText;
        })
        .catch(handleError)
        .finally(() => {
            setLoadingState(false);
        });
    }

    function handleError(error) {
        console.error('An error occurred:', error);
        outputPre.textContent = `An unexpected error occurred:\n${error.message}\n\nIs the backend server running?`;
        inputFields.innerHTML = 'Could not load problem details.';
    }
    
    function setLoadingState(isLoading) {
        runButton.disabled = isLoading;
        runButton.setAttribute('aria-busy', isLoading ? 'true' : 'false');
    }
}); 