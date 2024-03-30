// Initialize the map and set a default view
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);



function clear() {
    document.getElementById('fromAirport').value = '';
    document.getElementById('toAirport').value = '';

    // Clear markers
    map.eachLayer(function(layer) {
        if (!!layer.toGeoJSON && !(layer instanceof L.TileLayer)) {
            map.removeLayer(layer);
        }
    });
    // Clear flight details
    const displayElement = document.getElementById('routeDisplay');
    displayElement.innerHTML = '';

}

// Event listener for the clear button
document.getElementById('clearButton').addEventListener('click', function(event) {
    clear();
});

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
            // extract route information from routing info retrieved from server
            shortestPathInfo = routingInfo[0]
            pathNodeCoordinates = routingInfo[1]
            totalDistance = routingInfo[2]
            totalCost = routingInfo[3]

            // Clear previous markers and paths
            map.eachLayer(function(layer) {
                if (!!layer.toGeoJSON) {
                    map.removeLayer(layer);
                }
            });
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);
            
            for (let i = 0; i < pathNodeCoordinates.length-1; i++) {

                
                fromLongitude = pathNodeCoordinates[i][0]
                fromLatitude = pathNodeCoordinates[i][1]
                toLongitude = pathNodeCoordinates[i+1][0]
                toLatitude = pathNodeCoordinates[i+1][1]

                

                // Add markers for the airports
                if (pathNodeCoordinates.length < 3) {
                    L.marker([fromLatitude, fromLongitude]).addTo(map)
                        .bindPopup('Departure Airport: ' + shortestPathInfo[i])
                        .openPopup();
                    L.marker([toLatitude, toLongitude]).addTo(map)  
                        .bindPopup('Destination Airport: ' + shortestPathInfo[i+1])
                        .openPopup();
                }
                else if (i == 0) {
                    L.marker([fromLatitude, fromLongitude]).addTo(map)
                        .bindPopup('Departure Airport: ' + shortestPathInfo[i])
                        .openPopup();
                    L.marker([toLatitude, toLongitude]).addTo(map)  
                        .bindPopup('Connecting Airport: ' + shortestPathInfo[i+1])
                        .openPopup();
                }
                else if (i < pathNodeCoordinates.length-1) {
                    L.marker([fromLatitude, fromLongitude]).addTo(map)  
                        .bindPopup('Connecting Airport: ' + shortestPathInfo[i])
                        .openPopup();
                    L.marker([toLatitude, toLongitude]).addTo(map)  
                        .bindPopup('Destination Airport: ' + shortestPathInfo[i+1])
                        .openPopup();
                }
                else {
                    L.marker([fromLatitude, fromLongitude]).addTo(map)  
                        .bindPopup('Connecting Airport: ' + shortestPathInfo[i])
                        .openPopup();
                    L.marker([toLatitude, toLongitude]).addTo(map)  
                        .bindPopup('Connecting Airport: ' + shortestPathInfo[i+1])
                        .openPopup();
                }


                 // Calculate angle between two points
                const angle = Math.atan2(toLatitude - fromLatitude, toLongitude - fromLongitude) * (180 / Math.PI);

                // Define custom flight icon with rotation
                const flightIcon = L.icon({
                iconUrl: 'images/plane.png', // Replace 'path_to_your_flight_icon_image' with the actual path to your flight icon image
                iconSize: [32, 32], // Size of the icon
                iconAnchor: [16, 16], // Anchor point of the icon
                rotationAngle: angle // Rotate the icon based on the calculated angle
                });

                // Draw the route
    const routeCoordinates = [
        [fromLatitude, fromLongitude],
        [toLatitude, toLongitude]
    ];
    const routePath = L.polyline(routeCoordinates, {color: 'blue'}).addTo(map);
    map.fitBounds(routePath.getBounds());

    // Calculate midpoint coordinates
    const midLatitude = (fromLatitude + toLatitude) / 2;
    const midLongitude = (fromLongitude + toLongitude) / 2;

    // Add a flight icon marker at the midpoint coordinates of the route
    L.marker([midLatitude, midLongitude], { icon: flightIcon }).addTo(map);



                // // Draw the route
                // const routeCoordinates = [
                //     [fromLatitude, fromLongitude],
                //     [toLatitude, toLongitude]
                // ];
                // const routePath = L.polyline(routeCoordinates, {color: 'blue'}).addTo(map);
                // map.fitBounds(routePath.getBounds());
            }

            
            

            let pathDisplay; 
            // If shortestPathInfo is an array of airport names 
            if (Array.isArray(shortestPathInfo)) { 
                pathDisplay = shortestPathInfo.join(' -> '); 
            } else if (typeof shortestPathInfo === 'string') { 
                // If it's a string, replace all commas with ' -> ' 
                pathDisplay = shortestPathInfo.split(',').join(' -> '); 
            } else { 
            // If shortestPathInfo is neither an array nor a string, log an error or set a default value 
            console.error('Unexpected type for shortestPathInfo'); 
            pathDisplay = 'Unknown'; // or set a default value 
            } 

            // Calculate estimated flight time 
            const avgPlaneSpeed = 925; // km/h 
            const estFlightTime = totalDistance / avgPlaneSpeed; 
            const hours = Math.floor(estFlightTime); 
            const minutes = Math.round((estFlightTime - hours) * 60); 
            const estimatedTravelTime = `${hours} hours ${minutes} minutes`;
 
            // Display route details
            const displayContainer = document.getElementById('routeDisplay');
            displayContainer.innerHTML = ''; // Clear previous content

            // Create table and its header
            const table = document.createElement('table');
            table.className = 'table'; // Add class if you have specific styles for tables

            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');

            const headers = ["Departure Airport", "Destination Airport", "Total Distance", "Estimated Travel Time", "Price"];
            headers.forEach(headerText => {
                const header = document.createElement('th');
                header.textContent = headerText;
                headerRow.appendChild(header);
            });

            thead.appendChild(headerRow);
            table.appendChild(thead);

            // Create table body where the dynamic rows will be added
            const tbody = document.createElement('tbody');
            table.appendChild(tbody);

            // Dynamically add rows to the table body based on data
            shortestPathInfo.forEach((airport, index) => {
                if (index < shortestPathInfo.length - 1) {
                    const row = tbody.insertRow();
                    
                    let cell = row.insertCell();
                    cell.textContent = shortestPathInfo[index]; // From airport
                    
                    cell = row.insertCell();
                    cell.textContent = shortestPathInfo[index + 1]; // To airport
                    
                    cell = row.insertCell();
                    cell.textContent = `${Math.round(totalDistance / (shortestPathInfo.length - 1))} km`; // Distance
                    
                    cell = row.insertCell();
                    const legTime = estFlightTime / (shortestPathInfo.length - 1);
                    const legHours = Math.floor(legTime);
                    const legMinutes = Math.round((legTime - legHours) * 60);
                    cell.textContent = `${legHours} hours ${legMinutes} minutes`; // Estimated Travel Time

                    cell = row.insertCell();
                    cell.textContent = `$${Math.round(totalCost / (shortestPathInfo.length - 1))}`; // Price
                }
            });

            // Append the fully constructed table to display container
            displayContainer.appendChild(table);

            // auto scrolls down to bring route details into view
            displayElement.scrollIntoView();
        }
    }
    catch (error) {
        console.error('There was an error fetching the data:', error);
        window.alert("Network error when trying to fetch data. Server may be down.")
    }
};

