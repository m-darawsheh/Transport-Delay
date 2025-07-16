# Transport Delay Application
This document provides an overview of the Transport Delay application, including its features, installation instructions, and usage guidelines.

## Features
- Predict transport delays based on user input.
- User-friendly interface built with Flask and HTML.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/m-darawsheh/Transport-Delay.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Transport-Delay
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask development server:
   ```bash
   python main.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.
3. Interact with the application through the web interface.

## File Structure
- `main.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory for static files (CSS, JavaScript, images).
- `requirements.txt`: List of Python dependencies.

## Building prossesses

- The application uses Flask for the backend and HTML for the frontend.
- The main route (`/`) renders the `index.html` template.
- The `/get_info` route handles user input and renders the `predict.html` template.
- The `/result` route displays the prediction result using the `result.html` template.

## prediction process

1. User inputs relevant data through the web interface.
2. The application processes the input and makes a prediction.
3. The result is displayed on the `/result` page.

## workflow

1. abedalmuhdi collected the data and clean it and prepare it for the model training.
2. The model was trained using the cleaned data by abedalmuhdi.
3. While abedalmuhdi was looking for the data, we decided to make the flask application.
4. mohammed darawsheh and fares worked together to build the get_info.html routes.
5. and i did the index.html and result.html routes.
6. finally, we told  AI agent to make interface for the application.