import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    #Call API through a post call
    response = requests.post(url,json=myobj,headers=header)
    print(response)
    formatted_response = json.loads(response.text)

    #create empty emtions object
    emotions = {
        'anger' : None,
        'disgust' : None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emtion' : None
    }

    if response.status_code == 200:
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']

        emotions = {
            'anger' : emotion_data['anger'],
            'disgust' : emotion_data['disgust'],
            'fear': emotion_data['fear'],
            'joy': emotion_data['joy'],
            'sadness': emotion_data['sadness'],
        }

        dominant_emtion = max(emotions, key=emotions.get)

        emotions['dominant_emtion'] = dominant_emtion
        
    return emotions
        