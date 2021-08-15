word =""

for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))