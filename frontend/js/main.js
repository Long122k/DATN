function searchCity() {
    preventDefault();
    const cityInput = document.getElementById("city_input");
    const cityName = cityInput.value;
  
    // Example API request
    // Replace this with your own API request to fetch city information based on the entered city name
    fetchCityInformation(cityName)
      .then(data => {
        const cityInfoContainer = document.getElementById("city-info-container");
        const cityImage = cityInfoContainer.querySelector(".city-image");
        const cityTitle = cityInfoContainer.querySelector(".city-name");
        const cityNameElement = document.getElementById("city-name");
        const cityDescription = document.getElementById("city-description");
  
        // Update the city image, name, and description with the fetched data
        cityImage.src = data.imageUrl;
        cityImage.alt = data.cityName;
        cityTitle.textContent = data.cityName;
        cityNameElement.textContent = data.cityName;
        cityDescription.textContent = data.description;
  
        // Redirect to intro.html
        window.location.href = "intro.html";
      })
      .catch(error => {
        console.log("Error fetching city information:", error);
        // Reset the city image, name, and description in case of an error
        const cityInfoContainer = document.getElementById("city-info-container");
        const cityImage = cityInfoContainer.querySelector(".city-image");
        const cityTitle = cityInfoContainer.querySelector(".city-name");
        const cityNameElement = document.getElementById("city-name");
        const cityDescription = document.getElementById("city-description");
  
        cityImage.src = "images/p1.jpg";
        cityImage.alt = "City";
        cityTitle.textContent = "City";
        cityNameElement.textContent = "City";
        cityDescription.textContent = "An error occurred while fetching city information. Please try again.";
      });
  
    cityInput.value = ""; // Clear the search input
  
    return false;
  }
  
  function fetchCityInformation(cityName) {
    // Simulate a delay and return a promise with mock data
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (cityName.toLowerCase() === "paris") {
          resolve({
            cityName: "Paris",
            imageUrl: "images/p1.jpg",
            description: "Paris is the capital and most populous city of France, with an estimated population of 2,148,271 residents."
          });
        } else if (cityName.toLowerCase() === "new york city") {
          resolve({
            cityName: "New York City",
            imageUrl: "images/p2.jpg",
            description: "New York City is the most populous city in the United States, with an estimated population of 8,336,817 residents."
          });
        } else {
          reject("City not found");
        }
      }, 1000); // Simulate a delay of 1 second for fetching data
    });
  }
  

// Get all city info elements
const cityInfoElements = document.querySelectorAll('.city-info');

// Add click event listener to each city info element
cityInfoElements.forEach(cityInfo => {
  cityInfo.addEventListener('click', () => {
    // Toggle the 'active' class on the clicked city info element
    cityInfo.classList.toggle('active');
  });
});