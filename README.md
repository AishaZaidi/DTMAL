# Algorithm design
## Step 1: Conceptualization 
##### Contributors:(Muhammad Al-Waeli,Lilian Omolo,Stefan Ionica,Syeda Aisha Zaidi)
This dataset is part of our Assignment 2: Algorithm Design (Project Work) for the Datalogical thinking course. It is a curated metadata collection derived from open source digital book https://www.kaggle.com/datasets/lokeshparab/gutenberg-books-and-metadata-2025.
### Team Members & Roles
| Name | Role | Contribution |
|------|------|---------------|
| **Muhammad Al-Waeli** | Data Research Lead | Dataset selection and initial setup |
| **Syeda Aisha Zaidi** | Problem & Algorithm Lead | Designed problem logic and algorithm |
| **Lilian Omolo** | Data Engineer | Cleaned and validated dataset; supported algorithm design |
| **Stefan Ionica** | Documentation Lead | Website setup, documentation, and Python code |
## Step 2: Curation of our Dataset
##### Contributors:(Muhammad Al-Waeli,Lilian Omolo)
Dataset Overview
Column Name 
| Column Name | Description |
|--------------|-------------|
| **ID** | Unique identifier for each item in the dataset |
| **Type** | The kind of record (Text / Audio) |
| **Issued** | The year or date when the item was first published |
| **Title** | The title or name of the work |
| **Language** | The primary language of the work (e.g., English, French, German) |
| **Authors** | The creator(s) or main contributors of the work |
| **Subjects** | Thematic keywords or categories describing the content (e.g., Fiction, Science, History) |

##### Data Preparation Before Inclusion in the Repository

- The dataset was **cleaned and formatted** into a consistent CSV structure.  
- **Extra symbols, missing rows, and formatting errors** were removed.  
- All columns were checked to ensure **data consistency** (e.g., matching column headers and no blank identifiers).  
- Each record was validated to make sure the dataset met the **minimum requirement of 50+ entries**.
All records were validated to ensure at least **100 entries**, fulfilling assignment requirements.
**Intended Use:**
This dataset will be used to design and test an algorithmic model that processes bibliographic metadata.
**License & Usage:**
This dataset is intended for educational purposes only within the context of the Assignment 2 group project.
It is used under fair use for analysis, visualization, and algorithmic exploration.

## Step 3: Design Your Algorithm 
##### Contributors:(Lilian Omolo,Syeda Aisha Zaidi)

--- Step 1 – Setup

The dataset is loaded using read_csv("assignment2_dataset1.csv"), which reads all the book records into memory.

Several variables are initialized:

subjectTally → an empty dictionary that stores subjects as keys and their counts as values.

totalChecked → keeps track of the total number of records processed.

missingSubjects → counts how many records have empty or missing subject fields.

This step prepares all necessary data containers before the main loop starts.

Step 2 – Go Through Each Record

The algorithm uses a FOR loop (FOR each entry IN records DO) to go through each record (or row) in the dataset.

For every record, it increases the totalChecked variable by 1 to count that it has been processed.

This ensures every entry is analyzed exactly once.

Step 3 – Grab the Subject

The algorithm extracts the subject from the current record using:
subject ← trim(to_lowercase(entry["Subjects"]))

to_lowercase() ensures that “Fiction” and “fiction” are treated as the same value.

trim() removes any unnecessary spaces around the subject name.

This standardization step prevents counting errors caused by inconsistent capitalization or spacing.

Step 4 – Check if Subject Is Usable

Before counting, the algorithm checks if the subject value is not empty (IF subject ≠ "" THEN).

This prevents missing or blank subject fields from being added to the tally.

Only valid subject entries move on to the next step for counting.

Step 5 – Count It

The algorithm checks whether the subject already exists in the dictionary subjectTally:

If it does, its count is increased by 1.

If it does not, a new entry is created with an initial value of 1.

This logic ensures that every subject’s total occurrences are correctly tracked.

Step 6 – Note Missing Subjects

If the subject field was empty or invalid, the algorithm increases the missingSubjects counter by 1.

This allows the final report to include the number of incomplete records.

Step 7 – Find the Most Common One

After counting all subjects, the algorithm determines which subject appears most often.

It initializes:

topSubject → an empty string to hold the most common subject.

topCount → set to 0 as the starting comparison value.

The algorithm then loops through each subject in subjectTally:

If a subject’s count is higher than topCount, it updates topCount and topSubject.

At the end of this loop, topSubject contains the most frequent subject and topCount its frequency.

Step 8 – Show the Results

The algorithm prints a formatted summary report showing:

Each subject and its count.

The most frequent subject.

The total number of records processed.

The number of missing subject entries.

The final message — “Done analyzing!” — marks successful completion of the analysis.


## Step 4: Website 
##### Contributors:(Muhammad Al-Waeli,Lilian Omolo,Stefan Ionica)
The website was created following the steps below:  
- **Skeleton** creation.  
- Insertion of the body **content**  
- Building the general **structure**.
- **Attributes** team member information was included  
- Testing of final website to ensure interactivity
