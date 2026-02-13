document.addEventListener('DOMContentLoaded', function() {
    console.log('Document is ready. Fetching data...');
    fetchAwardsData();
});

function fetchAwardsData() {
    fetch('https://api.usaspending.gov/api/v2/awards/accounts')
    .then(response => {
        console.log('Received response:', response);
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Data received:', data);
        displayAwards(data.results);
    })
    .catch(error => console.error('Error fetching data:', error));
}

function displayAwards(awards) {
    if (!awards) {
        console.error('No awards data to display.');
        return;
    }
    const container = document.getElementById('awards-container');
    // Clear previous content
    container.innerHTML = '';
    awards.forEach(award => {
        console.log('Displaying award:', award);
        const div = document.createElement('div');
        div.className = 'award';
        // Check if the award properties match what you expect
        div.innerHTML = `
            <h3>${award.award_title || 'No Title'}</h3>
            <p>Amount: $${award.award_amount || 'No Amount'}</p>
            <p>Recipient: ${award.recipient_name || 'No Recipient'}</p>
        `;
        container.appendChild(div);
    });
}
