import csv
import glob
import os

DATA = "data"

# funnel stages, in order: (label, column, the value that counts)
STAGES = [
    ("Accepted",  "Accepted?",       "Y"),
    ("Replied",   "Response",        "Yes"),
    ("Booked",    "Call Booked?",    "Y"),
    ("Completed", "Call Completed?", "Y"),
]

# columns we slice a campaign by; first one present in the file wins
DIMENSIONS = ["Seniority Tier", "City"]

# a segment needs at least this many sent to get its own row
MIN_SEGMENT = 10


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def cell(row, column):
    return (row.get(column) or "").strip()


def pct(n, base):
    return f"{n / base * 100:.1f}%" if base else "0.0%"


def print_table(header, rows):
    table = [header] + rows
    widths = [max(len(str(row[i])) for row in table) for i in range(len(header))]
    for i, row in enumerate(table):
        print("  ".join(str(t).ljust(widths[j]) for j, t in enumerate(row)))
        if i == 0:
            print("  ".join("-" * w for w in widths))


def funnel(rows):
    scraped = len(rows)
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
    print("\n" + "=" * 50)
    print("Side-by-side comparison (% is share of sent)\n")
    metrics = ["Scraped", "Sent", "Accepted", "Replied", "Booked", "Completed"]

    def cell_value(metric, scraped, counts):
        if metric == "Scraped":
            return str(scraped)
        n = counts[metric]
        if metric == "Sent":
            return str(n)
        return f"{n} ({pct(n, counts['Sent'])})"

    header = ["Stage"] + [name for name, _, _ in results]
    rows = [[m] + [cell_value(m, s, c) for _, s, c in results] for m in metrics]
    print_table(header, rows)


def find_dimension(rows):
    for d in DIMENSIONS:
        if d in rows[0]:
            return d
    return None


def segment(name, rows):
    dim = find_dimension(rows)
    if not dim:
        return

    # group the rows by their dimension value
    groups = {}
    for r in rows:
        groups.setdefault(cell(r, dim) or "(unknown)", []).append(r)

    seg = [(key, funnel(grp)[1]) for key, grp in groups.items()]
    seg.sort(key=lambda x: -x[1]["Sent"])

    big = [(k, c) for k, c in seg if c["Sent"] >= MIN_SEGMENT]
    small = [c for k, c in seg if c["Sent"] < MIN_SEGMENT]

    print(f"\n{name} by {dim} (groups with at least {MIN_SEGMENT} sent)")
    header = ["Segment", "Sent", "Accepted", "Replied", "Booked", "Completed"]
    rows_out = []
    for k, c in big:
        s = c["Sent"]
        rows_out.append([k, s, f"{c['Accepted']} ({pct(c['Accepted'], s)})",
                         f"{c['Replied']} ({pct(c['Replied'], s)})", c["Booked"], c["Completed"]])

    # roll every too-small group into one "Other" line so totals still add up
    if small:
        ss = sum(c["Sent"] for c in small)
        agg = {m: sum(c[m] for c in small) for m in ["Accepted", "Replied", "Booked", "Completed"]}
        rows_out.append([f"Other ({len(small)} small)", ss,
                         f"{agg['Accepted']} ({pct(agg['Accepted'], ss)})",
                         f"{agg['Replied']} ({pct(agg['Replied'], ss)})", agg["Booked"], agg["Completed"]])

    print_table(header, rows_out)


files = sorted(glob.glob(os.path.join(DATA, "campaign_*.csv")))

results = []
for path in files:
    name = os.path.splitext(os.path.basename(path))[0].replace("_", " ").title()
    scraped, counts = funnel(load(path))
    results.append((name, scraped, counts))
    show(name, scraped, counts)

compare(results)

for path in files:
    name = os.path.splitext(os.path.basename(path))[0].replace("_", " ").title()
    segment(name, load(path))