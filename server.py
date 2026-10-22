"""flask init"""


from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import  emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """ description for detect emotion """
    #hello for static score core
    
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if(response['dominant_emotion'][0] == 'None'):
        return {'Invalid text! Please try again'}
    else:
        return {"Invalid text! Please try again"}
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50, debug=True)
