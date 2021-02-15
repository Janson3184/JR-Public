import nltk
import string


whiteListedCharacters = string.digits + string.ascii_letters + string.punctuation

print(whiteListedCharacters)

lemmatizer = nltk.WordNetLemmatizer()
tokenized = nltk.tokenize.word_tokenize('The runners are very fast.  $somet˙∆˚¬˙¨ˆˆ¨ˆˆø￿ ˆˆ˚˚∆ ƒƒimes They are all obtuse.')

for token in tokenized:

    #print(lemmatizer.lemmatize(token))

    omit_word = False
    blacklisted_chars = []

    for char in token:
        if char not in whiteListedCharacters:
            omit_word = True
            blacklisted_chars.append(char)
    if omit_word:
        print(f'Token: {token}  \nBlacklisted: {blacklisted_chars}\n\n')
    else:
        print(f'{token} does not contain any blacklisted characters.')