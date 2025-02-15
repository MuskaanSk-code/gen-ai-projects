import speech_recognition as sr

def transcribe_audio(input_file, output_file):
    """Convert audio to text and save it as a transcription file."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(input_file) as source:
        audio = recognizer.record(source)
    
    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        with open(output_file, 'w') as f:
            f.write(text)
        print(f"Transcription saved to {output_file}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech service.")

# Example usage
# transcribe_audio('assets/sample_audio.wav', 'data/transcriptions/video1.txt')
