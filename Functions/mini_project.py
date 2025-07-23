# Mini Project Using Functions

def server_cost_calculator(hours, rate=0.51):
    return hours * rate

def display_costs():
    daily = server_cost_calculator(24)
    weekly = server_cost_calculator(24 * 7)
    monthly = server_cost_calculator(24 * 30)
    budget_days = 918 / daily

    print(f"Daily cost: ${daily:.2f}")
    print(f"Weekly cost: ${weekly:.2f}")
    print(f"Monthly cost: ${monthly:.2f}")
    print(f"With $918, you can run the server for {budget_days:.2f} days.")

display_costs()
