# 1. Define the classes with the same method name
class AudioFile:
    def play(self):
        print("Playing audio track...")

class VideoFile:
    def play(self):
        print("Displaying video frames...")

# 2. Create the objects
song = AudioFile()
movie = VideoFile()

# 3. Store them in a single list
playlist = [song, movie]

# 4. Demonstrate polymorphism using a single loop
for file in playlist:
    file.play()  # Python automatically calls the correct 'play' method
