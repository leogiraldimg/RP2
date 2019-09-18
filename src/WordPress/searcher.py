import json
import unicodedata

with open('data.json', 'r+') as f:
    data = json.load(f)

with open('keywords_eler.txt', 'r+') as f:
    keywords = f.read()

keywords_array = keywords.split(";")
keywords_dict = { keywords_array[i] : 0 for i in range(0, len(keywords_array) ) }
commit_obj = ""

for commit in data:
    commit_message = commit["commit"]["message"]
    keywords_string = ""
    first_time = True

    for keyword in keywords_array:
        if commit_message.lower().find(keyword) != -1:
            keywords_dict[keyword] += 1

            if first_time == True:
                keywords_string += '"' + keyword + '"'
                first_time = False
            else:
                keywords_string += ',"' + keyword + '"'

    if keywords_string != "":           
        try:
            commit_obj_string = '{"id": "' + commit["sha"] + '", "message": "' + commit_message.replace("\n", "").replace('"', "").replace(':', "") + '", "url": "' + commit["html_url"] + '", "keywords": [' + keywords_string + ']}'
            print(commit_obj_string)
            commit_obj_loads = json.loads(commit_obj_string)
            commit_obj = json.dumps(commit_obj_loads, indent=2, sort_keys=True)
        except:
            continue

        with open('keywords_per_commit.json', 'a+') as f:
            f.write(commit_obj)            