# Exercise  1
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Exercise  2
def theme_park_entry(is_vip, has_ticket, age):
    if is_vip or (has_ticket and age > 18):
        return "Entry allowed"
    else:
        return "Entry denied"


# Exercise  3
def classify_score(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 70:
        result = "Good"
        if score == 89:
            result += " (Oru mark la Excellent miss!)"
    elif score >= 50:
        result = "Average"
        if score == 69:
            result += " (Oru mark la Good miss!)"
    else:
        result = "Fail"
    return result


# Exercise  4
if __name__ == "__main__":
    print("--- Exercise 1 ---")
    for n in [5, -3, 0]:
        print(n, "->", check_number(n))

    print("\n--- Exercise 2 ---")
    tests = [
        (True, False, 15),    # VIP -> allowed
        (False, True, 20),    # ticket + 18 mela -> allowed
        (False, True, 18),    # age > 18 illa -> denied
        (False, False, 30),   # ticket illa -> denied
    ]
    for vip, ticket, age in tests:
        print(f"VIP={vip}, Ticket={ticket}, Age={age} ->",
              theme_park_entry(vip, ticket, age))

    print("\n--- Exercise 3 ---")
    for s in [95, 90, 89, 75, 70, 69, 55, 50, 49, 0]:
        print(s, "->", classify_score(s))


