from flask import Flask, request
from flask_cors import CORS
from pathlib import Path
import requests
# import moviepy.editor as mp
# import speech_recognition as sr
# from googletrans import Translator, LANGUAGES

import os
os.environ["XDG_CACHE_HOME"] = os.path.join("./backend/bark_cache")
from backend.workable_code import *
from backend.video_audio_overlay import *
# from backend.bark_code import *


app = Flask(__name__)
CORS(app)

@app.route("/api/textable",methods=["GET","POST"])
def textable():
    state = request.args.get("state")
    data = request.get_json()
    text = data["text"]
    lang = data["lang"]
    translated_text = manual_text_translation(text,lang)
    if state == "text":
        returnJson = {
            "trans_text":translated_text,
            "origin_text":text,
            "trans_lang":lang
        }
        return returnJson
    elif state == "audio":
        import backend.bark_code 
        dest = {
            'English': 'en',
            'Hindi': 'hi',
            'Chinese': 'zh-CN',
            'German': 'de',
            'Spanish': 'es',
            'French': 'fr',
            'Italian': 'it',
            'Japanese': 'ja',
            'Korean': 'ko',
            'Polish': 'pl',
            'Portuguese': 'pt',
            'Russian': 'ru',
            'Turkish': 'tr',
        }
        backend.bark_code.text_to_speech(f"v2/{dest[lang]}_speaker_2",translated_text,f"../polyvox/public/Audios/output/TTS_Output_{dest[lang]}.wav")
        file_path = Path(f"../polyvox/public/Audios/output/TTS_Output_{dest[lang]}.wav")
        if file_path.exists():
            returnJson = {
                "trans_text":translated_text,
                "origin_text":text,
                "trans_lang":lang,
                "trans_path":f"../polyvox/public/Audios/output/TTS_Output_{dest[lang]}.wav",
            }
            return returnJson, 200
        return {"Error":"No file generated"}, 400


@app.route("/api/hearable",methods=["GET","POST"])
def hearable():
    state = request.args.get("state")
    data = request.get_json()
    path = data["path"]
    extractedText = speech_translation(audio_output_path=path)
    if state=="text":
        returnJson = {
                "path":path,
                "trans_text":extractedText,
            }
        return returnJson, 200
    
    elif state=="transText":
        entry={
            "text":extractedText,
            "lang":data["lang"]
        }
        transFetcher = requests.post("http://127.0.0.1:8080/api/textable?state=text",json=entry)
        if transFetcher.status_code==200:
            transData = transFetcher.json()
            returnJson = {
                    "trans_text":transData["trans_text"],
                    "origin_text":extractedText,
                    "trans_lang":data["lang"],
                    "origin_path":path,
                }
            return returnJson, 200
        return {"message":"may day"}, 400
    
    elif state=="transAudio":
        entry={
            "text":extractedText,
            "lang":data["lang"]
        }
        transFetcher = requests.post("http://127.0.0.1:8080/api/textable?state=audio",json=entry)
        if transFetcher.status_code==200:
            transData = transFetcher.json()
            returnJson = {
                    "trans_text":transData["trans_text"],
                    "origin_text":extractedText,
                    "trans_lang":data["lang"],
                    "origin_path":path,
                    "trans_path":transData["trans_path"]
                }
            return returnJson, 200
        return {"message":"may day"}, 400
    
@app.route("/api/viewable",methods=["GET","POST"])
def viewable():
    state = request.args.get("state")
    data = request.get_json()
    path = data["path"]
    name = path.split("/")[-1].split(".")[0]
    extract_audio_from_video(path,f"../polyvox/public/Audios/output/{name}.wav")
    extractedText = speech_translation(audio_output_path=f"../polyvox/public/Audios/output/{name}.wav")
    if state == "audio":
        returnJson = {
                    "path":path,
                    "trans_path":f"../polyvox/public/Audios/output/{name}.wav",
        }
        return returnJson, 200
    elif state == "text":
        returnJson = {
                "path":path,
                "trans_text":extractedText,
            }
        return returnJson, 200
    elif state == "transText":
        entry={
            "text":extractedText,
            "lang":data["lang"]
        }
        transFetcher = requests.post("http://127.0.0.1:8080/api/textable?state=text",json=entry)
        if transFetcher.status_code==200:
            transData = transFetcher.json()
            returnJson = {
                    "trans_text":transData["trans_text"],
                    "origin_text":extractedText,
                    "trans_lang":data["lang"],
                    "origin_path":path,
                }
            return returnJson, 200
        return {"message":"may day"}, 400
    elif state == "transAudio":
        entry={
            "text":extractedText,
            "lang":data["lang"]
        }
        transFetcher = requests.post("http://127.0.0.1:8080/api/textable?state=audio",json=entry)
        if transFetcher.status_code==200:
            transData = transFetcher.json()
            returnJson = {
                    "trans_text":transData["trans_text"],
                    "origin_text":extractedText,
                    "trans_lang":data["lang"],
                    "origin_path":path,
                    "trans_path":transData["trans_path"]
                }
            return returnJson, 200
        return {"message":"may day"}, 400
    elif state == "transVideo":
        entry={
            "text":extractedText,
            "lang":data["lang"]
        }
        transFetcher = requests.post("http://127.0.0.1:8080/api/textable?state=audio",json=entry)
        if transFetcher.status_code==200:
            transData = transFetcher.json()
            replace_audio(path,transData["trans_path"],f"../polyvox/public/Videos/output/{name}_{data['lang']}.mp4")
            returnJson = {
                    "trans_text":transData["trans_text"],
                    "origin_text":extractedText,
                    "trans_lang":data["lang"],
                    "origin_path":path,
                    "trans_path":f"../polyvox/public/Videos/output/{name}_{data['lang']}.mp4"
            }
            return returnJson, 200
        return {"message":"may day"}, 400

if __name__=="__main__":
    app.run(debug=True,port=8080)