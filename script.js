// Initialize the map and set a default view
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);


const currencies = [
    { code: "SGD", name: "Singapore Dollar" },
    { code: "EUR", name: "Euro" },
    { code: "USD", name: "US Dollar" },
    { code: "JPY", name: "Japanese Yen" },
    { code: "BGN", name: "Bulgarian Lev" },
    { code: "CZK", name: "Czech Republic Koruna" },
    { code: "DKK", name: "Danish Krone" },
    { code: "GBP", name: "British Pound Sterling" },
    { code: "HUF", name: "Hungarian Forint" },
    { code: "PLN", name: "Polish Zloty" },
    { code: "RON", name: "Romanian Leu" },
    { code: "SEK", name: "Swedish Krona" },
    { code: "CHF", name: "Swiss Franc" },
    { code: "ISK", name: "Icelandic Króna" },
    { code: "NOK", name: "Norwegian Krone" },
    { code: "HRK", name: "Croatian Kuna" },
    { code: "RUB", name: "Russian Ruble" },
    { code: "TRY", name: "Turkish Lira" },
    { code: "AUD", name: "Australian Dollar" },
    { code: "BRL", name: "Brazilian Real" },
    { code: "CAD", name: "Canadian Dollar" },
    { code: "CNY", name: "Chinese Yuan" },
    { code: "HKD", name: "Hong Kong Dollar" },
    { code: "IDR", name: "Indonesian Rupiah" },
    { code: "ILS", name: "Israeli New Sheqel" },
    { code: "INR", name: "Indian Rupee" },
    { code: "KRW", name: "South Korean Won" },
    { code: "MXN", name: "Mexican Peso" },
    { code: "MYR", name: "Malaysian Ringgit" },
    { code: "NZD", name: "New Zealand Dollar" },
    { code: "PHP", name: "Philippine Peso" },
    { code: "THB", name: "Thai Baht" },
    { code: "ZAR", name: "South African Rand" },
    
  ];

  // Get the select element
  const selectElement = document.getElementById('currency');

  // Loop through the currencies array and create options
  currencies.forEach(currency => {
    const option = document.createElement('option');
    option.value = currency.code; // Set the value to the currency code
    option.textContent = `${currency.code} - ${currency.name}`; // Set the text content to the currency name
    selectElement.appendChild(option); // Append the option to the select element
  });

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

// explore flights button's onclick function
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


            // calc estimated flight time 
            const avgPlaneSpeed = 925; // km/h 
            const estFlightTime = totalDistance / avgPlaneSpeed; 
            const hours = Math.floor(estFlightTime); 
            const minutes = Math.round((estFlightTime - hours) * 60); 
            const estimatedTravelTime = `${hours} hours ${minutes} minutes`;

            // Retrieve the selected currency from the dropdown box
            const selectedCurrency = document.getElementById('currency').value;

            // Convert the total cost to the selected currency
            const convertedCost = await convertCurrency(totalCost, selectedCurrency);

            // Display the converted cost
 
            // Display route details 
            const displayElement = document.getElementById('routeDisplay'); 

            displayElement.innerHTML = ` 
                <h3><u><strong>Flight Details:</strong><br></u></h3>
                <h4><strong>Shortest Path:</strong> ${pathDisplay}<br></h4>
                
                <table>
                    <tr>
                        <th><strong>From</strong></th>
                        <th><strong>To</strong></th>
                        <th><strong>Total Distance</strong></th>
                        <th><strong>Total Cost</strong></th>
                        <th><strong>Estimated Travel Time:</strong></th>
                    </tr>
                    <tr>
                        <td>${fromAirport}</td>
                        <td>${toAirport}</td>
                        <td>${totalDistance}km</td>
                        <td>$${convertedCost} in ${selectedCurrency}</td>
                        <td>${estimatedTravelTime}</td>
                    </tr>
                    <tr>
                </table>


            `;

            // auto scrolls down to bring route details into view
            displayElement.scrollIntoView();
        }
    }
    catch (error) {
        console.error('There was an error fetching the data:', error);
        window.alert("Network error when trying to fetch data. Server may be down.");
    }
};


async function convertCurrency(amount, currency) {
    const apiUrl = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_U9zUYU7KcpW3PTTLaJEIHd8wljcrm7cwXllGwe1i&currencies=EUR%2CUSD%2CJPY%2CBGN%2CCZK%2CDKK%2CGBP%2CHUF%2CPLN%2CRON%2CSEK%2CCHF%2CISK%2CNOK%2CHRK%2CRUB%2CTRY%2CAUD%2CBRL%2CCAD%2CCNY%2CHKD%2CIDR%2CILS%2CINR%2CKRW%2CMXN%2CMYR%2CNZD%2CPHP%2CTHB%2CZAR&base_currency=SGD';

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        let rate;

        if (currency === 'SGD') {
            rate = 1; // Conversion rate from SGD to SGD is always 1
        } else if (data && data.data && data.data[currency]) {
            rate = data.data[currency];
        } else {
            throw new Error(`Conversion rate for ${currency} not found`);
        }

        const convertedAmount = amount * rate;
        return convertedAmount.toFixed(2); // Round to two decimal places
    } catch (error) {
        console.error('Currency conversion error:', error);
        throw new Error('Currency conversion failed');
    }
}



async function runPy2() {
    let url = new URL('http://127.0.0.1:8000');

    try {
        const response = await fetch(url);
        const airports = await response.json();

        // Use a Set to store unique airport names
        const uniqueAirportNames = new Set();

        // Extract and add airport names to the set
        airports.forEach(airport => {
            uniqueAirportNames.add(airport.airportName);
        });

        // Populate the datalist element with unique airport names
        const datalist = document.getElementById('airports');
        datalist.innerHTML = ''; // Clear existing options
        uniqueAirportNames.forEach(airportName => {
            const option = document.createElement('option');
            option.value = airportName;
            datalist.appendChild(option);
        });
    } catch (error) {
        console.error('There was an error fetching the data:', error);
        window.alert("Network error when trying to fetch data. Server may be down.");
    }
}





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

$(".custom-select").each(function() {
    var classes = $(this).attr("class"),
        id      = $(this).attr("id"),
        name    = $(this).attr("name");
    var template =  '<div class="' + classes + '">';
        template += '<span class="custom-select-trigger">' + $(this).find("option:selected").text() + '</span>';
        template += '<div class="custom-options">';
        $(this).find("option").each(function() {
          template += '<span class="custom-option ' + $(this).attr("class") + '" data-value="' + $(this).attr("value") + '">' + $(this).html() + '</span>';
        });
    template += '</div></div>';
    
    $(this).wrap('<div class="custom-select-wrapper"></div>');
    $(this).hide();
    $(this).after(template);
  });
  $(".custom-option:first-of-type").hover(function() {
    $(this).parents(".custom-options").addClass("option-hover");
  }, function() {
    $(this).parents(".custom-options").removeClass("option-hover");
  });
  $(".custom-select-trigger").on("click", function() {
    $('html').one('click',function() {
      $(".custom-select").removeClass("opened");
    });
    $(this).parents(".custom-select").toggleClass("opened");
    event.stopPropagation();
  });
  $(".custom-option").on("click", function() {
    $(this).parents(".custom-select-wrapper").find("select").val($(this).data("value"));
    $(this).parents(".custom-options").find(".custom-option").removeClass("selection");
    $(this).addClass("selection");
    $(this).parents(".custom-select").removeClass("opened");
    $(this).parents(".custom-select").find(".custom-select-trigger").text($(this).text());
  });
  
