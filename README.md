Include: 
• Instructions to run the Python script (e.g., python weather_fetcher.py). 
• How to view the webpage (e.g., open index.html in a browser). 
• Any dependencies (e.g., requests library). 
• A brief note on your approach or assumptions (e.g., "Assumed the JSON file is 
generated before loading the webpage")

# Weather Dashboard Project

## Project Overview
This project is a simple web application that provides weather information for a given city using the OpenWeatherMap API. It is built using Flask, HTML, CSS, and JavaScript.

## Folder Structure
```
/ (Root Directory)
|-- app.py
|-- /templates
|   |-- index.html
|-- /static
|   |-- styles.css
|   |-- script.js
|-- .env
|-- requirements.txt
```

## File Descriptions

### 1. `app.py`
**Purpose:** Flask-based Python script that handles the backend logic.

**Key Features:**
- Uses dotenv to load environment variables securely.
- Handles both GET and POST requests.
- Fetches weather data from the OpenWeatherMap API.
- Implements error handling for better user experience.

**Important Code Snippet:**
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        if not city:
            return render_template('index.html', error="Please enter a city name.")
```

### 2. `index.html`
**Purpose:** HTML template that serves as the frontend interface.

**Key Features:**
- Displays a form for city input.
- Dynamically shows weather data or error messages using Jinja templating.

**Important Code Snippet:**
```html
<form method="POST">
    <input type="text" name="city" placeholder="Enter city name" required>
    <button type="submit">Get Weather</button>
</form>
```

### 3. `styles.css`
**Purpose:** Custom CSS file for styling the web interface.

**Key Features:**
- Clean, modern design with light colors.
- Responsive form and weather display section.

**Important Code Snippet:**
```css
body {
    background-color: #f4f4f4;
    text-align: center;
}
```

### 4. `script.js`
**Purpose:** JavaScript file that fetches fallback data from `weather_data.json`.

**Key Features:**
- Loads sample data in case the API fails.
- Provides a smooth data display experience.

**Important Code Snippet:**
```js
document.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("/static/weather_data.json");
});
```

### 5. `.env`
**Purpose:** Stores sensitive data like the API key securely.

**Example Content:**
```
API_KEY="your_openweathermap_api_key"
```

## How to Run the Project

1. Install Dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Set Up Environment Variables:
   - Create a `.env` file in the root folder.
   - Add your OpenWeatherMap API key:
   ```sh
   API_KEY=your_openweathermap_api_key
   ```

3. Run the Flask Application:
   ```sh
   python app.py
   ```

4. Access the Web Application:
   - Open [http://localhost:5000](http://localhost:5000) in your browser.

## Contact Information
**Developer:** Saurav Anand  
**Email:** [anandsaurabh6789@gmail.com](mailto:anandsaurabh6789@gmail.com)

