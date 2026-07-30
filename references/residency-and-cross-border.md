# Residence and cross-border situations

Most genuinely hard tax questions are residence questions wearing a disguise.
Someone asking "how much tax will I pay on €120k in Lisbon" often has an
unasked question underneath: whether they are still tax resident somewhere else.

## The 183-day rule is the exception, not the rule

Counting days is only decisive in some countries. The tests that actually apply:

| Test | Where it dominates |
| --- | --- |
| Day count alone | Poland, Czechia, Spain, Portugal, Korea, Japan |
| Available home | Germany, Austria, Switzerland, Denmark, Luxembourg — a flat you keep can make you resident with few days present |
| Centre of vital interests | France, Italy, Belgium, Poland (alternative test) |
| Permanent place of abode | New Zealand — overrides the day count entirely |
| Multi-factor statutory test | United Kingdom (Statutory Residence Test) |
| Residential ties | Canada |
| Citizenship | United States — the only major country taxing citizens abroad |

Two consequences follow. First, you can be resident in two countries at once
under their domestic rules. Second, you can fail to become non-resident in the
country you left, which is the more expensive mistake.

## Order of analysis for a cross-border question

1. **Domestic residence in each country** — apply each country's own test.
2. **Treaty tie-breaker if both say yes** — the standard sequence is permanent
   home, then centre of vital interests, then habitual abode, then nationality,
   then mutual agreement.
3. **Source rules** — which country may tax each item of income.
4. **Relief** — exemption with progression, or foreign tax credit.
5. **Social security** — governed by separate agreements (EU Regulation 883/2004,
   bilateral totalisation agreements) and it does *not* follow the tax treaty.
   You can be tax resident in one country and in another's social security system.

## Split years

Some countries tax you as resident for only part of the year of arrival or
departure (UK, Ireland, Netherlands, Germany in effect, Canada, Australia).
Others do not: **Spain has no split year at all** — arrive on 1 July and stay,
and you are resident for the whole calendar year including foreign income earned
before you moved. Portugal, France and Italy have partial-year mechanisms that
depend on the facts.

This single point changes the optimal moving date by months. It is worth raising
unprompted whenever someone mentions a planned move.

## Traps worth raising unprompted

- **Departure tax**: Canada and Norway deem a disposal of assets on ceasing
  residence. Japan has an exit tax above ¥100m of financial assets. The US has
  section 877A for covered expatriates.
- **Trailing residence**: Ireland's ordinary residence continues three years
  after leaving. Finland presumes residence for three years after departure for
  its own citizens. Brazil keeps you resident indefinitely without a formal exit
  declaration.
- **Tax in arrears**: Japanese inhabitant tax is billed the following June for
  the year just ended, so leaving generates a bill after you have gone.
- **Foreign asset reporting** is separate from income tax and separately
  penalised nearly everywhere. See `references/reporting-workflow.md`.
- **The 30%/50% inbound regimes** across Europe are elective, time-limited, and
  usually require you not to have been resident recently. They are the single
  largest lever for someone relocating, and they have hard application windows.

## What the engine can and cannot do here

`taxcalc` models one country at a time on the assumption that the person is
resident there for the full year. It applies no treaty relief and no foreign tax
credit. For a cross-border question, run each country separately, then reason
about relief explicitly — and say that is what you did.
