# BrightCart — E-commerce Profitability & Decision Intelligence

A Python analytics portfolio project that investigates
e-commerce profitability, operational cost drivers,
customer returns, marketing efficiency, and budget decisions.

The project combines financial reconciliation, exploratory
analysis, interactive Jupyter dashboards, business scenario
modeling, and independent automated testing.

## Business questions

1. Which product categories generate the most contribution profit?
2. How does profitability differ across sales channels?
3. Where do shipping costs, platform fees, and refunds
   create pressure on margins?
4. How does reported marketing efficiency differ by platform?
5. How could the marketing budget be reduced by 20%?
6. Which operational improvements should management investigate?

## Dataset overview

The project uses three source datasets:

| Dataset | Records | Purpose |
|---|---:|---|
| Orders | 2,000 | Revenue, costs, returns, and profit |
| Products | 207 | Product catalog and pricing information |
| Marketing Spend | 144 | Monthly advertising performance |

The main analysis covers January 2024 through December 2025.

There are 1,997 Orders records in that reporting period.
Three January 2026 orders are excluded from shared-period
analysis but remain included in source financial validation.

Important: The Orders dataset does not contain a verified
product-level join key. The `items_ordered` field represents
quantity, not `product_id`. The project does not invent a
transaction-level Orders-to-Products relationship.

## Verified financial findings

Financial equations were reconciled across all 2,000
original Orders records with zero mismatches.

| Metric | January 2024 – December 2025 |
|---|---:|
| Analyzed orders | 1,997 |
| Gross revenue | $277,648.30 |
| Discounts | $21,050.80 |
| Refunds | $20,582.45 |
| Net revenue | $236,015.05 |
| Transaction costs | $179,795.50 |
| Pre-marketing contribution profit | $56,219.55 |
| Contribution margin | 23.82% |

Contribution profit means recorded net revenue less
recorded product, shipping, platform, and transaction costs.
It is not full-company net income.

### Category and channel insights

- Electronics had the highest recorded category
  contribution profit: $13,973.46.
- Books had the lowest recorded category
  contribution margin: 11.89%.
- Mobile App had the highest recorded channel
  contribution margin: 29.74%.
- Marketplace had a 13.03% contribution margin,
  with $7,949.69 in recorded platform fees.
- The overall returned-order rate was 7.21%,
  with $20,582.45 in recorded refunds.

## Marketing efficiency and budget scenarios

Marketing data covers six platforms across 24 months.

| Metric | Value |
|---|---:|
| Historical marketing spend | $503,506.14 |
| Reported attributed revenue | $8,146,615.20 |
| Reported overall attributed ROAS | 16.18x |
| Modeled 20% budget reduction | $100,701.23 |
| Remaining modeled budget | $402,804.91 |

Two allocation scenarios were evaluated:

- Equal reduction: proportional cuts across
  platform-month records.
- Targeted reduction: prioritizes lower historical
  reported ROAS, subject to a strict 40% maximum
  cut per platform-month.

Both scenarios meet the 20% overall budget target.
For the validated historical data, neither exceeds
the 40% per-record limit.

These are budget allocation simulations, not
forecasts of future advertising performance.

### Critical attribution limitation

Marketing-reported attributed revenue ($8.15 million)
does not reconcile with gross revenue recorded in Orders
($277,648.30), despite the aligned reporting period.

The underlying reporting scopes or attribution methods
have not been verified. Therefore:

- Reported attributed ROAS is not verified incremental ROI.
- Marketing conversions are not verified new customers.
- Marketing spend is not subtracted from the sampled
  Orders contribution profit to claim company net income.
- A budget reduction is not assumed to increase profit.

## Three management recommendations

The following are hypothetical 10% improvements applied
to recorded historical cost or refund amounts.

| Recommendation | Historical base | Modeled improvement |
|---|---:|---:|
| Improve Books shipping efficiency | $6,251.80 | $625.18 |
| Review Marketplace platform fees | $7,949.69 | $794.97 |
| Investigate Food & Beverage refunds | $3,504.56 | $350.46 |
| **Combined conditional opportunity** | | **$1,770.61** |

These figures cover the full 24-month period.
They are not annual savings estimates or guaranteed gains.
Implementation costs, customer behavior changes,
and possible sales effects are not modeled.

## Project structure

```text
Bright cart/
├── brightcart/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── financials.py
│   ├── recommendations.py
│   └── budget_optimizer.py
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_financials.py
│   ├── test_recommendations.py
│   └── test_budget_optimizer.py
├── reports/
├── run_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

The three input CSVs are expected at the project root
when using the default script configuration.
Only share those datasets publicly if redistribution
is permitted.

## Setup and execution

Use a conventional Python environment with a version
compatible with the dependency requirements.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the default analysis:

```bash
python run_analysis.py
```

Or specify a separate data directory:

```bash
python run_analysis.py --data-dir "/path/to/csv-files"
```

Analyze a different reporting period:

```bash
python run_analysis.py --start-month 2025-01 --end-month 2025-12
```

Run the independent test suite:

```bash
python -m unittest discover -s tests -t . -v
```

The original interactive dashboard was developed
inside Jupyter using pandas, Matplotlib, and ipywidgets.
A separately packaged dashboard application is not yet
included in this repository.

## Quality assurance

The project currently includes 24 passing independent
unit tests covering:

- Required data schemas and date filtering.
- Missing files and duplicate keys.
- Revenue, cost, and profit reconciliation.
- Executive opportunity calculations.
- Invalid scenario assumptions.
- Marketing budget target reconciliation.
- Low-ROAS prioritization and strict cut limits.
- Protection against unintended source-data changes.

The standalone `run_analysis.py` workflow also passed
integration checks against the original BrightCart data.

## Tools and skills

Python, pandas, Matplotlib, ipywidgets, unittest,
financial reconciliation, data validation,
exploratory analysis, sensitivity analysis,
budget optimization, and executive reporting.

## Current limitations

- Orders and Marketing attribution do not reconcile.
- No supported product-level transaction join exists.
- Budget scenarios do not estimate causal sales impact.
- Management improvements are hypothetical.
- The interactive notebook dashboards have not yet
  been packaged into a standalone application.
- The CSV datasets may require permission before
  public redistribution.

## Future improvements

- Add a documented dashboard notebook or application.
- Add an end-to-end pipeline integration test.
- Make operating improvement assumptions configurable
  from the command line.
- Improve budget optimizer safeguards for arbitrary
  equal-cut and maximum-cut configurations.
- Add a machine-readable report export and visual examples.
