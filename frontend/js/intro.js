window.addEventListener("DOMContentLoaded", () => {
    const cityIntroContainer = document.getElementById("city-intro-container");
    const cityIntroTitle = document.getElementById("city-intro-title");
    const cityIntroContent = document.getElementById("city-intro-content");
  
    // Example API request
    // Replace this with your own API request to fetch city introduction based on the city name from the URL query parameter
    fetchCityIntroduction()
      .then(data => {
        cityIntroTitle.textContent = data.cityName;
        cityIntroContent.innerHTML = data.introduction;
      })
      .catch(error => {
        console.log("Error fetching city introduction:", error);
        cityIntroTitle.textContent = "City";
        cityIntroContent.innerHTML = "An error occurred while fetching city introduction.";
      });
  });
  
  function fetchCityIntroduction() {
    // Simulate a delay and return a promise with mock data
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        // Get the city name from the URL query parameter
        const urlParams = new URLSearchParams(window.location.search);
        const cityName = urlParams.get("city");
  
        if (cityName && cityName.toLowerCase() === "paris") {
          resolve({
            cityName: "Paris",
            introduction: "<p>Paris is the capital and most populous city of France, with an estimated population of 2,148,271 residents.</p><p>Paris is known for its iconic landmarks such as the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral.</p>"
          });
        } else if (cityName && cityName.toLowerCase() === "new york city") {
          resolve({
            cityName: "New York City",
            introduction: "<p>New York City is the most populous city in the United States, with an estimated population of 8,336,817 residents.</p><p>New York City is famous for its landmarks such as Times Square, Statue of Liberty, and Central Park.</p>"
          });
        } else {
          reject("City not found");
        }
      }, 1000); // Simulate a delay of 1 second for fetching data
    });
  }
  