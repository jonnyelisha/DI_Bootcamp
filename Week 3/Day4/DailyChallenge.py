import psycopg2
import requests
import random

conn = psycopg2.connect(
    host="localhost",
    database="Countries",
    user="postgres",
    password="Appleipod123"
)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    capital VARCHAR(100) NOT NULL,
    flag VARCHAR(255),
    subregion VARCHAR(100) 
    population INTEGER
)
''')

# Fetch data from API
response = requests.get('https://restcountries.com/v3.1/all')
all_countries = response.json()

# Select 10 random countries
random_countries = random.sample(all_countries, 10)

# Insert data into database
for country in random_countries:
    name = country['name']['common']
    capital = country['capital'][0] if country.get('capital') else 'N/A'
    flag = country['flags']['png']
    subregion = country.get('subregion', 'N/A')
    population = country['population']

    cursor.execute('''
    INSERT INTO countries (name, capital, flag, subregion, population)
    VALUES (%s, %s, %s, %s, %s)
    ''', (name, capital, flag, subregion, population))

# Commit changes and close connection
conn.commit()
conn.close()

print("10 random countries have been added to the database.")