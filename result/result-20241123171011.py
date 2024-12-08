def query_all_patient_diagnoses(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to retrieve all diagnoses for all patients
        query = """
        SELECT DISTINCT d.DiagnosisCode, d.DiagnosisDescription
        FROM Diagnoses d
        JOIN PatientDiagnoses pd ON d.DiagnosisID = pd.DiagnosisID
        """

        # Execute the query
        cursor.execute(query)
        # Fetch all results
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Define the connection string
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"

# Call the function and print the results
diagnoses = query_all_patient_diagnoses(connection_string)
for diagnosis in diagnoses:
    print(f"Diagnosis Code: {diagnosis[0]}, Description: {diagnosis[1]}")