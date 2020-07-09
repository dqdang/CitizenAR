import re
import sys
import tkinter as tk
import tkinter as tk

fields = 'Text',


def spongebob(s):
    # s = re.sub("[^0-9a-zA-Z]+", "", s).replace("\"","").lower()
    # s = s.replace("\"","").lower()
    if s[0] == "\"" and s[-1] == "\"":
        s = s[1:-2]
    new_s = "\""
    s = s.lower().strip()
    for i in range(len(s)):
        if i % 2 != 0:
            new_s += s[i].upper()
        else:
            new_s += s[i]
    new_s += "\""
    return new_s


def fetch(root, entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        text = spongebob(text)
        res.configure(state=tk.NORMAL)
        res.delete(1.0, tk.END)
        res.insert(1.0, text)
        res.pack(expand=tk.TRUE, fill="both", padx=5, pady=5)
        res.configure(state=tk.DISABLED)
        # print('%s: "%s"' % (field, text))


def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


if __name__ == "__main__":
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(root, e)))
    b1 = tk.Button(root, text='Sponge',
                   command=(lambda e=ents: fetch(root, e)))
    res = tk.Text(root, height=25, borderwidth=0)
    res.configure(state=tk.DISABLED)
    res.configure(inactiveselectbackground=res.cget("selectbackground"))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
