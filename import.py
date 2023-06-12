import csv
import pymysql
from datetime import datetime
import re

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='coffee'
)

cursor = conn.cursor()

with open('df_arabica_clean.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        farm_data = (row['Farm Name'], row['Altitude'], row['Producer'], row['Country of Origin'], row['Region'])
        cursor.execute("""
            INSERT INTO Farm (Farm_Name, Altitude, Producer, Country_of_Origin, Region)
            VALUES (%s, %s, %s, %s, %s)
        """, farm_data)
        conn.commit()
        farm_id = cursor.lastrowid

        company_data = (row['Company'], row['In-Country Partner'], row ['Certification Body'], row['Certification Address'], row['Certification Contact'])
        cursor.execute("""
            INSERT INTO Company (Company, In_Country_Partner, Certification_Body, Certification_Address, Certification_Contact)
            VALUES (%s, %s, %s, %s, %s)
        """, company_data)
        conn.commit()
        company_id = cursor.lastrowid

        bag_data = (row['Number of Bags'], row['Bag Weight'])
        cursor.execute("""
            INSERT INTO Bagging (Number_of_Bags, Bag_Weight)
            VALUES (%s, %s)
        """, bag_data)
        conn.commit()
        bag_id = cursor.lastrowid

        harvest_year = row['Harvest Year'].split('/')[0].strip()
        grading_date = datetime.strptime(re.sub(r"(\d+)(st|nd|rd|th)", r"\1", row['Grading Date']), "%B %d, %Y").strftime("%Y-%m-%d")
        expiration_date = datetime.strptime(re.sub(r"(\d+)(st|nd|rd|th)", r"\1", row['Expiration']), "%B %d, %Y").strftime("%Y-%m-%d")
        time_data = (harvest_year, grading_date, expiration_date)
        cursor.execute("""
            INSERT INTO Time_Dimension (Harvest_Year, Grading_Date, Expiration)
            VALUES (%s, %s, %s)
        """, time_data)
        conn.commit()
        time_id = cursor.lastrowid

        harvest_data = (time_id, row['Lot Number'])
        cursor.execute("""
            INSERT INTO Harvest_Information (Time_ID, Lot_Number)
            VALUES (%s, %s)
        """, harvest_data)
        conn.commit()
        harvest_id = cursor.lastrowid

        defect_data = (row['Category One Defects'], row['Quakers'], row['Category Two Defects'])
        cursor.execute("""
            INSERT INTO Defects (Category_One_Defects, Quakers, Category_Two_Defects)
            VALUES (%s, %s, %s)
        """, defect_data)
        conn.commit()
        defect_id = cursor.lastrowid

        characteristic_data = (row['Variety'], row['Processing Method'], row['Color'])
        cursor.execute("""
            INSERT INTO Coffee_Characteristics (Variety, Processing_Method, Color)
            VALUES (%s, %s, %s)
        """, characteristic_data)
        conn.commit()
        characteristic_id = cursor.lastrowid

        rating_data = (
            farm_id, harvest_id, company_id, bag_id, defect_id, characteristic_id,
            row['Total Cup Points'], row['Aroma'], row['Flavor'], row['Aftertaste'], row['Acidity'],
            row['Body'], row['Balance'], row['Uniformity'], row.get('Clean Cup'), row['Sweetness'],
            row['Overall'], row['Defects'], row.get('Moisture Percentage')
        )
        cursor.execute("""
            INSERT INTO Coffee_Ratings (Farm_ID, Harvest_ID, Company_ID, Bag_ID, Defect_ID, Characteristics_ID,
                                        Total_Cup_Points, Aroma, Flavor, Aftertaste, Acidity, Body, Balance, Uniformity, 
                                        Clean_Cup, Sweetness, Overall, Defects, Moisture_Percentage)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, rating_data)
        conn.commit()

cursor.close()
conn.close()
