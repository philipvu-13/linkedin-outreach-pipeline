# LinkedIn Outreach Pipeline

Turning a real job-search networking campaign into a data project, one step at a time.

## What this is

While job searching for data engineering roles, I ran cold outreach to data
professionals on LinkedIn and tracked what happened to every person I contacted.
This repo takes that raw tracking data and is slowly being rebuilt into an
automated data pipeline that ingests, cleans, and analyzes it.

It started as a spreadsheet. The goal is to rebuild it the way a data engineer
would, replacing each manual step with code as I go.

## The campaign, in plain terms

For each campaign I reached out to about 200 people and followed them through
five stages. Most people drop off at each stage, so the numbers shrink as you
read down. That shrinking shape is called a funnel.

- **Sent** – I sent a connection request
- **Accepted** – they accepted it
- **Replied** – they replied to my message
- **Booked** – they agreed to a call
- **Completed** – the call actually happened

## Results so far

Snapshot as of May 30, 2026. Both campaigns are still active, so contacts can
still accept, reply, or attend booked calls. These are current standings, not
final numbers. Contacts are anonymized; percentages are share of sent.

| Stage | Campaign 1 | Campaign 2 |
|---|---|---|
| Scraped leads | 200 | 194 |
| Sent | 191 | 186 |
| Accepted | 50 (26%) | 29 (16%) |
| Replied | 22 (12%) | 10 (5%) |
| Booked | 11 (6%) | 8 (4%) |
| Completed | 6 (3%) | 5 (3%) |

I source leads with a scraper, so some profiles turn out to be dead or
invalid. "Scraped" is everyone I pulled; "Sent" is who I could actually reach.
The gap (9 and 8) is bad source data the pipeline has to filter out.

Acceptance dropped from 26% to 16% between the two campaigns. Figuring out why,
whether it's targeting, messaging, or just noise from a small sample, is the
kind of question this project is being built to answer.

## Status

Building this in public, one piece at a time:

- [x] Capture real campaign data as structured files
- [ ] Compute funnel metrics in code
- [ ] Compare campaigns and segments
- [ ] Automate the data collection
- [ ] Load into a database with a proper transformation layer

## Data

The `data` folder holds one anonymized CSV per campaign, one row per contact.
Both files share the same funnel columns. Campaign 1 also records each contact's
seniority level; campaign 2 records city instead. Reconciling small differences
like that is part of the work.

## Stack

- Python today
- A database, transformation, and dashboard layer to come