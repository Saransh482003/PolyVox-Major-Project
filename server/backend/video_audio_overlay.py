#embedding the translated audio in the video
from moviepy.editor import *
from moviepy.audio.fx.all import audio_loop
from moviepy.video.fx.all import speedx

def replace_audio(video_path, audio_path, output_path):
    # Load video and audio
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # If audio is shorter than video, speed up the audio
    if audio.duration < video.duration:
        audio = audio.fx(speedx, factor=audio.duration/video.duration)
    # If video is shorter than audio, slow down the audio
    elif video.duration < audio.duration:
        audio = audio.fx(speedx, factor=audio.duration/video.duration)

    # Replace the audio of the video
    video_with_new_audio = video.set_audio(audio)

    # Write the result to a file
    video_with_new_audio.write_videofile(output_path, codec='libx264')
    video.close()
    audio.close()
    video_with_new_audio.close()
