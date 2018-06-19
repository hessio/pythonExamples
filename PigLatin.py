import sys

vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])

def pigLatin(word):
    if word[0] in vowels:
        return word + 'yay'
    else:
        for i, c in enumerate(word):
            if c in vowels:
                return word[i:] + word[:i] + 'ay'
    
    return None

def main():
    for line in sys.stdin:
        if len(line) == 0:
            continue
        print(' '.join(map(pigLatin, line.split())))

if __name__ == "__main__":
    main()
