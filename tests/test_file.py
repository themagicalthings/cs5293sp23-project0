import sys
sys.path.append('..')
from project0 import project0
import pytest
import pypdf
import re
import sqlite3
import tempfile

url = ("https://www.normanok.gov/sites/default/files/documents/2023-01/2023-01-22_daily_incident_summary.pdf")

def test_fetchincidents():
    f=project0.fetchincidents(url)  
    assert f is not None  

def test_extractincidents():
    f=project0.fetchincidents(url)
    e=project0.extract_incidents(f)
    assert e is not None

def test_createdb():
    db=project0.createdb() 
    assert db=="norman.db" 

def test_populatedb():
    db=project0.createdb()
    conn=sqlite3.connect(db)
    c=conn.cursor()
    res=c.execute('select * from incidents;')
    assert res!=None

def test_status():
    res=project0.status()
    assert len(res)>0
