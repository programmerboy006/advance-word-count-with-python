# Advanced Word Counter Project

A Python program that analyzes text files and provides detailed statistics including word count, character count, most frequent words, and more.

## 📁 Project Structure

```
advanced-word-counter/
├── advanced_word_counter.py    # Main program file
├── sample.txt                 # Sample text file for testing
├── README.md                  # This file
└── requirements.txt           # No external dependencies needed
```

## 🎯 What This Program Does

This program reads a text file and analyzes it to provide:

### Basic Statistics:
- **Total words**: How many words are in the file
- **Unique words**: How many different words appear
- **Characters**: Total characters with and without spaces
- **Lines**: Number of lines in the file
- **Average words per line**: Statistical measure

### Advanced Analysis:
- **Top 10 most frequent words**: Shows which words appear most often
- **Word frequency percentages**: What percentage of the text each word represents
- **Longest and shortest words**: Identifies extreme word lengths
- **Average word length**: Statistical measure of word sizes
- **Words appearing only once**: Unique words in the text

## 🔧 How to Run

### Prerequisites:
- Python 3.6 or higher installed on your computer
- A text file to analyze (sample.txt is provided)

### Steps:
1. **Download the files**: Save `advanced_word_counter.py` and `sample.txt` in the same folder
2. **Open terminal/command prompt**: Navigate to the folder containing the files
3. **Run the program**: 
   ```bash
   python advanced_word_counter.py
   ```
4. **Enter filename**: When prompted, type `sample.txt` (or any other .txt file)

## 📖 Understanding Method 2 (Step by Step)

### Step 1: File Reading
```python
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
```
- Opens the file safely using `with` statement
- `encoding='utf-8'` handles special characters
- Reads entire file content into memory

### Step 2: Basic Counting
```python
words = content.split()        # Split text into words
word_count = len(words)        # Count total words
char_count = len(content)      # Count all characters
line_count = len(content.split('\n'))  # Count lines
```
- `split()` separates text by whitespace (spaces, tabs, newlines)
- `len()` counts items in a list or characters in a string

### Step 3: Text Cleaning
```python
cleaned_words = []
for word in words:
    cleaned_word = word.translate(str.maketrans('', '', string.punctuation)).lower()
    if cleaned_word:
        cleaned_words.append(cleaned_word)
```
- **Purpose**: Remove punctuation and convert to lowercase for accurate counting
- **Example**: "Hello!" becomes "hello", "World." becomes "world"
- **Why**: So "Hello" and "hello!" are counted as the same word

### Step 4: Frequency Analysis
```python
from collections import Counter
word_freq = Counter(cleaned_words)
```
- **Counter**: Special dictionary that counts occurrences
- **Example**: `Counter(['apple', 'banana', 'apple'])` → `{'apple': 2, 'banana': 1}`
- **Result**: Each word paired with how many times it appears

### Step 5: Display Results
```python
for rank, (word, count) in enumerate(word_freq.most_common(10), 1):
    percentage = (count / len(cleaned_words)) * 100
    print(f"{rank:2d}. {word:<15} : {count:4d} times ({percentage:.1f}%)")
```
- **most_common(10)**: Gets the 10 most frequent words
- **enumerate(start=1)**: Adds ranking numbers starting from 1
- **Formatting**: Makes output neat and aligned

## 🧪 Sample Output

When you run the program with `sample.txt`, you'll see:

```
==================================================
📈 ADVANCED WORD COUNT ANALYSIS
==================================================
📁 File: sample.txt
📝 Total words: 234
🔤 Unique words: 156
📊 Total characters (with spaces): 1,456
📊 Total characters (without spaces): 1,123
📄 Total lines: 23
📏 Average words per line: 10.17

==============================
🏆 TOP 10 MOST FREQUENT WORDS
==============================
 1. the            :   15 times (7.4%)
 2. and            :   10 times (4.9%)
 3. of             :    8 times (3.9%)
 4. programming    :    7 times (3.4%)
 5. in             :    6 times (2.9%)
 6. text           :    5 times (2.5%)
 7. to             :    5 times (2.5%)
 8. analysis       :    4 times (2.0%)
 9. python         :    4 times (2.0%)
10. is             :    4 times (2.0%)
```

## 🎓 Learning Concepts

This project teaches you:

### 1. **File Handling**
- Opening and reading files safely
- Error handling for missing files
- Working with different file encodings

### 2. **String Manipulation**
- Splitting text into words
- Removing punctuation
- Converting case (uppercase/lowercase)

### 3. **Data Structures**
- **Lists**: Store words and cleaned words
- **Dictionaries**: Counter stores word frequencies
- **Tuples**: Used in enumerate and most_common

### 4. **Python Libraries**
- **string**: Access to punctuation characters
- **collections.Counter**: Easy frequency counting

### 5. **Basic Statistics**
- Calculating averages
- Finding maximums and minimums
- Percentage calculations

## 🚀 Extending the Project

Try these modifications to learn more:

### Easy Modifications:
1. **Change the number of top words**: Modify `most_common(10)` to show more or fewer words
2. **Add more file formats**: Support .docx or .pdf files
3. **Save results**: Write analysis to a new file

### Intermediate Modifications:
1. **Remove stop words**: Filter out common words like "the", "and", "of"
2. **Case sensitivity option**: Let users choose case-sensitive analysis
3. **Word length analysis**: Show distribution of word lengths

### Advanced Modifications:
1. **Multiple file analysis**: Compare multiple files
2. **Graphical output**: Create charts showing word frequencies
3. **Web interface**: Make it a web application

## 🐛 Common Issues and Solutions

### Problem: "File not found"
**Solution**: Make sure the text file is in the same folder as the Python script

### Problem: "UnicodeDecodeError"
**Solution**: The `encoding='utf-8'` parameter should handle most text files

### Problem: Numbers mixed with text
**Solution**: The current version treats numbers as words. You can modify the cleaning function to handle this

### Problem: Very large files are slow
**Solution**: For files larger than 100MB, consider processing in chunks

## 📚 Next Steps

After mastering this project:
1. Learn about regular expressions for advanced text processing
2. Explore natural language processing (NLP) libraries like NLTK or spaCy
3. Study machine learning techniques for text classification
4. Build web applications with Flask or Django

## 🤝 Contributing

Feel free to modify and improve this code! Some ideas:
- Add more statistical analysis
- Improve the user interface
- Add support for different file formats
- Create unit tests

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

---

**Happy coding! 🎉**