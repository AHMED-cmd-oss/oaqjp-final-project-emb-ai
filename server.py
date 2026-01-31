"""
API with Flask for 
AI application
"""
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route('/')
def index():
    """
    rendering HTML file
    """
    return render_template("index.html")
@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detection():
    """
    Endpoints to get emotion detection model result
    """
    user_input = request.args.get('textToAnalyze')
    result = emotion_detector(user_input)
    if result['dominant_emotion'] is None:
        return "Invalid input!",400
    return (
        f"For the given statement, the system response is"
        f"'anger':{result['anger']}, 'disgust': {result['disgust']},"
        f"'fear': {result['fear']}, 'joy': {result['joy']}"
        f"and 'sadness': {result['sadness']}."
        f"The dominant emotion is {result['dominant_emotion']}."
    ),200
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5008)
        