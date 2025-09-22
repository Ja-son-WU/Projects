with open ("sample.txt","r", encoding="utf-8") as f:
    text= f.read().lower()

print(text)


for ch in ".,!?":
    text = text.replace(ch, " ")
words = text.split()


freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1


for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(word, ":", count)