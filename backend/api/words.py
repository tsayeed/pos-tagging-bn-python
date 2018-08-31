import random
import sys
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
words_filepath = os.path.join(file_dir, "words.txt")

def generate(filename= words_filepath, count=200):
    with open(filename, "r") as file:
        lines = file.readlines()
        words = [word.strip() for word in lines]
        words = random.sample(words, count)
        return words



if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) == 2 else 200
    
    print("words = ", end='')
    print(generate(count=count))
