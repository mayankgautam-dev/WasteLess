# WasteLess

WasteLess helps people reduce food waste with simple, practical decisions.

## Vision

Reduce waste. Shop smarter. Bin it right.

## Lean Canvas (Project Direction)

### Problem
1. People overbuy groceries and notice too late when food goes bad.
2. No simple way to track item freshness at home.
3. Recycling and disposal choices are often confusing.
4. Wasteful habits increase cost and environmental impact.

### Solution
1. Smart shopping support based on what users already have.
2. Item freshness guidance to act before expiry.
3. Built-in waste classification for better disposal decisions.

### Unique Value Proposition
- One app cycle: plan, track, reduce, and recycle.
- Useful for students and busy households without extra effort.
- Simple setup, practical from day one.

### Customer Segments
1. College students in hostels/PGs with tight budgets.
2. Young urban professionals with busy schedules.
3. Small shared homes trying to cut grocery bills.
4. Regular grocery shoppers who often discard unused food.

### Customer Relationships
1. Smooth first run (no steep learning curve).
2. Friendly expiry nudges before items go bad.
3. Optional weekly summaries (money saved, waste avoided).
4. In-app waste reduction tips.

### Channels
1. App Store / Google Play.
2. Instagram and short-form content.
3. College WhatsApp/Telegram communities.
4. Sustainability communities and referral word-of-mouth.

### Key Resources
1. Mobile app (iOS/Android).
2. Lightweight AI/rule engine.
3. Product and barcode data.
4. Small development/design team.
5. Low-cost cloud hosting.

### Key Metrics
- Active users
- Retention rate
- Waste reduced (kg/month)

### Cost Structure
1. Initial app development and maintenance.
2. AI model training and periodic updates.
3. Basic student-focused marketing and outreach.
4. Cloud/server costs.

### Revenue Streams
1. Free tier for core features.
2. Premium subscription for planning/stats/smart suggestions.
3. Brand partnerships with eco-friendly grocery products.
4. Future anonymized aggregate insights (opt-in only, privacy-safe).

## Current Repository Scope

This repository currently contains a student-friendly Python prototype:

- `wasteless_agent.py`
  - `analyze_items(items_list)` for freshness status and action suggestions
  - `suggest_purchase(existing_items, new_item)` for simple buy/no-buy guidance
  - `waste_category(item_name)` for wet/dry/unknown waste type
