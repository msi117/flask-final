import requests
import json

def emotion_detector(text_to_analyze):
    # API endpoint URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Request headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Request data
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    # Send POST request to the API
    response = requests.post(url, headers=headers, json=input_data)

    # Parse the JSON response
    json_response = json.loads(response.text)

    # Extract emotions
    emotions = json_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    highest_value = float('-inf')
    dominant_emotion = None

    for key, value in emotions.items():
        if value > highest_value:
            highest_value = value
            dominant_emotion = key

    emotions['dominant_emotion'] = dominant_emotion
    return emotions
