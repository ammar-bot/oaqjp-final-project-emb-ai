import requests
import json


def emotion_detector(text_to_analyse):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

	    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

	    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

	    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)   
    formatted_response = json.loads(response.text)
    if(response.status_code == 400): 
       
        return {'anger': "None", 'disgust': "None", 'fear':"None", 'joy':"None",'sadness':"None",'dominant_emotion': "None"}

       
    else:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        listEmotions = [('anger',anger),('fear',fear),('disgust',disgust),
        ('joy',joy), ('sadness',sadness)]

        dominant_emotion = max(listEmotions, key=lambda x: x[1])

        return {'anger': anger, 'disgust': disgust, 'fear':fear, 'joy':joy,'sadness':sadness,'dominant_emotion': dominant_emotion}
    