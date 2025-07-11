from flask import Flask, request, Response
import os
from io import BytesIO
from gtts import gTTS # google text-to-speech

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def home():

    text = "Hello, DevOps"

    # query string에서 lang 값을 가져오고, 없으면 DEFAULT_LANG(ko) 사용
    # en, ko, ja 등 지원
    lang = request.args.get('lang', DEFAULT_LANG)
    
    # 메모리 버퍼 생성
    # 메모리에서 바이너리값(파일 정보 등)을 다룰 수 있게 해줌
    fp = BytesIO()

    # gTTS 객체 생성, text는 음성으로 변환할 문자열, lang은 언어 코드
    # com은 tld(top level domain)으로, translate.google.<tld>에 접속하여 음성 변환
    # .com이 막힌 경우나, localized된 발음을 들을 수 있다.
    # https://gtts.readthedocs.io/en/latest/module.html
    gTTS(text, "com", lang).write_to_fp(fp)

    # Flask에서 기본으로 사용하는 Response 객체
    # 반환값과 해당 반환값이 어떤 형식인지 설정
    # mimetype: 미디어 타입. 문서, 파일 등의 바이트 집합이 어떤 형식인지 나타냄
    # https://tedboy.github.io/flask/generated/generated/flask.Response.html
    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)