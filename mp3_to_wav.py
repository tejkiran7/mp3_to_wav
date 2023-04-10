import sys
from pydub import AudioSegment

# Get the source and destination directories from command-line arguments
mp3_dir = sys.argv[1]
wav_dir = sys.argv[2]

# Create the destination directory if it does not exist
if not os.path.exists(wav_dir):
    os.makedirs(wav_dir)

# Iterate over each file in the MP3 directory
for mp3_file in os.listdir(mp3_dir):
    if mp3_file.endswith(".mp3"):
        mp3_path = os.path.join(mp3_dir, mp3_file)
        wav_path = os.path.join(wav_dir, mp3_file.replace(".mp3", ".wav"))
        # Load the MP3 audio clip using pydub
        audio = AudioSegment.from_file(mp3_path, format="mp3")
        
        # Export the audio clip as a WAV file
        audio.export(wav_path, format="wav")
        
        print(f"Converted {mp3_path} to {wav_path}")
