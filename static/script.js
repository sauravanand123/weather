document.addEventListener("DOMContentLoaded", async () => {
    const weatherDataDiv = document.getElementById("weather-data");

    try {
        const response = await fetch("/static/weather_data.json");
        if (!response.ok) {
            throw new Error("Failed to fetch weather data.");
        }

        const data = await response.json();
        weatherDataDiv.innerHTML = `
            <p><strong>City:</strong> ${data.city}</p>
            <p><strong>Temperature:</strong> ${data.temperature}°C</p>
            <p><strong>Description:</strong> ${data.description}</p>
            <p><strong>Humidity:</strong> ${data.humidity}%</p>
        `;
    } catch (error) {
        weatherDataDiv.innerHTML = `<p>Error loading weather data. Please try again later.</p>`;
        console.error("Error fetching weather data:", error);
    }
});