// document.getElementById('searchForm').addEventListener('submit', function(event) {
//     event.preventDefault(); // Prevents form from submitting in the traditional way

//     const fromAirport = document.getElementById('fromAirport').value;
//     const toAirport = document.getElementById('toAirport').value;

//     // Dummy data for demonstration (Replace these with your actual data fetching logic)
//     const fromLatitude = 34.052235; // Example: Los Angeles (LAX)
//     const fromLongitude = -118.243683;
//     const toLatitude = 40.712776; // Example: New York (JFK)
//     const toLongitude = -74.005974;
//     const shortestPathInfo = 'Direct Flight';
//     const totalDistance = '3940 km';
//     const estimatedTravelTime = '5 hours 30 minutes';
    
//     // Clear previous markers and paths
//     map.eachLayer(function(layer) {
//         if (!!layer.toGeoJSON) {
//             map.removeLayer(layer);
//         }
//     });
//     L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//         attribution: '© OpenStreetMap contributors'
//     }).addTo(map);

//     // Add markers for the airports
//     L.marker([fromLatitude, fromLongitude]).addTo(map)
//         .bindPopup('Departure Airport: ' + fromAirport)
//         .openPopup();
//     L.marker([toLatitude, toLongitude]).addTo(map)
//         .bindPopup('Destination Airport: ' + toAirport)
//         .openPopup();

//     // Draw the route
//     const routeCoordinates = [
//         [fromLatitude, fromLongitude],
//         [toLatitude, toLongitude]
//     ];
//     const routePath = L.polyline(routeCoordinates, {color: 'blue'}).addTo(map);
//     map.fitBounds(routePath.getBounds());

//     // Display route details
//     const displayElement = document.getElementById('routeDisplay');
//     displayElement.innerHTML = `
//         <strong>Flight Details:</strong><br>
//         Shortest Path: ${shortestPathInfo}<br>
//         Total Distance: ${totalDistance}<br>
//         Estimated Travel Time: ${estimatedTravelTime}<br>
//     `;
// });

