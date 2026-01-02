document.getElementById('convertForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const amount = document.getElementById('amount').value;
    const fromCurrency = document.getElementById('fromCurrency').value;
    const toCurrency = document.getElementById('toCurrency').value;

    const data = {
        ammount: amount,
        from: fromCurrency,
        to: toCurrency
    };

    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Converted Amount: ${data['Converted ammount']}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error converting currency';
    });
});
