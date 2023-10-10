from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    if request.method == 'POST':
        try:
            data = request.get_json()
            text_to_analyze = data.get('text')
            
            emotions = emotion_detector(text_to_analyze)

            emotions = [f"'{emotion}': {value}" for emotion, value in emotions.items() if emotion != "dominant_emotion"]
            return emotions


        except Exception as e:
            return jsonify({"error": str(e)}), 500
