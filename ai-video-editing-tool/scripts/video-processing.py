from moviepy.editor import VideoFileClip

def trim_video(input_file, start_time, end_time, output_file):
    """Trim the video between start_time and end_time."""
    video = VideoFileClip(input_file)
    trimmed_video = video.subclip(start_time, end_time)
    trimmed_video.write_videofile(output_file, codec="libx264")

# Example usage
# trim_video('assets/sample_video.mp4', 10, 30, 'output/trimmed_video.mp4')
