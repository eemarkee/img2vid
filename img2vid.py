import os
import sys
import subprocess

def create_video_from_images(image_folder, frame_rate):
    """
    Creates a video from a sequence of images in a given folder.

    Args:
        image_folder (str): Path to the folder containing images.
        frame_rate (int): Frame rate of the output video.

    Example:
        python3 img2vid.py "C:/Users/marke/OneDrive/Videos/Captures/2" 30
    """
    if not os.path.exists(image_folder):
        print(f"Error: Folder '{image_folder}' not found.")
        return

    # Get the folder name to use as the video filename
    video_name = os.path.basename(image_folder)
    video_output = os.path.join(os.path.dirname(image_folder), f"{video_name}.mp4")

    # Define FFmpeg command to create the video
    ffmpeg_cmd = [
        "ffmpeg", "-framerate", str(frame_rate), "-i",
        os.path.join(image_folder, f"{video_name}_%06d.png"),  # Match extracted filenames
        "-c:v", "libx264", "-pix_fmt", "yuv420p", video_output,
        "-hide_banner", "-loglevel", "info"
    ]

    # Run FFmpeg command
    print(f"Creating video '{video_output}' from images in '{image_folder}' at {frame_rate} FPS...")
    subprocess.run(ffmpeg_cmd)

    print(f"Video saved as: {video_output}")

# Handle command-line arguments correctly
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 img2vid.py <image_folder> <frame_rate>")
    else:
        image_folder = sys.argv[1]  # Get actual folder path
        frame_rate = int(sys.argv[2])  # Convert frame rate to integer
        create_video_from_images(image_folder, frame_rate)
