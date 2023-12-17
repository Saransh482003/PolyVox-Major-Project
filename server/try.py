from backend.video_translation import manual_text_translation

data = {
    "text":"Hello everyone how are you",
    "lang":"French"
}
text = data["text"]
lang = data["lang"]
translated_text = manual_text_translation(text,lang)
print(translated_text)