# LinkedIn Outreach Pipeline

Turning a real job-search networking campaign into a data project, one step at a time.

## Why I built this

Like a lot of new grads in this market, I started the usual way: mass applying.
After roughly 200 cold applications I had close to zero interviews. So I changed
tactics. Instead of firing resumes into the void, I went straight to the people
already doing the work.

The goal was to build my network and learn the data field directly from real
engineers and analysts, not blog posts. Cold outreach was the method: reach
professionals on LinkedIn, start conversations, and get on calls to learn how
they think about the work, the tools, and breaking in.

I tracked every contact like a funnel. Turning that tracking into a real data
pipeline is what this repo is about.

## What's in this repo

The project started as a spreadsheet. This repo takes that raw tracking data
and is slowly rebuilding it the way a data engineer would, replacing each
manual step with code as I go.

## The funnel, in plain terms

For each campaign I reached out to about 200 people and followed them through
five stages. Most people drop off along the way, so the numbers shrink as you
read down. That shrinking shape is the funnel.

- **Sent** – I sent a connection request (some scraped profiles were dead, so this is fewer than I pulled)
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

I source leads with a scraper, so some profiles turn out to be dead or invalid.
"Scraped" is everyone I pulled; "Sent" is who I could actually reach. Those 9
and 8 are bad source data the pipeline filters out.

Acceptance dropped from 26% to 16% between the two campaigns. Figuring out why,
whether it's targeting, messaging, or just noise from a small sample, is the
kind of question this project is being built to answer.

## Status

Building this in public, one piece at a time:

- [x] Capture real campaign data as structured files
- [x] Compute funnel metrics in code
- [ ] Compare campaigns and segments
- [ ] Automate the data collection
- [ ] Load into a database with a proper transformation layer

## How the campaign was run

- **Apify** – scraped lead lists from LinkedIn/Apollo
- **Google Sheets** – tracked every contact and outcome by hand
- **LinkedIn, Google Meet, Google Calendar** – outreach and calls

## Pipeline stack

The data side this project is rebuilding into:

- **Python** – reading and processing the data (current)
- **Database + transformation layer** – coming next
- **Dashboard** – coming later

## Data

The `data` folder holds one anonymized CSV per campaign, one row per contact.
Both files share the same funnel columns. Campaign 1 also records each contact's
seniority level; campaign 2 records city instead. Reconciling small differences
like that is part of the work.