from flask import Flask, request, Response, render_template
import os
from io import BytesIO
from gtts import gTTS # google text-to-speech
import base64

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def home():

    text = "Hello, DevOps"

    lang = request.args.get('lang', DEFAULT_LANG)
    
    fp = BytesIO()

    gTTS(text, "com", lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

@app.route("/tts", methods=['GET', 'POST'])
def tts():
    if request.method == 'GET':
        return render_template('index.html', error=None, audio=None)
    form = request.form
    text = form.get('input_text', 'Hello, DevOps')
    lang = form.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    try:
        gTTS(text, tld="com", lang=lang).write_to_fp(fp)
    except Exception as e:
        return render_template('index.html', error=f"오디오 생성 실패: {str(e)}", audio=None)
    return render_template('index.html', audio=base64.b64encode(fp.getvalue()).decode())

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)