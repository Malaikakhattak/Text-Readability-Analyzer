# -------- FINAL TEXT ANALYZER WITH FULL OUTPUT --------

import re  

# -------- COUNT FUNCTIONS --------

def count_sentences(text):
    
    
    sentences = re.findall(r'[.!?]+', text)
 
    return max(1, len(sentences))
    
def count_words(text):
    
    return len(text.split())

def count_syllables(word):
   
    word = word.lower()
    
    vowels = "aeiouy"
    
    count = 0
    
    prev = False

    for char in word:
        
        if char in vowels:
           
            if not prev:
            
                
                count += 1
            
            prev = True
        
        else:
            prev = False

    if word.endswith("e"):
        
        count -= 1

    return max(1, count)

def total_syllables(text):
    
    return sum(count_syllables(w) for w in text.split())

# -------- CLASSIFICATION --------

def difficulty_level(score):

    if score >= 70:
        return "Easy"
    elif score >= 40:
        return "Medium"
    else:
        return "Hard"

def education_level(grade):
    
    if grade <= 5:
        return "Primary School"
    elif grade <= 10:
        return "Secondary School"
    elif grade <= 14:
        return "College"
    else:
        return "University"

# -------- MAIN --------

text = input("Enter your text:\n")

words = count_words(text)

sentences = count_sentences(text)

syllables = total_syllables(text)

# -------- CALCULATIONS --------

reading_ease = 206.835 - 1.015*(words/sentences) - 84.6*(syllables/words)
# Flesch Reading Ease formula apply kiya

grade = 0.39*(words/sentences) + 11.8*(syllables/words) - 15.59
# Flesch-Kincaid Grade formula apply kiya

difficulty = difficulty_level(reading_ease)

level = education_level(grade)

# -------- OUTPUT --------

print("\n" + "="*60)

print("📊 TEXT ANALYSIS WITH CALCULATION")


print("="*60)

print("\n🔹 Counts:")
print(f"Words = {words}")

print(f"Sentences = {sentences}")

print(f"Syllables = {syllables}")

print("\n🔹 Flesch Reading Ease Calculation:")
print(f"= 206.835 - 1.015*({words}/{sentences}) - 84.6*({syllables}/{words})")

print(f"= {round(reading_ease,2)}")

print("\n🔹 Flesch-Kincaid Grade Calculation:")
print(f"= 0.39*({words}/{sentences}) + 11.8*({syllables}/{words}) - 15.59")


print(f"= {round(grade,2)}")


print("\n🎯 Final Result:")
print(f"Flesch Reading Ease = {round(reading_ease,2)}")


print(f"Flesch-Kincaid Grade = {round(grade,2)}")
# final grade

print(f"Difficulty: {difficulty}")
# difficulty level show 

print(f"Education Level: {level}")
