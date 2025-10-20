# Algorithm: CountPopularSubjects
### Goal
Figure out which subject shows up the most in the library records.
## Pseudocode
BEGIN

    # Step 1: Setup
    records ← read_csv("csv-data.csv")                    # Load the data file
    subjectTally ← empty dictionary                       # maintain track of subject counts
    totalChecked ← 0                                      # Total records looked at
    missingSubjects ← 0                                   # Records without subject info
# Step 2: Go through each record
    FOR each entry IN records DO
totalChecked ← totalChecked + 1
 # Step 3: Grab the subject
  subject ← trim(to_lowercase(entry["Subjects"]))
  # Step 4: Check if subject is usable
        IF subject ≠ "" THEN
# Step 5: Count it
IF subject IN subjectTally THEN
subjectTally[subject] ← subjectTally[subject] + 1
ELSE
subjectTally[subject] ← 1
END IF
ELSE
# Step 6: Note missing subject
missingSubjects ← missingSubjects + 1
# Step 7: Find the most common one
    topSubject ← ""
    topCount ← 0

    FOR each subject IN subjectTally DO
        IF subjectTally[subject] > topCount THEN
            topCount ← subjectTally[subject]
            topSubject ← subject
END IF

END FOR


