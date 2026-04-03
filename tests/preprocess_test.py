from backend.audio_preprocessing.preprocess import preprocess_audio

# Test file name
file_name = "eps_6.mp3"

# Function call
output_path = preprocess_audio(file_name)

print("Preprocessing done! it work succesfully")
print("Output file:", output_path)