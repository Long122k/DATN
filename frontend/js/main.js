// Function to handle the search
function handleSearch() {
  // Get the value from the search input
  const searchInput = document.querySelector(".search-input");
  const searchTerm = searchInput.value;

  // Call the API with the search term
  fetchData(searchTerm)
    .then((data) => {
      // Process the returned data
      displayResults(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
  // Store the search term in session storage
  sessionStorage.setItem("searchTerm", searchTerm);

  // Redirect to the new page without the search term in the URL
  // window.location.href = "city_intro.html";
}

// Function to fetch data from the API
function fetchData(searchTerm) {
  const url = `http://127.0.0.1:5000/api/search/${encodeURIComponent(
    searchTerm
  )}`;

  return fetch(url).then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  });
}

// Function to display the search results
function displayResults(data) {
  // Extract the relevant data from the API response
  const city = data.city_name;
  const intro = data.intro;
  const title = data.title;
  const activities = data.activity;
  const image = data.city_image;
  const country = data.country_name;

  // Display the results in the console
  console.log("City:", city);
  console.log("Intro:", intro);
  console.log("Title:", title);
  console.log("Activities:", activities);
  console.log("Image:", image);
  console.log("Country:", country);
}

// Check if the event listener is already attached to the search button
const searchButton = document.querySelector(".search-btn");
const clickEvent = new Event("click");
const searchButtonHasEventListener = searchButton.dispatchEvent(clickEvent);

// Attach the event listener only if it is not already attached
if (!searchButtonHasEventListener) {
  searchButton.addEventListener("click", handleSearch);
}
