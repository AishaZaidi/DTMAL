import csv
import re

def filter_subjects(subject):
    # Skip library classification codes  
    s = subject.strip()
    if len(s) <= 3:
        return False
    if re.match(r'^[a-z]*\d+[a-z]*$', s):
        return False  
    if re.match(r'^[a-z]{1,4}$', s):
        return False
    return True

def main():
    subjectTally = {}
    totalChecked = 0
    missingSubjects = 0
    
    with open("data/data-cleaned.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            totalChecked += 1
            if row["Subjects"]:
                for subject in row["Subjects"].split("|"):
                    clean = subject.strip().lower()
                    if clean and filter_subjects(clean):
                        subjectTally[clean] = subjectTally.get(clean, 0) + 1
            else:
                missingSubjects += 1
    
    # Sort by frequency
    sorted_subjects = sorted(subjectTally.items(), key=lambda x: x[1], reverse=True)
    
    # Find the most frequent subject
    if sorted_subjects:
        topSubject = sorted_subjects[0][0]
        topCount = sorted_subjects[0][1]
    else:
        topSubject = "None found"
        topCount = 0
    
    # Display results in the specified format
    print("===== Subject Analysis Report =====")
    print("Subjects and Their Counts:")
    
    for subject, count in sorted_subjects:
        print(f"{subject} -> {count}")
    
    print("-----------------------------------")
    print(f"Most Frequent Subject: {topSubject}")
    print(f"Times Appeared: {topCount}")
    print(f"Total Records Checked: {totalChecked}")
    print(f"Records Missing Subject: {missingSubjects}")
    print("Done analyzing!")

if __name__ == "__main__":
    main()