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
    subjects = {}
    total_checked = 0
    missing_subjects = 0
    
    with open("data/data-cleaned.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_checked += 1
            if row["Subjects"]:
                for subject in row["Subjects"].split("|"):
                    clean = subject.strip().lower()
                    if clean and filter_subjects(clean):
                        subjects[clean] = subjects.get(clean, 0) + 1
            else:
                missing_subjects += 1
    
    # Sort by frequency
    sorted_subjects = sorted(subjects.items(), key=lambda x: x[1], reverse=True)
    
    # Find the most frequent subject
    if sorted_subjects:
        top_subject = sorted_subjects[0][0]
        top_count = sorted_subjects[0][1]
    else:
        top_subject = "None found"
        top_count = 0
    
    # Display results in the specified format
    print("===== Subject Analysis Report =====")
    print("Subjects and Their Counts:")
    
    for subject, count in sorted_subjects:
        print(f"{subject} -> {count}")
    
    print("-----------------------------------")
    print(f"Most Frequent Subject: {top_subject}")
    print(f"Times Appeared: {top_count}")
    print(f"Total Records Checked: {total_checked}")
    print(f"Records Missing Subject: {missing_subjects}")
    print("Done analyzing!")

if __name__ == "__main__":
    main()