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
    records = 0
    
    with open("data/data-cleaned.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records += 1
            if row["Subjects"]:
                for subject in row["Subjects"].split("|"):
                    clean = subject.strip().lower()
                    if clean and filter_subjects(clean):
                        subjects[clean] = subjects.get(clean, 0) + 1
    
    # Sort by frequency
    sorted_subjects = sorted(subjects.items(), key=lambda x: x[1], reverse=True)
    
    print("Top subjects:")
    for subject, count in sorted_subjects[:20]:
        print(f"{count:2d}x {subject}")
    
    print(f"\nMost popular: {sorted_subjects[0][0]} ({sorted_subjects[0][1]}x)")
    print(f"Total records: {records}")
    print(f"Unique subjects: {len(subjects)}")

if __name__ == "__main__":
    main()