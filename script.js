document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents form from submitting in the traditional way

    const fromAirport = document.getElementById('fromAirport').value;
    const toAirport = document.getElementById('toAirport').value;

    // Placeholder for where you would integrate the route finding logic
    const displayElement = document.getElementById('routeDisplay');
    displayElement.innerHTML = `Searching routes from ${fromAirport} to ${toAirport}...`;

    // Here, you'd call a function to search for routes and update the displayElement with the results
});
