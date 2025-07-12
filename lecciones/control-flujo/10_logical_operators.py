has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("You are eligible for a loan.")

if has_good_credit or has_criminal_record:
    print("You are eligible for a loan, but with conditions.")
