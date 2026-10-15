
"""Run the core BrightCart analysis from validated CSV files."""

import argparse
from pathlib import Path

from brightcart.data_loader import load_brightcart_data
from brightcart.financials import validate_order_financials
from brightcart.recommendations import calculate_opportunities
from brightcart.budget_optimizer import optimize_marketing_budget


def run_analysis(data_dir, start_month="2024-01", end_month="2025-12"):
    """Load data, validate finances, and report key findings."""

    # Load the source datasets using our standalone module
    # and align Orders and Marketing to the requested months
    data = load_brightcart_data(
        data_dir=data_dir,
        start_month=start_month,
        end_month=end_month
    )

    # Audit all original Orders records, including
    # records outside the reporting period
    audit = validate_order_financials(data["orders"])

    # Stop immediately if the accounting equations
    # do not reconcile with the recorded financial fields
    if not audit["all_valid"]:
        raise ValueError(
            f"Financial reconciliation failed: {audit}"
        )

    # Use only Orders within the selected reporting period
    # to calculate the financial metrics in the report
    orders = data["financial_orders"]

    # Calculate order-level net revenue and contribution
    # without subtracting the separate marketing dataset
    net_revenue = orders["net_revenue"].sum()
    contribution = orders["profit"].sum()

    # Calculate a revenue-weighted contribution margin
    # and handle periods containing no recorded revenue
    margin = (
        contribution / net_revenue * 100
        if net_revenue != 0
        else float("nan")
    )

    # Model three hypothetical operating improvements
    # using the reusable recommendation calculator
    opportunities = calculate_opportunities(
        orders, improvement_pct=10
    )

    # Sum conditional savings over the reporting period
    # without describing them as realized improvements
    potential_savings = (
        opportunities["potential_savings"].sum()
    )

    # Generate two marketing budget scenarios
    # using the validated monthly marketing records
    marketing = data["financial_marketing"]

    # Skip optimization for periods with no marketing
    # rather than dividing by a zero advertising budget
    if marketing.empty:
        marketing_spend = 0.0
        marketing_cut = 0.0
        remaining_marketing = 0.0
    else:
        optimized = optimize_marketing_budget(
            marketing,
            reduction_pct=20,
            maximum_cut_pct=40
        )

        # Work in cents so reported budget values
        # reconcile exactly to the allocation model
        marketing_spend = (
            optimized["spend_cents"].sum() / 100
        )

        marketing_cut = (
            optimized["targeted_cut_cents"].sum() / 100
        )

        remaining_marketing = (
            marketing_spend - marketing_cut
        )

    # Present verified financial facts first
    print("BRIGHTCART — REPRODUCIBLE ANALYSIS REPORT")
    print("=" * 60)

    print(f"Reporting period: {start_month} to {end_month}")
    print(f"Source orders audited: {audit['orders_checked']:,}")
    print(f"Reporting-period orders: {len(orders):,}")

    print("\nVERIFIED ORDER FINANCIALS")
    print(f"Net revenue: ${net_revenue:,.2f}")
    print(f"Pre-marketing contribution: ${contribution:,.2f}")
    print(f"Contribution margin: {margin:.2f}%")
    print("Financial reconciliation: PASS")

    # Print the three hypothetical improvement scenarios
    # separately from the historical profit baseline
    print("\nHYPOTHETICAL OPERATING IMPROVEMENTS")

    for _, opportunity in opportunities.iterrows():
        print(
            f"{opportunity['recommendation']}: "
            f"${opportunity['potential_savings']:,.2f}"
        )

    print(
        f"Combined conditional opportunity: "
        f"${potential_savings:,.2f}"
    )

    # Report the marketing budget independently
    # because its attributed revenue does not
    # reconcile with recorded Orders revenue
    print("\nSEPARATE MARKETING BUDGET SCENARIO")
    print(f"Original budget: ${marketing_spend:,.2f}")
    print(f"Proposed reduction: ${marketing_cut:,.2f}")
    print(f"Remaining budget: ${remaining_marketing:,.2f}")

    print("\nLIMITATIONS")
    print("- Contribution is before marketing expenditure.")
    print("- Operating improvements are hypothetical.")
    print("- Marketing attribution is not reconciled to Orders.")
    print("- Budget cuts are not forecasts of increased profit.")

    # Return numerical metrics as well as printed output
    # so automated tests can verify this complete pipeline
    return {
        "orders_audited": audit["orders_checked"],
        "reporting_orders": len(orders),
        "net_revenue": float(net_revenue),
        "contribution": float(contribution),
        "potential_savings": float(potential_savings),
        "marketing_spend": float(marketing_spend),
        "marketing_cut": float(marketing_cut),
        "remaining_marketing": float(remaining_marketing)
    }


if __name__ == "__main__":

    # Read the location of the input data from the command line
    # defaulting to the directory containing this script
    parser = argparse.ArgumentParser(
        description="Run the BrightCart financial analysis."
    )

    parser.add_argument(
        "--data-dir",
        default=str(Path(__file__).resolve().parent),
        help="Directory containing the three BrightCart CSVs."
    )

    parser.add_argument(
        "--start-month",
        default="2024-01"
    )

    parser.add_argument(
        "--end-month",
        default="2025-12"
    )

    # Run the analysis with the requested data and dates
    args = parser.parse_args()

    run_analysis(
        args.data_dir,
        start_month=args.start_month,
        end_month=args.end_month
    )
