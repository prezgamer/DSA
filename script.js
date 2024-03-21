// Initialize the map and set a default view
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

async function runPy() {
    const fromAirport = document.getElementById('fromAirport').value;
    const toAirport = document.getElementById('toAirport').value;
    
    let url = new URL('http://127.0.0.1:8000')
    let params = {param1: fromAirport, param2: toAirport}
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))

    try {
        response = await fetch(url)
        const routingInfo = await response.json();
        if (routingInfo == null) {
            window.alert("Either no route exists in between these airports or you have entered invalid airport names. Please try again.")
        }
        else {
            shortestPathInfo = routingInfo[0]
            totalDistance = routingInfo[1]
            fromLatitude = routingInfo[2]
            fromLongitude = routingInfo[3]
            toLatitude = routingInfo[4]
            toLongitude = routingInfo[5]
            
            // Clear previous markers and paths
            map.eachLayer(function(layer) {
                if (!!layer.toGeoJSON) {
                    map.removeLayer(layer);
                }
            });
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);

            // Add markers for the airports
            L.marker([fromLatitude, fromLongitude]).addTo(map)
                .bindPopup('Departure Airport: ' + fromAirport)
                .openPopup();
            L.marker([toLatitude, toLongitude]).addTo(map)
                .bindPopup('Destination Airport: ' + toAirport)
                .openPopup();

            // Draw the route
            const routeCoordinates = [
                [fromLatitude, fromLongitude],
                [toLatitude, toLongitude]
            ];
            const routePath = L.polyline(routeCoordinates, {color: 'blue'}).addTo(map);
            map.fitBounds(routePath.getBounds());

            // Display route details
            const displayElement = document.getElementById('routeDisplay');
            displayElement.innerHTML = `
                <strong>Flight Details:</strong><br>
                Shortest Path: ${shortestPathInfo}<br>
                Total Distance: ${totalDistance}km<br>
            `;
        }
    }
    catch (error) {
        console.error('There was an error fetching the data:', error);
        window.alert("Network error when trying to fetch data. Server may be down.")
    }
};

document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents form from submitting in the traditional way

    const fromAirport = document.getElementById('fromAirport').value;
    const toAirport = document.getElementById('toAirport').value;

    // Dummy data for demonstration (Replace these with your actual data fetching logic)
    const fromLatitude = 34.052235; // Example: Los Angeles (LAX)
    const fromLongitude = -118.243683;
    const toLatitude = 40.712776; // Example: New York (JFK)
    const toLongitude = -74.005974;
    const shortestPathInfo = 'Direct Flight';
    const totalDistance = '3940 km';
    const estimatedTravelTime = '5 hours 30 minutes';
    
    // Clear previous markers and paths
    map.eachLayer(function(layer) {
        if (!!layer.toGeoJSON) {
            map.removeLayer(layer);
        }
    });
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add markers for the airports
    L.marker([fromLatitude, fromLongitude]).addTo(map)
        .bindPopup('Departure Airport: ' + fromAirport)
        .openPopup();
    L.marker([toLatitude, toLongitude]).addTo(map)
        .bindPopup('Destination Airport: ' + toAirport)
        .openPopup();

    // Draw the route
    const routeCoordinates = [
        [fromLatitude, fromLongitude],
        [toLatitude, toLongitude]
    ];
    const routePath = L.polyline(routeCoordinates, {color: 'blue'}).addTo(map);
    map.fitBounds(routePath.getBounds());

    // Display route details
    const displayElement = document.getElementById('routeDisplay');
    displayElement.innerHTML = `
        <strong>Flight Details:</strong><br>
        Shortest Path: ${shortestPathInfo}<br>
        Total Distance: ${totalDistance}<br>
        Estimated Travel Time: ${estimatedTravelTime}<br>
    `;
});

