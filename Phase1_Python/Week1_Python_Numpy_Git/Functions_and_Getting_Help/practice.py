# Write a function called calculate_grade
# It takes a score (number) as input
# It returns:
# "A" if score >= 90
# "B" if score >= 80
# "C" if score >= 70
# "Fail" if below 70
# Test it with scores: 95, 82, 71, 60


def CalculateGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "Fail"
    
# Example usage:
score = 95
grade = CalculateGrade(score)
print(f"The grade for a score of {score} is: {grade}")

# Write a function called calculate_bill
# It takes: price, quantity, and discount_percent
# It returns the final price after discount
# Example: price=1000, quantity=2, discount=10%
# Final = (1000 * 2) - 10% = 1800
# Test it with 3 different inputs
def CalculateBill(price, quantity, discount_percent):
    
    total = price * quantity
    discounted_amount = total * (discount_percent / 100)
    final_amount = total - discounted_amount
    return final_amount
# Example usage:
price = 550
quantity = 3
discount_percent = 8
final_bill = CalculateBill(price=price, quantity=quantity, discount_percent=discount_percent)
print("Price:",price,
      "\nQuantity:",quantity,
      "\nDiscount Percent:",discount_percent,
      "\nFinal Bill:",final_bill)

# Write a function called greet
# It takes a name and a greeting (default greeting = "Hello")
# It prints: "Hello, Ahmed!" or "Good Morning, Ahmed!"
# Call it once without a greeting, once with a greeting


def greet(name, greeting = "Hello"):


    return f"{greeting}, {name}!"
# Example usage:
print(greet("Alice"))  # Uses default greeting
print(greet("Bob", "Hi"))  # Uses custom greeting