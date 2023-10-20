# Python script that can extract frames from a video at a rate of one frame per second

import os
import cv2

# Define the path to the input videos folder and the output folder for frames
input_folder = r"path_to_input_videos_folder"  # Replace with the path to your input videos folder
output_folder = r"path_to_output_frames_folder"  # Replace with the path to your output frames folder

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all the files in the input folder
videos = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]

# Loop through each video file
for video_file in videos:
    # Construct the full path to the video file
    video_path = os.path.join(input_folder, video_file)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video was successfully opened
    if not cap.isOpened():
        print(f"Could not open video: {video_file}")
        continue
    
    # Initialize counters and flags
    frame_count = 0
    success = True

    # Loop through frames
    while success:
        # Read a frame from the video
        success, frame = cap.read()
        
        # Check if the read was successful
        if success:
            # Calculate the time (in seconds) of the current frame
            time_in_seconds = frame_count // cap.get(cv2.CAP_PROP_FPS)

            # Save the frame if it's at 1-second intervals
            if frame_count % int(cap.get(cv2.CAP_PROP_FPS)) == 0:
                frame_filename = f"{video_file}_frame_{time_in_seconds}s.jpg"
                frame_path = os.path.join(output_folder, frame_filename)
                cv2.imwrite(frame_path, frame)

            # Increment the frame count
            frame_count += 1

    # Release the video capture object
    cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
