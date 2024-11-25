import os
import subprocess

input_dir = "videos_orig"
output_dir = "videos"

os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for file_name in os.listdir(input_dir):
    input_path = os.path.join(input_dir, file_name)

    if os.path.isfile(input_path) and file_name.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.wmv')):
        output_path = os.path.join(output_dir, file_name)

        ffmpeg_command = [
            "ffmpeg",
            "-i", input_path,         # Input file
            "-c:v", "libx264",        # Use H.264 codec for video
            "-preset", "slow",        # Balance compression and speed
            "-crf", "23",             # Quality factor (lower = better quality)
            "-c:a", "aac",            # Use AAC codec for audio
            output_path               # Output file
        ]

        print(f"Converting {file_name} to H.264...")
        
        subprocess.run(ffmpeg_command, check=True)

print(f"Conversion completed! Converted files are in the {output_dir} directory.")
