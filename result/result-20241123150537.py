def query_all_diagnoses(connection_string):
    import pyodbc

    try:
        # Establish connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to get all diagnoses for all patients
        query = """
        SELECT p.FirstName, p.LastName, p.DateOfBirth, d.DiagnosisCode, d.DiagnosisDescription
        FROM Patients p
        JOIN PatientDiagnoses pd ON p.PatientID = pd.PatientID
        JOIN Diagnoses d ON pd.DiagnosisID = d.DiagnosisID
        """

        # Execute the query and fetch results
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.FirstName, row.LastName, row.DateOfBirth, row.DiagnosisCode, row.DiagnosisDescription) for row in result]
    except pyodbc.Error as e:
        # Handle any errors that occur during the query execution
        print("Error executing query: ", e)
        return []

# Connection string for the database
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"

# Perform the query and get the diagnoses
diagnoses = query_all_diagnoses(connection_string)

# Display the results
for diagnosis in diagnoses:
    print(diagnosis)