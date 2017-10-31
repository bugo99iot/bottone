import re


vowels=["a","e","o","u"]

def add_one(word):
    word = re.sub(r"[^A-Za-z]+", '', word)
    if len(word) > 2:
        if word[-1] in vowels:
            word = word[:-1]
        word = word + "one"
    else:
        word = word
    return word

if __name__ == "__main__":
    main()
