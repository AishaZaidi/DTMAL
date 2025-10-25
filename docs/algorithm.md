# Algorithm: CountPopularSubjects
### Goal
Figure out which subject shows up the most in the library records.
## Pseudocode
BEGIN

    # Step 1: Setup
    # Load the data file
    records <- read_csv("data-cleaned.csv")   
    # maintain track of subject counts             
    subjectTally <- empty dictionary  
    # Total records looked at                     
    totalChecked <- 0                                      
    # Records without subject info
    missingSubjects <- 0   

# Step 2: Go through each record
    FOR each entry IN records DO
totalChecked <- totalChecked + 1
 # Step 3: Grab the subject
  subject <- trim(to_lowercase(entry["Subjects"]))
  # Step 4: Check if subject is usable
        IF subject != "" THEN
# Step 5: Count it
IF subject IN subjectTally THEN
subjectTally[subject] <- subjectTally[subject] + 1
ELSE
subjectTally[subject] <- 1
END IF
ELSE
# Step 6: Note missing subject
missingSubjects <- missingSubjects + 1
# Step 7: Find the most common one
    topSubject <- ""
    topCount <- 0

    FOR each subject IN subjectTally DO
        IF subjectTally[subject] > topCount THEN
            topCount <- subjectTally[subject]
            topSubject <- subject
# Step 8: Show the results
    PRINT "===== Subject Analysis Report ====="
    PRINT "Subjects and Their Counts:"

    FOR each subject IN subjectTally DO
        PRINT subject, "→", subjectTally[subject]
    END FOR

    PRINT "-----------------------------------"
    PRINT "Most Frequent Subject:", topSubject
    PRINT "Times Appeared:", topCount
    PRINT "Total Records Checked:", totalChecked
    PRINT "Records Missing Subject:", missingSubjects
    PRINT "Done analyzing!"
END IF

END FOR



