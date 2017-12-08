import json
import pandas as pd
import sys

def analysis(file_name, user_id):
    times = 0
    minutes = 0
    with open(file_name) as f:
        for item in json.load(f):
            if item['user_id'] == user_id:
                times += 1
                minutes += item['minutes']
    return times,minutes

if __name__ == '__main__':
    file_name = sys.argv[1]
    user_id = int(sys.argv[2])
    analysis_data = analysis(file_name,user_id)
    print(user_id,analysis_data[0], analysis_data[1])

