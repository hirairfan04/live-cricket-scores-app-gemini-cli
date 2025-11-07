# Live Cricket Scores Viewer

This is a simple Flask web application that fetches and displays live cricket scores from an RSS feed.

## Features

*   Fetches live cricket scores from `https://static.cricinfo.com/rss/livescores.xml`.
*   Parses the XML feed to extract match titles, links, and descriptions.
*   Displays the scores in a user-friendly web interface.

## Project Structure

```
.
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

*   `app.py`: The main Flask application file. It handles routing, fetches the RSS feed, parses it, and renders the `index.html` template.
*   `requirements.txt`: Lists the Python dependencies required to run the application.
*   `templates/index.html`: The HTML template used to display the cricket scores.

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository (if applicable):**

    ```bash
    # If this project is in a Git repository
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Ensure your virtual environment is activated.**
2.  **Run the Flask application:**

    ```bash
    python app.py
    ```

3.  **Open your web browser** and navigate to `http://127.0.0.1:5000/` (or the address shown in your console).

## Technologies Used

*   Python
*   Flask
*   Requests library for HTTP requests
*   `xml.etree.ElementTree` for XML parsing
