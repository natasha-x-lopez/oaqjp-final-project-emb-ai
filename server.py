"""
Server module for Emotion Detection application.
Provides endpoints for detecting emotions in text.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Handle POST requests to the /emotionDetector endpoint.
    
    Returns the emotion analysis of the provided text.
    
    Returns:
        json: A JSON response containing the emotion analysis or an error message.
    """
    data = request.get_json()
    text_to_analyze = data.get('text')
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again."})

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_text})

@app.route('/')
def index():
    """
    Serve the index.html file.
    
    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
