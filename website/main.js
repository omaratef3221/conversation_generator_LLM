document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button[type="project_button"]').forEach(button => {
        button.onclick = function() {
            var inputText = document.querySelector('.input_text').value;
            var buttonText = this.textContent;
            sendToPython(inputText, buttonText);
        };
    });
});

function sendToPython(inputText, buttonText) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:5500/generate', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (this.status == 200) {
            document.querySelector('.generated_conversation').innerHTML = this.responseText;
        }
    };
    xhr.send(JSON.stringify({text: inputText, button: buttonText}));
}

