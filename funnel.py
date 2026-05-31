import csv
import glob
import os

# every campaign file lives in the data folder, named campaign_XX.csv
DATA = "data"

# the funnel stages, in order. each stage is (label, column, the value that counts)
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


def pct(n, base):
    return f"{n / base * 100:.1f}%" if base else "0.0%"


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
        print(f"  {label + ':':10} {n:<4} ({pct(n, sent)} of sent | {pct(n, prev)} from previous)")
        prev = n


def compare(results):
    # results is a list of (name, scraped, counts), one per campaign
    print("\n" + "=" * 50)
    print("Side-by-side comparison (% is share of sent)\n")

    metric_rows = ["Scraped", "Sent", "Accepted", "Replied", "Booked", "Completed"]

    def cell_value(metric, scraped, counts):
        if metric == "Scraped":
            return str(scraped)
        n = counts[metric]
        if metric == "Sent":
            return str(n)
        return f"{n} ({pct(n, counts['Sent'])})"

    # build the table as rows of text, starting with the header
    header = ["Stage"] + [name for name, _, _ in results]
    table = [header]
    for metric in metric_rows:
        table.append([metric] + [cell_value(metric, s, c) for _, s, c in results])

    # size each column to its widest cell so everything lines up
    widths = [max(len(row[i]) for row in table) for i in range(len(header))]

    for i, row in enumerate(table):
        print("  ".join(text.ljust(widths[j]) for j, text in enumerate(row)))
        if i == 0:
            print("  ".join("-" * w for w in widths))


files = sorted(glob.glob(os.path.join(DATA, "campaign_*.csv")))

results = []
for path in files:
    name = os.path.splitext(os.path.basename(path))[0].replace("_", " ").title()
    scraped, counts = funnel(load(path))
    results.append((name, scraped, counts))
    show(name, scraped, counts)

compare(results)