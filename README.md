# Python Tests Solutions

This repository contains solutions to two Python test problems:
1. **Regular Expression String Validation**
2. **Word Frequency Counter**

## 📜 Problem 1: String Validation using Regular Expressions
This script checks if a given string meets the following criteria:
- At least **6 characters long**
- Contains **2 to 3 numbers**
- Numbers must be **separated by at least one non-numeric character**
- No consecutive numbers allowed

### 🔹 File: `string_validator.py`
### 🚀 Usage:
Run the script and test different input cases:
```bash
python string_validator.py
```
Example:
```python
print(is_valid_string("a1b2c3"))   # True
print(is_valid_string("123abc"))   # False
```

---

## 📜 Problem 2: Word Frequency Counter
This script reads a text input, counts the frequency of each word, and displays them in **descending order of frequency**.

### 🔹 File: `word_frequencies.py`
### 🚀 Usage:
Run the script with any text input:
```bash
python word_frequencies.py
```
Example:
```python
text = "Hello world! This is a test. Hello, this test is only a test."
frequencies = word_frequencies(text)
print(frequencies)
```
Output:
```
test: 3
hello: 2
this: 2
is: 2
a: 2
world: 1
only: 1
```

---

## 📂 Repository Structure:
```
📦 Python-Tests
 ┣ 📜 string_validator.py
 ┣ 📜 word_frequencies.py
 ┗ 📜 README.md
```

---

## 🛠 Requirements  
- Python 3.x  
- No external libraries required (uses `re` and `collections.Counter` from Python's standard library)

## 📌 How to Clone and Run
1. Clone this repository:  
   ```bash
   git clone https://git@github.com:code-iddih/python_test_solutions.git
   ```
2. Navigate into the folder:
   ```bash
   cd repository-name
   ```
3. Run the scripts:
   ```bash
   python string_validator.py
   python word_frequencies.py
   ```

---

## 📧 Contact  
For any questions or improvements, feel free to reach out! 😊  

---


