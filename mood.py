mood_songs = {
    "happy": ["Here Comes the Sun", "Walking on Sunshine", "I'm Feeling Good"],
    "sad": ["Tears in Heaven", "Someone Like You", "Hallelujah"],
    "energetic": ["Eye of the Tiger", "We Will Rock You", "Uptown Funk"],
    "relaxed": ["Weightless", "Nature Sounds", "Rainy Days and Mondays"]
}

mood = input("Enter your current mood (happy, sad, energetic, relaxed): ")

if mood in mood_songs:
    print(f"Here's a playlist for you: {', '.join(mood_songs[mood])}")
else:
    print("Invalid mood. Try again!")