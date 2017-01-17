class Entry:

    def __init__(self, text, status = 0, reference = "", tags = [],
                 additional_field_1 = None,
                 additional_field_2 = None,
                 additional_field_3 = None):
        
        self.text = text
        self.status = status
        self.reference = reference
        self.tags = tags
        self.additional_field_1 = additional_field_1
        self.additional_field_2 = additional_field_2
        self.additional_field_3 = additional_field_3

    def do(self):
        self.status = 1
        
def copydb():
    with open('db.pkl', 'rb') as f:
        db = pickle.load(f)
        db.is_changed = False
    return db

def savedb(db, filename):
    copydb = copy.deepcopy(db)
    copydb.is_canged = False
    with open(filename, 'wb') as f:
        pickle.dump(copydb, f)

def convert(writing_pad):
    new_pages = []
    for page in writing_pad.pages:
        new_page = []
        for old_entry in page:
            entry = Entry(old_entry.text, old_entry.status)
            new_page.append(entry)
        newpages.append(new_page)
        
