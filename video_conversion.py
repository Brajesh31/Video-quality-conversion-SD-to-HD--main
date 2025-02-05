import cv2
import os
import subprocess

def upscale_video(input_file, output_file, scale_factor=2):
    temp_video = "temp_upscaled_video.avi"
    temp_audio = "temp_audio.aac"

    # Extract audio from the input video
    extract_audio(input_file, temp_audio) 

    # Open the video capture object
    cap = cv2.VideoCapture(input_file)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error opening video file!")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define new width and height based on scale factor
    new_width = width * scale_factor
    new_height = height * scale_factor

    # Define video writer for output
    writer = cv2.VideoWriter(temp_video, cv2.VideoWriter_fourcc(*'XVID'), fps, (new_width, new_height))

    # Process video frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Upscale the frame using interpolation (e.g., cv2.INTER_CUBIC)
        upscaled_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        # Write the upscaled frame to the output video
        writer.write(upscaled_frame)

    # Release resources
    cap.release()
    writer.release()

    # Merge the upscaled video with the original audio
    merge_audio_video(temp_video, temp_audio, output_file)

    # Remove temporary files
    os.remove(temp_video)
    os.remove(temp_audio)

def extract_audio(video_path, audio_path):
    """Extracts audio from a video file using ffmpeg."""
    command = f"ffmpeg -i \"{video_path}\" -q:a 0 -map a \"{audio_path}\""
    subprocess.run(command, shell=True, check=True)

def merge_audio_video(video_path, audio_path, output_path):
    """Merges audio and video files using ffmpeg."""
    command = f"ffmpeg -i \"{video_path}\" -i \"{audio_path}\" -c:v copy -c:a aac -strict experimental \"{output_path}\""
    subprocess.run(command, shell=True, check=True)

# Example usage
input_file = "C:/Users/sandh/Desktop/video_conversion/input_video/input_sd_video.mp4"
output_file = "C:/Users/sandh/Desktop/video_conversion/upscaled_video/output_hd_video.mp4"
upscale_video(input_file, output_file)

print("Video upscaling complete!")
