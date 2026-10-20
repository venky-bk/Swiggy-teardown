"""Synthetic food-delivery funnel example. Not Swiggy data."""
STAGES = [
    ("food_home_viewed", 100_000),
    ("restaurant_viewed", 60_000),
    ("item_added_to_cart", 24_000),
    ("checkout_started", 18_000),
    ("checkout_completed", 14_400),
    ("order_delivered", 13_200),
]

def main():
    print("ILLUSTRATIVE SYNTHETIC COUNTS — not Swiggy data")
    previous = None
    for stage, users_or_orders in STAGES:
        if previous is None:
            print(f"{stage:24s} {users_or_orders:>8,} (baseline)")
        else:
            rate = users_or_orders / previous * 100 if previous else 0
            print(f"{stage:24s} {users_or_orders:>8,} ({rate:5.1f}% of previous stage)")
        previous = users_or_orders
    print("\nImportant: real analysis must define consistent user/order denominators,")
    print("identity rules, attribution windows, event deduplication and cancellations.")

if __name__ == "__main__":
    main()
