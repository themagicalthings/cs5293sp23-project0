**- CS5293SP23 Project0 
- by Vamsi Thokala**

**-Norman Daily Incident Summary** 

This code extracts data from a PDF file containing Norman, Oklahoma's daily incident summary and stores it in a Pandas DataFrame. It then creates a SQLite3 database named norman.db and populates it with the extracted data.
Prerequisites

This code requires the following **libraries**:

    urllib.request
    pypdf
    re
    pandas
    sqlite3

**Installation**

You can install the required libraries using pip:

pip install urllib pypdf re pandas sqlite3

**Usage**

    Step 1: Define the URL of the PDF file containing the Norman Daily Incident Summary. The current URL is set as the default.
    Step 2: Call the extract_incidents function, passing the incident data fetched from the URL as an argument. This function returns a Pandas DataFrame containing the extracted incident data.
    Step 3: Call the createdb function to create the SQLite3 database and populatedb function to populate the database with the data in the Pandas DataFrame.

python

**url** = "https://www.normanok.gov/sites/default/files/documents/2023-01/2023-01-22_daily_incident_summary.pdf"

**Extract data from PDF and store it in a Pandas DataFrame**
incident_data = fetchincidents(url)
incidents_df = extract_incidents(incident_data)

**Create and populate the SQLite3 database**
createdb()
populatedb(incidents_df)

**Functions**
fetchincidents

This function takes the URL of the PDF file containing the Norman Daily Incident Summary as an argument. It uses urllib.request to fetch and return the incident data.
**extract_incidents**

This function takes the incident data fetched using fetchincidents as an argument. It extracts the relevant information like incident date, incident number, location, nature, and incident ORI from the PDF using the PyPDF library. It then stores the extracted data in a Pandas DataFrame.
createdb

This function creates a **SQLite3 database** named norman.db and a table named incidents with columns named incident_time, incident_number, incident_location, nature, and incident_ori.
populatedb

This function populates the incidents table in the norman.db database with the data stored in the Pandas DataFrame.

**Files included:**

    main.py
    project0.py
    test_data.py

**Requirements:**

Python 3.x, PyPDF2, pandas, urllib, sqlite3

**Usage:**

    Clone the repository.
    Download the incident report PDF file from the Norman Police Department Activity Reports.
    Save the PDF file in the same directory where main.py and project0.py are saved.
    Run main.py to execute the program.
    Run test_data.py to run the test cases.

**Functions:**

    fetchincidents(url):
    This function fetches the data from the provided input URL using urllib package.

    extractincidents(incidents):
    This function extracts and parses the data and stores the data in the form of lists to insert into the database. It uses PyPDF2 package to extract data from the PDF file.

   **createdb():**
    This function creates a new database by connecting to SQLite3.

  **populatedb(incidents):
    This function inserts the data that is present in the form of lists into the database.

   **status():**
    This function fetches the required output.

**Test cases:**

    fetchincidents(url):
    This function tests whether the returned data is empty or not.

    extractincidents(incidents):
    This function tests whether the list is empty or not, if the return type is list or not and if the length of each incident is equal to 5 or not.

    createdb():
    This function tests whether the table that is created is empty or not.

    populatedb(incidents):
    This function tests whether the data that we are receiving is properly inserted or not.

    status():
    This function tests whether the data that we have received in the extractincidents(incidents) is of list type or not.

**How to Run the file **   

Run the command pipenv run python project0/main.py --incidents [URL], where [URL] is the URL of the PDF file containing the incident reports. This will fetch the data from the PDF, store it in the database, and output the count of each incident type.

**Output :**

<img width="1470" alt="Screenshot 2023-03-07 at 8 09 12 PM" src="https://user-images.githubusercontent.com/115323632/223606040-ee3a52ed-c355-42e2-b5c6-9df9968825f4.png">

<img width="675" alt="Screenshot 2023-03-07 at 8 10 50 PM" src="https://user-images.githubusercontent.com/115323632/223606069-0d7e054d-db5e-44b1-b905-1e6d69f407a4.png">


