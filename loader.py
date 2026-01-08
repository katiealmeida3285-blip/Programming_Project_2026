import csv
#this was the only way i could get basic tests to work without getting a unicode error message
#it also functioned well with my final code
def load_videos(path):
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)
    return data
