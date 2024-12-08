def query_all_patients(connection_string):
    import pyodbc

    try:
        # Establish a connection to the SQL Server database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to select all patients
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

        # Return the results as a list of dictionaries
        return [
            {
                "PatientID": row.PatientID,
                "FirstName": row.FirstName,
                "LastName": row.LastName,
                "DateOfBirth": row.DateOfBirth,
                "Gender": row.Gender,
                "Address": row.Address,
                "PhoneNumber": row.PhoneNumber
            }
            for row in result
        ]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Connection string to the SQL Server database
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiG;"

# Call the function to get all patients
patients = query_all_patients(connection_string)

# Print the list of patients
for patient in patients:
    print(patient)