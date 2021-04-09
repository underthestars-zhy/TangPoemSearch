import os
import pprint

import json

if __name__ == '__main__':
    search_word = '人'
    all_poems = []
    count = 0

    all_file = os.listdir('./json')
    for file in all_file:
        if file[-4:] == 'json':
            with open('./json/' + file) as f:
                json_list = json.load(f)
                for json_dict in json_list:
                    p = ''
                    for a_p in json_dict['paragraphs']:
                        p += a_p
                    if search_word in p:
                        all_poems.append(json_dict)
                        count += 1
                        break

    with open('./poems.json', 'w') as f:
        json.dump(all_poems, f, ensure_ascii=False, indent=4)
