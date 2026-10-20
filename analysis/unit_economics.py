"""Illustrative order-level contribution calculator. Not Swiggy data."""
from dataclasses import dataclass

@dataclass
class OrderEconomics:
    platform_revenue: float
    variable_fulfilment_cost: float
    platform_funded_promotion: float
    support_refund_allowance: float

    def contribution(self) -> float:
        return (
            self.platform_revenue
            - self.variable_fulfilment_cost
            - self.platform_funded_promotion
            - self.support_refund_allowance
        )

def main():
    example = OrderEconomics(
        platform_revenue=70.0,
        variable_fulfilment_cost=42.0,
        platform_funded_promotion=10.0,
        support_refund_allowance=3.0,
    )
    incremental_orders = 10_000
    print("ILLUSTRATIVE ONLY — not Swiggy data")
    print(f"Contribution per order: ₹{example.contribution():.2f}")
    print(f"Contribution from {incremental_orders:,} truly incremental orders: "
          f"₹{example.contribution() * incremental_orders:,.2f}")
    print("Excludes fixed build cost, cannibalisation, taxes, and unmodelled costs.")

if __name__ == "__main__":
    main()
