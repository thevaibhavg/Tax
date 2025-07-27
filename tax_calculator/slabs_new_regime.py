def calculate_tax_new_regime(income):
    """
    Calculate tax based on 2025-26 new regime slabs.
    No deductions considered except standard ₹50,000 for salary.
    """
    slabs = [
        (0, 3_00_000, 0.00),
        (3_00_001, 6_00_000, 0.05),
        (6_00_001, 9_00_000, 0.10),
        (9_00_001, 12_00_000, 0.15),
        (12_00_001, 15_00_000, 0.20),
        (15_00_001, float('inf'), 0.30),
    ]

    taxable_income = max(income - 50_000, 0)  # ₹50,000 standard deduction
    total_tax = 0
    breakdown = {}

    for lower, upper, rate in slabs:
        if taxable_income > lower:
            taxed = min(taxable_income, upper) - lower
            slab_tax = taxed * rate
            breakdown[f"{rate*100:.0f}%"] = round(slab_tax)
            total_tax += slab_tax

    return round(total_tax), breakdown
