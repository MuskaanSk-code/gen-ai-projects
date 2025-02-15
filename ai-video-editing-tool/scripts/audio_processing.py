from pydub import AudioSegment

def adjust_audio(input_file, output_file, volume_change_db):
    """Adjust the audio volume by a certain number of decibels."""
    audio = AudioSegment.from_file(input_file)
    adjusted_audio = audio + volume_change_db  # Increase or decrease volume
    adjusted_audio.export(output_file, format="wav")

# Example usage
# adjust_audio('assets/sample_audio.wav', 'output/adjusted_audio.wav', -5)
