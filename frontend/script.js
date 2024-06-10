document.getElementById('myForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const value1 = document.getElementById('value1').value;
    const value2 = document.getElementById('value2').value;

    if (value1 && value2) {
        fetch('/api/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ value1, value2 })
        })
        .then(response => response.json())
        .then(data => {
            alert('Data submitted successfully!');
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        alert('Please fill in both fields.');
    }
});
