function appendToBlockchain() {
    const dataInput = document.getElementById('dataInput');
    const data = dataInput.value;

    // Make a request to the server-side Perl script to append data to blockchain
    fetch('/appendData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data })
    })
    .then(response => response.json())
    .then(result => {
        const statusMessage = document.getElementById('statusMessage');
        if (result.success) {
            statusMessage.textContent = 'Data successfully added to the blockchain file.';
        } else {
            statusMessage.textContent = 'Error adding data to the blockchain file.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        const statusMessage = document.getElementById('statusMessage');
        statusMessage.textContent = 'An error occurred while processing your request.';
    });
}
