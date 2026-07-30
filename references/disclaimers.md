# Disclaimers and honest limits

## The standard line

End substantive tax answers with something equivalent to:

> This is an estimate based on published tax year 2025 parameters, not tax
> advice. Confirm against [the authority] before filing or making a financial
> decision.

Adapt the wording to the answer. A one-line "what's my take-home in Berlin"
question does not need three sentences of hedging; a decision about which
country to move to does.

## What to be genuinely careful about

The parameters in `data/countries/` are a best-effort snapshot of tax year 2025.
They are not maintained by a tax authority and have not been professionally
reviewed. Every country file carries `sources` with the official URL. When the
stakes are real — a relocation, an equity sale, a regime election with a
deadline — say plainly that the figures should be checked against that source.

Being straight about this is more useful than hedging everything. "The bands
here are TY2025 and the top rate changed in the last budget, so check the
current table before you rely on this" tells the user something. "Consult a
professional" repeated five times tells them nothing.

## Things worth saying out loud when they apply

- **US citizens and green card holders** remain taxable on worldwide income
  wherever they live. Any answer about moving abroad that ignores this is wrong.
- **Leaving a country properly** is usually harder than arriving. Departure tax
  in Canada and Norway, the exit declaration in Brazil, ordinary residence in
  Ireland, the three-year rule in Finland, inhabitant tax in arrears in Japan.
- **Special regimes are elective and time-limited.** Beckham in Spain, the
  impatriate regimes in Italy and Portugal, the 30% ruling in the Netherlands,
  BIRTI in Belgium, the flat rate election in Korea. Missing the election window
  is permanent — Spain's six-month deadline cannot be fixed afterwards.
- **Treaties change the answer** for anyone with income or presence in more than
  one country, and the tie-breaker tests in a treaty override domestic residence
  rules. The engine models one country at a time and knows nothing about treaties.

## What the engine does not model at all

Wealth taxes, inheritance and gift tax, property taxes, VAT and consumption
taxes, corporate tax, payroll withholding schedules, treaty relief, foreign tax
credits, and most itemised deductions. It computes personal income tax and
social security on employment and self-employment income. Say so when it matters.

## What not to do

- Do not present a number to the cent as if it were an assessment.
- Do not answer a question about tax evasion, undeclared income, or hiding
  assets. Answering questions about *disclosure* routes — voluntary disclosure,
  late filing, amended returns — is the useful and appropriate thing to do, and
  is usually what the person actually needs.
- Do not guess at a rate that is not in the data. Say it is not covered and
  point at the source.
