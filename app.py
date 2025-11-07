
from flask import Flask, render_template
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    scores = []
    try:
        response = requests.get('https://static.cricinfo.com/rss/livescores.xml')
        response.raise_for_status()  # Raise an exception for HTTP errors
        root = ET.fromstring(response.content)

        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else 'N/A'
            link = item.find('link').text if item.find('link') is not None else '#'
            description = item.find('description').text if item.find('description') is not None else 'N/A'
            scores.append({'title': title, 'link': link, 'description': description})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        scores.append({'title': 'Error fetching scores', 'link': '#', 'description': str(e)})
    except ET.ParseError as e:
        print(f"Error parsing RSS feed: {e}")
        scores.append({'title': 'Error parsing scores', 'link': '#', 'description': str(e)})

    return render_template('index.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True)
