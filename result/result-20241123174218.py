def query_database(connection_string):
    import pyodbc

    try:
        # Establish the connection
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to get all diagnoses for all patients
        query = """
        SELECT DISTINCT d.DiagnosisCode, d.DiagnosisDescription
        FROM Diagnoses d
        JOIN PatientDiagnoses pd ON d.DiagnosisID = pd.DiagnosisID
        JOIN Patients p ON pd.PatientID = p.PatientID
        """

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Process and return the result
        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]

    except pyodbc.Error as e:
        # Handle errors and print the error message
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
diagnoses = query_database(connection_string)
for diagnosis in diagnoses:
    print(f"Diagnosis Code: {diagnosis[0]}, Description: {diagnosis[1]}")