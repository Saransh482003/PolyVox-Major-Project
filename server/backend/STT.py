from video_translation import speech_translation,text_to_speech,replace_audio

''' 
1. Translated audio only (either ways; input = audio/video)
can be generated using the following function
for example: 
this will help you to translate the audio; you can skip video path if you have audio already

--Text = speech_translation(video_path=video,audio_output_path=audio_output_path,dest_name = lang,manual_text=manual_text)   

#replace the "speaker" with the speaker id, translated audio is the path where the translated file will be saved.
--text_to_speech(speaker,Text,translated_audio)

the output of these two lines will be the translated audio.

2. Translated text only 

this will help you to translate the audio; you can skip video path if you have audio already

--Text = speech_translation(video_path=video,audio_output_path=audio_output_path,dest_name = lang,manual_text=manual_text)
--print(Text) #this will return the translated text only


3. Audio to text (without any translation)

This will transcribe the audio in its original language when not given dest_name
--Text = speech_translation(video_path=video,audio_output_path=audio_output_path,manual_text=manual_text)
--print(Text) #this will return the original text only

4. text to audio/translated translated audio
#if manual text is provided then 
use the following function for text to audio

#relace the value of dest_name parameter for translation to any other language else keep it none or do not mention it either.
--Text = speech_translation(manual_text="yes",dest_name = None,text = text)   
--print(Text)
#text to speech conversion
--text_to_speech(speaker,Text,translated_audio)

'''


#------------------------------------------------------------------------------------------------------------------------#

'''for the text being entered by the user manually'''

# #complete usage
# #this is an example to embed AI audio in a video with no audio by inputting manual text
# translated_audio = 'files/en_audio4.wav'  #the file location where translated audio will be saved
# video = "files/video 4.mp4"   #the location of the actual video file
# output_video_path = "files/en_video4.mp4"  #the location where the translated video will be saved
# speaker  = "v2/en_speaker_1"    #select the speaker id
# audio_output_path = "files/extracted_audio_video4.wav"  #the location where the extracted audio will be saved

# #extracted text translation
# #the audio must not have background sound like music,noise etc. for better quality text extraction
# manual_text = "Yes"   #if this is "yes" then the user need to type the text manually
# lang= "English"  #the language in which the text will be converted
# text = """Friends, Here are some data science roles and their average salaries in India. Data Engineer earn over 8.35 lakhs per annum, 
# Data Scientist being 11 lakhs per annum, Data Analyst has 5.5 lakhs per annum, 8.3 lakhs per annum being offered to AI Engineer 
# and a Machine Learning Engineer has been offered 7.5 lakhs per annum on average. Follow us on Instagram for more updates."""

# # #if manual text is provided then the text will be translated else the text will be extracted from the video provided.
# # Text = speech_translation(dest_name = lang,manual_text=manual_text,text = text)   
# # print(Text)

# #text to speech conversion
# text_to_speech(speaker,text,translated_audio)  

# #embed the translated audio in video
# replace_audio(video, translated_audio,output_video_path)



#------------------------------------------------------------------------------------------------------------------------#

'''
An Example to translate video (end to end)

'''

#complete usage
#this is an example of completely translating the audio of a video embed it in the video at the end.
translated_audio = 'files/hi_audio6.wav'  #the file location where translated audio will be saved
video = "files/video6.mp4"   #the location of the actual video file
output_video_path = "files/hi_video6.mp4"  #the location where the translated video will be saved
speaker  = "v2/hi_speaker_2"    #select the speaker id
audio_output_path = "files/extracted_audio_video6.wav"  #the location where the extracted audio will be saved

#extracted text translation
#the audio must not have background sound like music,noise etc. for better quality text extraction
manual_text = "No"   #if this is "yes" then the user need to type the text manually
lang= "Hindi"  #the language in which the text will be converted

#if manual text is provided then the text will be translated else the text will be extracted from the video provided.
Text = speech_translation(video_path=video,audio_output_path=audio_output_path,dest_name = lang)   
print(Text)

#text to speech conversion
text_to_speech(speaker,Text,translated_audio)  

#embed the translated audio in video
replace_audio(video, translated_audio,output_video_path)




