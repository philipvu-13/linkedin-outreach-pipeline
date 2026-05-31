import csv
import glob
import os

# every campaign file lives in the data folder, named campaign_XX.csv
DATA = "data"

# the five funnel stages, in order. each stage is (label, column, the value that counts)
STAGES = [
    ("Accepted",  "Accepted?",       "Y"),
    ("Replied",   "Response",        "Yes"),
    ("Booked",    "Call Booked?",    "Y"),
    ("Completed", "Call Completed?", "Y"),
]


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def cell(row, column):
    return (row.get(column) or "").strip()


def funnel(rows):
    scraped = len(rows)
    # "sent" = rows where I actually sent a request (has a date)
    sent = sum(1 for r in rows if cell(r, "Connection Sent Date"))

    counts = {"Sent": sent}
    for label, column, value in STAGES:
        counts[label] = sum(1 for r in rows if cell(r, column) == value)

    return scraped, counts


def show(name, scraped, counts):
    sent = counts["Sent"]
    print(f"\n{name}")
    print(f"  Scraped:   {scraped}")
    print(f"  Sent:      {sent}")

    prev = sent
    for label, _, _ in STAGES:
        n = counts[label]
        of_sent = n / sent * 100
        of_prev = n / prev * 100 if prev else 0
        print(f"  {label + ':':10} {n:<4} ({of_sent:.1f}% of sent | {of_prev:.1f}% from previous)")
        prev = n


files = sorted(glob.glob(os.path.join(DATA, "campaign_*.csv")))
for path in files:
    name = os.path.splitext(os.path.basename(path))[0].replace("_", " ").title()
    scraped, counts = funnel(load(path))
    show(name, scraped, counts)