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

For each campaign I reach out to about 200 people and follow them through five
stages. Most people drop off along the way, so the numbers shrink as you read
down. That shrinking shape is the funnel.

- **Sent** – I sent a connection request (some scraped profiles were dead, so this is fewer than I pulled)
- **Accepted** – they accepted it
- **Replied** – they replied to my message
- **Booked** – they agreed to a call
- **Completed** – the call actually happened

## The campaigns

Each campaign targets a different audience, which matters a lot when reading the
numbers below. The point isn't to run one big blast; it's to see how different
groups of people respond to the same kind of outreach.

- **Campaign 1** – Data engineers (split by seniority: Senior DE, Analytics, Entry/Junior)
- **Campaign 2** – Analytics engineers
- **Campaign 3** – Technical recruiters in the data space
- **Campaign 4** – Founders of AI startups and companies that lean heavily on data

## Results so far

Snapshot as of June 14, 2026. Campaigns are still active, so contacts can still
accept, reply, or attend booked calls. Campaigns 3 and 4 went out most recently,
which is why their later stages are still empty. These are current standings, not
final numbers. Contacts are anonymized; percentages are share of sent.

| Stage | C1 (Data Eng) | C2 (Analytics Eng) | C3 (Recruiters) | C4 (Founders) |
|---|---|---|---|---|
| Scraped leads | 200 | 206 | 203 | 204 |
| Sent | 191 | 186 | 189 | 193 |
| Accepted | 51 (27%) | 39 (21%) | 25 (13%) | 25 (13%) |
| Replied | 22 (12%) | 12 (7%) | 0 (0%) | 0 (0%) |
| Booked | 12 (6%) | 8 (4%) | 0 (0%) | 0 (0%) |
| Completed | 9 (5%) | 7 (4%) | 0 (0%) | 0 (0%) |

I source leads with a scraper, so some profiles turn out to be dead or invalid.
"Scraped" is everyone I pulled; "Sent" is who I could actually reach. The gap
between the two is bad source data the pipeline filters out.

### Reading the acceptance rate

Acceptance falls from 27% to 13% across the four campaigns, but that isn't a
straight decline in outreach quality. Each campaign is a different audience.
Working engineers and analysts (Campaigns 1 and 2) accept at a noticeably higher
rate than recruiters and founders (Campaigns 3 and 4), who get far more inbound
and are harder to reach. Separating audience effects from messaging effects is
exactly the kind of question this project is being built to answer.

## Status

Building this in public, one piece at a time:

- [x] Capture real campaign data as structured files
- [x] Compute funnel metrics in code
- [x] Compare campaigns and segments
- [ ] Automate the data collection
- [ ] Load into a database with a proper transformation layer

## How the campaigns were run

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
All files share the same funnel columns. Campaign 1 records each contact's
seniority tier; Campaigns 2 through 4 record city instead. Reconciling small
differences like that is part of the work.
