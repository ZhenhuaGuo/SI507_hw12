import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0
def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []
        next_id = 0

    for each_entry in entries:
        if int(each_entry['id']) > next_id:
            next_id = int(each_entry['id']) + 1

def get_entries():
    global entries
    return entries


def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    next_id += 1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id_):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id 
    for entry in entries:
        if entry['id'] == id_:
            entry_deleted = entry
            break
    entries.remove(entry_deleted)
    for each_entry in entries:
        if each_entry['id'] > next_id:
            next_id = int(each_entry['id']) + 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def change_entry(id_, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id 
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    for entry in entries:
        if entry['id'] == id_:
            entry['text'] = text
            entry['timestamp'] = time_string
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
        