# Group 9's Book Subject Analysis Project
## Assignment 2: Algorithm Design (Project Work) - Datalogical Thinking Course

Hi! We are Group 9, and this is our complete submission for Assignment 2. We analyzed a dataset of books from Project Gutenberg to determine which subjects appear most frequently in the collection.
Please do not forget to check out our website: https://aishazaidi.github.io/DTMAL/index.html

## Assignment Completion Overview

We have successfully completed all required steps:
- **Step 1**: Conceptualized our approach and selected an appropriate dataset
- **Step 2**: Curated and cleaned our dataset (99 records, well-formed CSV)
- **Step 3**: Designed our algorithm (50+ lines, includes variables, selections, and iterations)
- **Step 4**: Built a 4-page website with navigation and motivations for our choices
- **Step 5**: Published everything on GitHub with GitHub Pages hosting

## What is In Our Project

Here is everything we have built for this assignment:
- **`count_popular_subjects.py`** - Our main Python script that implements the algorithm
- **`data-cleaned.csv`** - Our curated dataset (Excel compatible, 99 records)
- **`algorithm.md`** - Detailed pseudocode of our algorithm (50+ lines)
- **`docs/`** folder - Complete 4-page website with navigation
- **`data/`** folder - All data files including original and processed versions

## Step 1: Conceptualization

**Problem Definition**: We identified a clear algorithmic problem - determining which book subjects appear most frequently in a large literary dataset.

**Dataset Selection**: We chose the Gutenberg Books metadata from Kaggle, which contains structured information about books including subjects, authors, titles and publication data.

**Data Model Understanding**: We analyzed the dataset structure and determined that the "Subjects" column would be our primary focus, requiring preprocessing to handle multiple subjects per book and standardization of subject names.

## Step 2: Dataset Curation

**Dataset Requirements Met**:
- **99 items** (far exceeding the 50 minimum requirement)
- **Well-formed data** (clean CSV format, no syntactical errors, Excel compatible)
- **Properly modeled** for our algorithm needs

**Data Preparation Process** (Led by Lilian Omolo):
- Cleaned original Kaggle dataset to remove formatting inconsistencies
- Standardized column headers and data types
- Created `data-cleaned.csv` which is Excel-compatible
- Ensured data structure supports efficient subject analysis

**Final Dataset**: Located in `data/data-cleaned.csv` - ready for algorithmic processing  

## Step 3: Algorithm Design

**Algorithm Requirements Met**:
- **50+ lines** of code (see `algorithm.md` and `count_popular_subjects.py`)
- **Variables**: `subjectTally`, `totalChecked`, `missingSubjects`, `topSubject`, `topCount`
- **Selections**: IF-ELSE statements
- **Iterations**: FOR loops for processing records and finding most frequent subject

**Algorithm Overview** (Designed by Syeda Aisha Zaidi):
Our algorithm systematically processes each book record to count subject frequencies:

**1. Initialization**
- Load dataset from `data-cleaned.csv`
- Initialize counters and data structures

**2. Data Processing Loop**
- Iterate through each book record
- Extract and clean subject information
- Handle missing or invalid data appropriately

**3. Subject Counting**
- Use dictionary to track subject frequencies
- Normalize subject names (lowercase, trim spaces)
- Count multiple subjects per book separately

**4. Analysis**
- Find the most frequently occurring subject
- Generate comprehensive statistics

**5. Results Output**
- Display all subjects with their counts
- Show most popular subject and frequency
- Report total records processed and missing data

**Implementation**: Available in both pseudocode (`algorithm.md`) and working Python code (`count_popular_subjects.py`).

## Step 4: Website Design

**Website Requirements Met**:
- **4+ linked web pages** with navigation bar
- **Motivations included** for all design choices
- **Complete project documentation**

**Website Structure** (Built by Stefan Ionica):
- **`index.html`** - Home page introducing the project and our research question
- **`dataset.html`** - Detailed dataset description with structure, cleaning process, and design motivations
- **`algorithm.html`** - Step-by-step algorithm explanation with design rationale
- **`people.html`** - Team member information and detailed division of labor

**Design Motivations Documented**:
- **Dataset choices**: Why we selected Gutenberg Books and how we structured the data
- **Algorithm design**: Rationale for our counting approach and data normalization
- **Technical decisions**: Bootstrap framework choice, responsive design considerations
- **Division of labor**: Clear documentation of who contributed what to each project phase

**Technical Implementation**: Bootstrap 5.3.3, responsive design, professional styling

## Step 5: GitHub Publication

**Publishing Requirements Met**:
- **GitHub Repository**: Complete project hosted at this repository
- **GitHub Pages**: Website publicly accessible via GitHub Pages hosting

**Team Members & Division of Labor**

**Muhammad Al-Waeli** - Project Coordinator & Data Research
- Selected and evaluated the Kaggle Gutenberg Books dataset
- Led initial project conceptualization and planning
- Coordinated team collaboration and milestone tracking

**Syeda Aisha Zaidi** - Algorithm Designer & Documentation
- Designed the complete algorithm logic and approach
- Wrote detailed pseudocode documentation (`algorithm.md`)
- Defined the problem scope and algorithmic requirements

**Lilian Omolo** - Data Engineer
- Performed comprehensive data cleaning and validation
- Created the final `data-cleaned.csv` (Excel-compatible)
- Tested algorithm implementation and validated results

**Stefan Ionica** - Technical
- Wrote the Python algorithm (`count_popular_subjects.py`)
- Built the website
- GitHub repository setup and deployment
