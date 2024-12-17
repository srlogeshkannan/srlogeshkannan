def text_to_emoji(text):
    # Define a dictionary of words to emojis
    emoji_dict = {
        "happy": "😊",
        "sad": "😢",
        "love": "❤",
        "fire": "🔥",
        "heart": "💖",
        "laugh": "😂",
        "cool": "😎",
        "angry": "😠",
        "star": "⭐",
        "sun": "☀",
        "moon":"🌜",
        "music":"🎼",
        "think":"🤔",
        "shy" : "😳",
        "done":"👍🏻",
        "super":"👌",
        "wow":"😍",
        "cloud":"☁️"
    }
    
    # Split text into words and replace with emojis if available
    words = text.split()
    converted = [emoji_dict.get(word.lower(), word) for word in words]
    
    # Join the words back into a sentence
    return " ".join(converted)

# Example usage
text = "I am happy to see the moon covered by stars and clouds"
result = text_to_emoji(text)
print(result)
