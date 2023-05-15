import argparse
import itertools
import sys 

leet_dict = { 
    'a': ['4', '@', 'a', 'A'],
    'b': ['8', 'b', 'B'],
    'c': ['(', '[', '{', 'c', 'C'],
    'd': ['d', 'D'],
    'e': ['3', 'e', 'E'],
    'f': ['f', 'F'],
    'g': ['6', '9', 'g', 'G'],
    'h': ['h', 'H'],
    'i': ['1', '!', '|', 'i', 'I'],
    'j': ['j', 'J'],
    'k': ['k', 'K'],
    'l': ['1', '|', '7', 'l', 'L'],
    'm': ['m', 'M'],
    'n': ['n', 'N'],
    'o': ['0', 'o', 'O'],
    'p': ['p', 'P'],
    'q': ['q', 'Q'],
    'r': ['r', 'R'],
    's': ['$', '5', 's', 'S'],
    't': ['+', '7', 't', 'T'],
    'u': ['u', 'U'],
    'v': ['v', 'V'],
    'w': ['w', 'W'],
    'x': ['x', 'X'],
    'y': ['y', 'Y'],
    'z': ['2', 'z', 'Z']
}

def generate_leet_combinations(word):
    combinations = []
    for char in word:
        char_lower = char.lower()
        if char_lower in leet_dict:
            alternatives = leet_dict[char_lower]
            combinations.append(alternatives)
        else:
            combinations.append([char])

    wordlist = [''.join(comb) for comb in itertools.product(*combinations)]
    return wordlist

def main():
    parser = argparse.ArgumentParser(description='Generate Leet speak wordlist.')
    parser.add_argument('-w', '--word', help='Input word')
    parser.add_argument('-s', '--save', help='Save wordlist to file', metavar='FILENAME')
    parser.add_argument('-p', '--pad', type=int, help='Pad the output to the specified length')

    args = parser.parse_args()

    if args.word:
        user_word = args.word
    else:
        user_word = input("Enter a word: ")

    leet_wordlist = generate_leet_combinations(user_word)
    
    if args.pad:
        pad_len = args.pad
        if pad_len <= len(user_word):
            print("Pad length must be greater than input word length")
            sys.exit()
        else:
            padding = ['!', '$', '#']
            padding_combinations = [''.join(comb) for comb in itertools.product(padding, repeat=pad_len - len(user_word))]
            padded_wordlist = []
            for word in leet_wordlist:
                for pad in padding_combinations:
                    padded_wordlist.append(word + pad)
            leet_wordlist = padded_wordlist

    if len(leet_wordlist) > 100000:
        choice = input("The resulting wordlist has over 100,000 words. Do you still want to proceed? (y/n): ")
        if choice.lower() != 'y':
            print("Wordlist generation aborted.")
            sys.exit()
            
    if args.save:
        filename = args.save
        if not filename:
            parser.error("A filename must be provided when using the --save option.")
        with open(filename, 'w') as file:
            for word in leet_wordlist:
                file.write(word + '\n')
        print("Wordlist saved to", filename)
    else:
        for word in leet_wordlist:
            print(word)


if __name__ == '__main__':
    main()
