from collections import Counter
def word_frequency(sentence):
    words=sentence.lower().split()


    frequency={}
    for word in words:
        if word in frequency:
            frequency[word]=+1
        else:
            frequency[word]=1
    return frequency

sentance="Python is easy and python is poweful "

result= word_frequency(sentance)


# Sort by frequency
sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

print(sorted_result)


# Explore Section using Counter
counter_result = Counter(words for words in sentance.lower().split())

print(counter_result)
