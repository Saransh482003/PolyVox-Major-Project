import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator, LANGUAGES

# Function to extract audio from a video and save it as an audio file
def extract_audio_from_video(video_path, output_audio_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)

# Define the desired languages
desired_languages = {
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
#if user wants to input manual text
def manual_text_translation(text,dest_name):
    desired_languages = {
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
    if dest_name in desired_languages:
        # print(dest_name)
        dest_code = desired_languages[dest_name]
        # print(dest_code)
        translator = Translator()
        translated_text = translator.translate(text, dest=dest_code)
        translated_text_only = translated_text.text
        # print(translated_text_only)
        return translated_text_only

    else:
        print("Invalid language selection. Please choose from English, Hindi, or Chinese.")

#if user does not input manual text ---the text will be extracted from audio in the video and then translated
def speech_translation(video_path = None, audio_output_path=None,dest_name=None,manual_text = "No",text = None):

    try:
        if manual_text in ["Yes","Y","yes","YES"]:
            resultant_text = manual_text_translation(text,dest_name)
            return resultant_text

        else:
            # Recognize speech from the extracted audio
            if video_path !=None:   #if video path is given then extract the audio from it
                extract_audio_from_video(video_path, audio_output_path)  
                r = sr.Recognizer()
                audio = sr.AudioFile(audio_output_path)
            else:   #video path not given take the audio for the audio path provided
                r = sr.Recognizer()
                audio = sr.AudioFile(audio_output_path)

            #perform audio to text conversion and text translation
            
            #audio to original text if dest_name parameter is not provided
            with audio as source:
                audio_file = r.record(source)
                result = r.recognize_google(audio_file)
            
                if dest_name!=None:
                    if dest_name in desired_languages:
                        dest_code = desired_languages[dest_name]
                        translator = Translator()
                        translated_text = translator.translate(result, dest=dest_code)
                        translated_text_only = translated_text.text
                        return translated_text_only
                    else:
                        print("Invalid language selection. Please choose from English, Hindi, or Chinese.")
                else:
                    return result

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting gracefully.")

#----------------------------------------------------------------------------------------------------------------------

