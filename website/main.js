document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button[type="project_button"]').forEach(button => {
        button.onclick = function() {
            var inputText = document.querySelector('.input_text').value;
            var buttonText = this.textContent;
            sendToPython(inputText, buttonText);
            showProgressBar(); // Show progress bar when API call starts
        };
    });
});

function sendToPython(inputText, buttonText) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:5500/generate', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Update progress bar as the request progresses
    xhr.onprogress = function(event) {
        if (event.lengthComputable) {
            var percentComplete = (event.loaded / event.total) * 100;
            updateProgressBar(percentComplete);
        }
    };

    xhr.onload = function() {
        if (this.status == 200) {
            var formattedResponse = this.responseText.replace(/\n/g, '<br>');
            document.querySelector('.generated_conversation').innerHTML = formattedResponse;
        }
        hideProgressBar(); // Hide progress bar when API call is complete
    };

    xhr.send(JSON.stringify({text: inputText, button: buttonText}));
}

function showProgressBar() {
    document.getElementById('progressBarContainer').style.display = 'block';
    updateProgressBar(0); // Initialize progress to 0%
}

function updateProgressBar(percent) {
    document.getElementById('progressBar').style.width = percent + '%';
}

function hideProgressBar() {
    document.getElementById('progressBarContainer').style.display = 'none';
}
