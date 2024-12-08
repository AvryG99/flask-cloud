def query_database(connection_string):
    import pyodbc

    try:
        # Connect to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to find all doctors who diagnosed patient John Doe
        query = """
        SELECT DISTINCT doc.FirstName, doc.LastName, doc.Specialty
        FROM Doctors doc
        JOIN PatientDoctor pd ON doc.DoctorID = pd.DoctorID
        JOIN Patients p ON pd.PatientID = p.PatientID
        WHERE p.FirstName = 'John' AND p.LastName = 'Doe'
        """

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the result as a list of tuples
        return [(row.FirstName, row.LastName, row.Specialty) for row in result]
    
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Connection string
connection_string = (
    "driver={ODBC Driver 17 for SQL Server};"
    "server=web-service.database.windows.net;"
    "database=mimic-iii;"
    "UID=averyg99;"
    "PWD=#200267YuHAiGGIAHUY;"
)

# Call the function and print the results
doctors = query_database(connection_string)
for doctor in doctors:
    print(f"Doctor Name: {doctor[0]} {doctor[1]}, Specialty: {doctor[2]}")