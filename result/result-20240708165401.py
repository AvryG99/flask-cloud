def query_database(connection_string):
    import pyodbc

    # Establish a connection to the SQL Server database
    try:
        conn = pyodbc.connect(connection_string)
    except pyodbc.Error as e:
        print("Could not connect to the database. Error: ", e)
        return

    cursor = conn.cursor()

    # Define the query to get all diagnoses of female patients
    query = """
    SELECT Diagnoses.DiagnosisDescription
    FROM Patients
    JOIN PatientDiagnoses ON Patients.PatientID = PatientDiagnoses.PatientID
    JOIN Diagnoses ON PatientDiagnoses.DiagnosisID = Diagnoses.DiagnosisID
    WHERE Patients.Gender = 'F'
    """

    try:
        # Execute the query and fetch the results
        cursor.execute(query)
        result = cursor.fetchall()
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        result = None
    finally:
        # Close the connection
        conn.close()

    # Process the result
    if result:
        return [row.DiagnosisDescription for row in result]
    else:
        return []

# Connection string for the SQL Server database
connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=EHR;Trusted_Connection=yes;"

# Call the function and print the results
diagnoses = query_database(connection_string)
print(diagnoses)