
test_cash_flows = [-1000, 399, 400, 300, 748, 800]
discount_rate = 0.12  

def calculate_npv(drate, dcash_flows):
    total_npv = 0
    for t, cf in enumerate(dcash_flows):
       
        discounted_value = cf / (1 + drate)**t
        total_npv += discounted_value
    return total_npv

result = calculate_npv(discount_rate, test_cash_flows)
if result < 0:
    print(f"${result:.2f}, reject")
elif result >= 0:
    print(f"${result:.2f},accept")


