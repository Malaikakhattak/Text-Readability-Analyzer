# Text Readability Analyzer

A Python-based **Text Analyzer** that analyzes written text and calculates its readability level using the **Flesch Reading Ease** and **Flesch-Kincaid Grade Level** formulas.

## Features

* Counts total words
* Counts sentences
* Estimates syllables
* Calculates Flesch Reading Ease score
* Calculates Flesch-Kincaid Grade Level
* Classifies text difficulty as Easy, Medium, or Hard
* Determines the corresponding education level
* Displays the complete calculation and final results

## Technologies Used

* Python
* Regular Expressions (`re`)
* Flesch Reading Ease Formula
* Flesch-Kincaid Grade Level Formula

## How to Run

Make sure Python is installed.

Run the program using:

```bash
python project.py
```

Enter your text when prompted.

The program will display the word, sentence, and syllable counts, followed by the readability calculations and final classification.

## Example Output

```text
Counts:
Words = 25
Sentences = 2
Syllables = 35

Flesch Reading Ease = 65.42
Flesch-Kincaid Grade = 7.21
Difficulty: Medium
Education Level: Secondary School
```

## Project Structure

```text
Text-Readability-Analyzer/
│
├── project.py
└── README.md
```

## Formulas Used

### Flesch Reading Ease

```text
206.835 - 1.015 × (Words / Sentences)
          - 84.6 × (Syllables / Words)
```

### Flesch-Kincaid Grade Level

```text
0.39 × (Words / Sentences)
+ 11.8 × (Syllables / Words)
- 15.59
```

## Project Type

**Text Analysis / Natural Language Processing Academic Project**

This project demonstrates basic text processing, statistical calculations, readability analysis, and classification using Python.
