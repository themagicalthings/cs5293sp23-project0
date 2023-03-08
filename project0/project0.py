# Imports necessary libraries/modules like urllib.request, pypdf, re, pandas, and sqlite3.
import urllib.request
import pypdf
import re
import pandas as pd
import sqlite3
from io import BytesIO

# Defines a URL variable which contains the URL of a PDF file.
url = "https://www.normanok.gov/sites/default/files/documents/2023-01/2023-01-22_daily_incident_summary.pdf"

#Defines a function named fetchincidents that takes in the URL and uses urllib.request module to fetch and return the incident data.
def fetchincidents(url):
    headers={}
    headers['User-Agent']="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    incident_data=urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    #print(incidents)
    return incident_data

# Defines a function named extract_incidents that takes in the incident data and extracts the relevant information like incident date, incident number, location, nature, and incident ORI from the PDF using the PyPDF library. It then stores the extracted data in a Pandas DataFrame.
def extract_incidents(incident_data):#First, fetch the incident data from the URL using the fetchincidents function and assign the returned data to the incident_data variable
    incident_data = fetchincidents(url)#Next, create a PdfReader object from the incident_data using the PyPDF library
    pdf = pypdf.PdfReader(BytesIO(incident_data))#Initialize an empty string variable called text, and an empty list called final_data
    text = ""
    final_data=[]
    #For each page in the PDF, extract the text using the extract_text() function from the PyPDF library
    #Then, split the text on the word "NORMAN" to remove unnecessary information at the end of the document
    #After that, split the resulting text into a list of lines using the splitlines() function
    for page in range(len(pdf.pages)):
        text = pdf.pages[page].extract_text()
        text = text.split('NORMAN')[0]#It then splits the text on the string "NORMAN" and keeps the first part
        page_data = text.splitlines()[1:]
        
        sm_c=0
        for line in page_data:#The resulting text is split into lines, and for each line, the code extracts relevant information and creates a dictionary object
            if len(line) <= 15:#The location is constructed by joining all words in the line except for the last one, which represents the nature of the incident
                sm_c+=1
                #print('here it is empty')
            else:#The dictionary contains the date/time, incident number, location, nature, and incident ORI of the incident
                temp = line.split()
                date = temp[0] + " " + temp[1]
                incident_number = temp[2]
                incident_ori = temp[-1]
                locnat = temp[3:-1]
                natture = ""
                locnatt = " ".join(locnat)
                
                for t in range(len(locnat)):
                    if len(locnat[t]) > 1: 
                        if locnat[t][0].isupper() and locnat[t][1].islower():
                            natture = " ".join(locnat[t:len(locnat)])

                if natture == "Call Nature Unknown":#If the nature of the incident is "Call Nature Unknown", it is changed to "911 Call Nature Unknown"
                    natture = "911 Call Nature Unknown"
                final_loc = locnatt[:locnatt.index(natture)] + locnatt[locnatt.index(natture) + len(natture):]
                final_data.append({ "Date / Time": date, "Incident Number": incident_number, "Location": final_loc,"Nature":natture, "Incident ORI": incident_ori })#The resulting dictionary object is appended to a list of final data
                
    df=pd.DataFrame(final_data)#Finally, the function returns the list of final data
    return df
# Defines a function named createdb that creates a SQLite3 database named norman.db and a table named incidents with columns named incident_time, incident_number, incident_location, nature, and incident_ori.
db='norman.db'
def createdb():
    conn = sqlite3.connect(db)#The function first establishes a connection to the norman.db database using sqlite3.connect(). It then creates a cursor object that can execute SQL commands on the database.
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS incidents (
        incident_time TEXT,
        incident_number TEXT,
        incident_location TEXT,
        nature TEXT,
        incident_ori TEXT
    );""")#it executes an SQL command using c.execute() to create the incidents table with the specified column names and data types. The IF NOT EXISTS clause is used to ensure that the table is only created if it does not already exist.
    conn.commit()
    conn.close()
    print(db)
    return db

# Defines a function named populatedb that populates the incidents table in the norman.db database with the data stored in the Pandas DataFrame.   
def populatedb(incidents):#populatedb takes one parameter, incidents, which is a pandas DataFrame containing incident data.
    conn = sqlite3.connect(db)#The function starts by establishing a connection to the SQLite database specified in the db variable.
    c = conn.cursor()
    c.execute('delete from incidents')
    conn.commit()

    for i in range(len(incidents)) :#It then deletes any existing data in the incidents table.
        final=(incidents.iloc[i, 0], incidents.iloc[i, 1],incidents.iloc[i, 2],incidents.iloc[i, 3],incidents.iloc[i, 4])
        c.execute('insert into incidents values(?,?,?,?,?)',final)
        conn.commit()
    conn.close()

# Defines a function named status that retrieves the data from the incidents table in the norman.db database and prints the number of incidents for each nature of the incident.
def status():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT nature, COUNT(*) FROM incidents GROUP BY nature")#The extracted data is then inserted into the incidents table using an SQL INSERT statement.
    rows = c.fetchall()
    for row in rows:
        if row[0]=="":
            continue
        else:
            print(str(row[0])+"|"+str(row[1]))
    conn.close()
    return rows
