# Week 3 | Class 02: Probability, conditional probability and Bayes' rule

# Example: a test detects a condition.
prevalence = 0.02            # P(condition)
sensitivity = 0.95           # P(positive | condition)
false_positive_rate = 0.05   # P(positive | no condition)

p_positive = (sensitivity * prevalence +
              false_positive_rate * (1 - prevalence))
p_condition_given_positive = sensitivity * prevalence / p_positive

print("P(condition):", prevalence)
print("P(positive):", round(p_positive, 4))
print("P(condition | positive):", round(p_condition_given_positive, 4))

# Joint, marginal and conditional probabilities with a tiny table
records = [
    {"subscribed": True, "digital": True},
    {"subscribed": True, "digital": False},
    {"subscribed": True, "digital": True},
    {"subscribed": False, "digital": True},
    {"subscribed": False, "digital": False},
    {"subscribed": False, "digital": False},
]
n = len(records)
p_digital = sum(r["digital"] for r in records) / n
p_subscribed = sum(r["subscribed"] for r in records) / n
both = sum(r["subscribed"] and r["digital"] for r in records) / n
conditional = both / p_subscribed if p_subscribed else 0

print("\nP(digital):", round(p_digital, 3))
print("P(subscribed):", round(p_subscribed, 3))
print("P(subscribed and digital):", round(both, 3))
print("P(digital | subscribed):", round(conditional, 3))
