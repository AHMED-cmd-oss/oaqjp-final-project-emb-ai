import requests

def emotion_detector(text_to_analyse):
    """
    This function get result from IBM emotion detection model. 
    """
    if not text_to_analyse:
        return {"dominant_emotion":None}   
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    user_input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL,headers = headers,json = user_input)
    if response.status_code == 200:
        result = response.json()["emotionPredictions"][0]['emotion']
        result['dominant_emotion'] = max(result,key = result.get)
        return result
    elif response.status_code == 400:
        return {"dominant_emotion":None}   
    
