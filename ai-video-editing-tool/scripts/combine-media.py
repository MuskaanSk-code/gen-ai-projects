from moviepy.editor import VideoFileClip, AudioFileClip

def combine_audio_with_video(video_file, audio_file, output_file):
    """Combine the video with a new audio track."""
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    video = video.set_audio(audio)
    video.write_videofile(output_file, codec="libx264")

# Example usage
# combine_audio_with_video('output/trimmed_video.mp4', 'output/adjusted_audio.wav', 'output/final_output.mp4')
