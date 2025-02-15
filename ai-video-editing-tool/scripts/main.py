from scripts.video_processing import trim_video
from scripts.audio_processing import adjust_audio
from scripts.speech_to_text import transcribe_audio
from scripts.combine_media import combine_audio_with_video

def main():
    # Step 1: Trim video
    print("Trimming video...")
    trim_video('assets/sample_video.mp4', 10, 30, 'output/trimmed_video.mp4')

    # Step 2: Convert speech to text (generate subtitles)
    print("Generating subtitles...")
    transcribe_audio('assets/sample_audio.wav', 'data/transcriptions/video1.txt')

    # Step 3: Adjust audio (e.g., normalize volume)
    print("Adjusting audio...")
    adjust_audio('assets/sample_audio.wav', 'output/adjusted_audio.wav', -5)

    # Step 4: Combine trimmed video with adjusted audio
    print("Combining video and audio...")
    combine_audio_with_video('output/trimmed_video.mp4', 'output/adjusted_audio.wav', 'output/final_output.mp4')

    print("Process complete. Check the output folder for the final video.")

if __name__ == "__main__":
    main()
