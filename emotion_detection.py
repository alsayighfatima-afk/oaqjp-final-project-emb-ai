import requests
import json

def emotion_detector(text_to_analyze):
    # الرابط والهيدرز الخاصة بـ Watson NLP [citation:1][citation:2]
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # التعامل مع الخطأ 400 (للسؤال 12)
    if response.status_code == 400:
        return None # أو return {"error": "Invalid text"}
        
    # تحويل النص إلى JSON (للسؤال 2)
    formatted_response = json.loads(response.text)
    
    # استخراج المشاعر (للسؤال 4)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # إيجاد المشاعر المسيطرة (Dominant Emotion)
    emotion_scores = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # التنسيق النهائي (للسؤال 4)
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }