import csv
from log_classifier import classify_log_error

correct = 0
total = 0



with open('eval_set.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        predicted=classify_log_error(row['line'])
        expected=row['expected']
        total += 1
        if predicted == expected:
            correct += 1
            print(f"PASS | {expected:8} | {row['line']}")
        else:
            print(f"FAIL | expected {expected}, got {predicted} | {row['line']}")
print(f"Accuracy: {correct}/{total} = {correct/total}")
