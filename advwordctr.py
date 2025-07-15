import string
from collections import Counter

def count_words_advanced(filename):
    """
    Advanced word counter with frequency analysis
    
    This function does the following:
    1. Opens and reads a text file
    2. Counts basic statistics (words, characters, lines)
    3. Cleans the text by removing punctuation and converting to lowercase
    4. Counts how many times each word appears
    5. Shows the most common words
    
    Args:
        filename (str): Name of the text file to analyze
    """
    
    try:
        print(f"Opening file: {filename}")
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        print("File loaded successfully!")
        print(f"File size: {len(content)} characters")

        print("\nCalculating statistics...")
        words = content.split()
        word_count = len(words)
        char_count = len(content)
        char_count_no_spaces = len(content.replace(" ", ""))
        line_count = content.count("\n") + 1
        print("Cleaning text for analysis")
        
        cleaned_words = []
        for word in words:
            cleaned_words.append(word.translate(str.maketrans('', '', string.punctuation)).lower())

        print("Analyzing word frequencies")
        word_freq = Counter(cleaned_words)
        unique_words = len(word_freq)
        
        print(f"\n{'='*50}")
        print("ADVANCED WORD COUNT STATISTICS")
        print(f"{'='*50}")
        print(f"Total words: {word_count}")
        print(f"Total characters: {char_count}")
        print(f"Total characters (no spaces): {char_count_no_spaces}")
        print(f"Total lines: {line_count}")
        print(f"Unique words: {unique_words}")
        
        if unique_words > 0:
            avg_words_per_unique = word_count / unique_words
            print(f"Word variety ratio: {avg_words_per_unique:.2f}")
        
            print(f"\n{'='*30}")
            print("TOP 10 MOST FREQUENT WORDS")
            print(f"{'='*30}")
            
            for rank, (word, count) in enumerate(word_freq.most_common(10), start=1):
                percentage = (count / len(cleaned_words)) * 100
                print(f"{rank:2d}. {word:<15}: {count:>4d} times ({percentage:>5.1f}%)")
            
            print(f"\n{'='*30}")
            print("ADDITIONAL STATISTICS")
            print(f"{'='*30}")

            longest_word = max(cleaned_words, key=len)
            shortest_word = min(cleaned_words, key=len)
            avg_word_length = sum(len(word) for word in cleaned_words) / len(cleaned_words)
            print(f"Longest word: {longest_word}")
            print(f"Shortest word: {shortest_word}")
            print(f"Average word length: {avg_word_length:.2f}")
            
            words_appear_once = [word for word, count in word_freq.items() if count == 1]
            print(f"Words appearing only once: {len(words_appear_once)}")

        print(f"\n{'='*50}")
        print("ANALYSIS COMPLETE")
        print(f"{'='*50}")

    except FileNotFoundError:
        print(f"File not found: {filename}")
        print("Make sure the file exists in the same folder as the script")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function that runs the program
    """
    print("ADVANCED WORD COUNTER")
    print('='*40)
    print("This program provides advanced word count statistics for a text file")
    print()
    
    filename = input("Enter the name of the text file: ").strip()
    if not filename:
        print("Filename cannot be empty")
        return
    
    print()
    count_words_advanced(filename)
    
    print("\nThanks for using Advanced Word Counter!")
         
if __name__ == "__main__":
    main()
