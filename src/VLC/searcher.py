import json

with open('data.json', 'r+') as f:
    data = json.load(f)

with open('keywords.txt', 'r+') as f:
    keywords = f.read()

keywords_array = keywords.split(";")
keywords_dict = { keywords_array[i] : 0 for i in range(0, len(keywords_array) ) }

count = 0

for commit in data:
    commit_message = commit["commit"]["message"]

    for keyword in keywords_array:
        if commit_message.lower().find(keyword) != -1:
            keywords_dict[keyword] += 1
            count = count + 1

print("count:", count)
print("\n")
print("keywords_dict:", keywords_dict)