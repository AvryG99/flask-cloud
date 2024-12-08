def query_patients(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to select all patients
        query = """
        SELECT PatientID, FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber
        FROM Patients
        """

        # Execute the query
        cursor.execute(query)
        # Fetch all results
        result = cursor.fetchall()
        # Close the connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.PatientID, row.FirstName, row.LastName, row.DateOfBirth, row.Gender, row.Address, row.PhoneNumber) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiG;"
patients = query_patients(connection_string)
for patient in patients:
    print(patient)