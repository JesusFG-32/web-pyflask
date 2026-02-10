from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Dummy Data
SPEAKERS = {
    1: {"first": "Alice", "last": "Johnson", "linkedin": "https://linkedin.com/in/alicejohnson"},
    2: {"first": "Bob", "last": "Smith", "linkedin": "https://linkedin.com/in/bobsmith"},
    3: {"first": "Charlie", "last": "Davis", "linkedin": "https://linkedin.com/in/charliedavis"},
    4: {"first": "Diana", "last": "Evans", "linkedin": "https://linkedin.com/in/dianaevans"},
    5: {"first": "Evan", "last": "Wright", "linkedin": "https://linkedin.com/in/evanwright"},
    6: {"first": "Fiona", "last": "Green", "linkedin": "https://linkedin.com/in/fionagreen"},
    7: {"first": "George", "last": "Harris", "linkedin": "https://linkedin.com/in/georgeharris"},
    8: {"first": "Hannah", "last": "Lewis", "linkedin": "https://linkedin.com/in/hannahlewis"},
    9: {"first": "Ian", "last": "Clark", "linkedin": "https://linkedin.com/in/ianclark"},
    10: {"first": "Julia", "last": "Walker", "linkedin": "https://linkedin.com/in/juliawalker"},
    11: {"first": "Kevin", "last": "Hall", "linkedin": "https://linkedin.com/in/kevinhall"},
    12: {"first": "Laura", "last": "Allen", "linkedin": "https://linkedin.com/in/lauraallen"}
}

SCHEDULE = [
    {
        "id": 1,
        "time": "09:00 - 09:45",
        "title": "Keynote: The Future of Cloud Computing",
        "speakers": [1, 2],
        "category": ["Keynote", "Cloud Architecture"],
        "description": "An overview of where cloud technology is heading in the next decade.",
        "type": "talk"
    },
    {
        "id": 2,
        "time": "10:00 - 10:45",
        "title": "Mastering Kubernetes with GKE",
        "speakers": [3],
        "category": ["DevOps", "Containers"],
        "description": "Deep dive into managing containers at scale using Google Kubernetes Engine.",
        "type": "talk"
    },
    {
        "id": 3,
        "time": "11:00 - 11:45",
        "title": "AI/ML on Google Cloud: Vertex AI",
        "speakers": [4, 5],
        "category": ["AI/ML", "Data Science"],
        "description": "Building and deploying machine learning models efficiently with Vertex AI.",
        "type": "talk"
    },
    {
        "id": 4,
        "time": "12:00 - 13:00",
        "title": "Lunch Break",
        "speakers": [],
        "category": ["Break"],
        "description": "Enjoy a networking lunch!",
        "type": "break"
    },
    {
        "id": 5,
        "time": "13:00 - 13:45",
        "title": "BigQuery for Big Data Analytics",
        "speakers": [6],
        "category": ["Data Analytics", "Big Data"],
        "description": "Unlocking insights from petabytes of data using BigQuery.",
        "type": "talk"
    },
    {
        "id": 6,
        "time": "14:00 - 14:45",
        "title": "Serverless Development with Cloud Run",
        "speakers": [7, 8],
        "category": ["Serverless", "App Dev"],
        "description": "Focus on code, not infrastructure, by deploying to Cloud Run.",
        "type": "talk"
    },
    {
        "id": 7,
        "time": "15:00 - 15:45",
        "title": "Securing Your Cloud Infrastructure",
        "speakers": [9],
        "category": ["Security", "Cloud Architecture"],
        "description": "Best practices for IAM and network security in Google Cloud.",
        "type": "talk"
    },
    {
        "id": 8,
        "time": "16:00 - 16:45",
        "title": "Multi-Cloud Strategies with Anthos",
        "speakers": [10, 11],
        "category": ["Hybrid Cloud", "Strategy"],
        "description": "Managing applications across on-premise and multiple cloud environments.",
        "type": "talk"
    },
    {
        "id": 9,
        "time": "17:00 - 17:45",
        "title": "Closing Remarks & Networking",
        "speakers": [12],
        "category": ["Networking"],
        "description": "Wrap up the day and connect with fellow attendees.",
        "type": "talk"
    }
]

def get_speaker_details(speaker_ids):
    details = []
    for sid in speaker_ids:
        if sid in SPEAKERS:
            details.append(SPEAKERS[sid])
    return details

@app.route('/')
def home():
    current_date = datetime.now().strftime("%B %d, %Y")
    # Enrich schedule with speaker details for list view if needed, 
    # but we can also just pass the raw data and look it up in template or enrich here.
    # Let's enrich here for easier template rendering.
    enriched_schedule = []
    for event in SCHEDULE:
        event_copy = event.copy()
        event_copy['speaker_details'] = get_speaker_details(event.get('speakers', []))
        enriched_schedule.append(event_copy)
        
    return render_template('index.html', 
                           date=current_date, 
                           location="San Francisco, CA", 
                           schedule=enriched_schedule)

@app.route('/api/search')
def search():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify(SCHEDULE)
    
    results = []
    for event in SCHEDULE:
        if event['type'] == 'break':
            continue
            
        # Check title
        if query in event['title'].lower():
            results.append(event)
            continue
            
        # Check category
        if any(query in cat.lower() for cat in event['category']):
            results.append(event)
            continue
            
        # Check speakers
        speaker_ids = event['speakers']
        speaker_details = get_speaker_details(speaker_ids)
        found_speaker = False
        for sp in speaker_details:
             full_name = f"{sp['first']} {sp['last']}".lower()
             if query in full_name:
                 found_speaker = True
                 break
        if found_speaker:
            results.append(event)
            
    # Enrich results with speaker details before returning
    enriched_results = []
    for event in results:
        event_copy = event.copy()
        event_copy['speaker_details'] = get_speaker_details(event.get('speakers', []))
        enriched_results.append(event_copy)

    return jsonify(enriched_results)

if __name__ == '__main__':
    app.run(debug=True)
