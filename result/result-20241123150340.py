def query_database(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to retrieve all diagnoses for all patients
        query = """
        SELECT DISTINCT d.DiagnosisCode, d.DiagnosisDescription
        FROM Diagnoses d
        JOIN PatientDiagnoses pd ON d.DiagnosisID = pd.DiagnosisID
        JOIN Patients p ON pd.PatientID = p.PatientID
        """

        # Execute the query
        cursor.execute(query)
        # Fetch all results from the executed query
        result = cursor.fetchall()
        # Close the database connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]
    except pyodbc.Error as e:
        # Print any error that occurs during the query execution
        print("Error executing query: ", e)
        return []

# Example usage
if __name__ == "__main__":
    connection_string = (
        "driver={ODBC Driver 17 for SQL Server};"
        "server=web-service.database.windows.net;"
        "database=mimic-iii;"
        "UID=averyg99;"
        "PWD=#200267YuHAiGGIAHUY;"
    )
    diagnoses = query_database(connection_string)
    for diagnosis in diagnoses:
        print(f"Diagnosis Code: {diagnosis[0]}, Description: {diagnosis[1]}")