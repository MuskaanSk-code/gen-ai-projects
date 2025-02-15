from moviepy.editor import VideoFileClip

def trim_video(input_file, start_time, end_time, output_file):
    """Trim the video between start_time and end_time."""
    # Load the video file
    video = VideoFileClip(input_file)
    
    # Get the video duration
    video_duration = video.duration
    print(f"Video Duration: {video_duration} seconds")
    
    # Ensure start_time and end_time are within the video duration
    if start_time >= video_duration:
        print(f"Start time {start_time} is greater than video duration. Adjusting to {video_duration - 1} seconds.")
        start_time = video_duration - 1  # Adjust start_time to be just 1 second before the video ends
    
    if end_time > video_duration:
        end_time = video_duration  # Limit end_time to the video duration

    # Trim the video
    trimmed_video = video.subclip(start_time, end_time)
    
    # Save the trimmed video
    trimmed_video.write_videofile(output_file, codec="libx264")

# Example usage (you can test this with your own times)
# trim_video('assets/sample_video.mp4', 10, 30, 'output/trimmed_video.mp4')
