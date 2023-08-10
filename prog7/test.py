import psycopg2

# Connect to the database
con = psycopg2.connect(
    host="localhost",
    database="myDB",
    user="postgres",
    password="postgres",
    port=5432
)

# Get user input
pcode = str(input("Enter postcode to show weather for: "))

# Construct the query with user input
query = f"""
    SELECT "Postcode 31", "Postcode 32" FROM new_table
    WHERE "Postcode 1" = '{pcode}';
"""

# Create a cursor
cur = con.cursor()
cur.execute(query)

# Fetch the results
results = cur.fetchall()

# Close the cursor and connection
cur.close()
con.close()

print(results)
# Process and display the results
for row in results:
    print(row)  # Replace this with your desired display code
