def query_all_diagnoses(connection_string):
    import pyodbc

    try:
        # Establish connection to the database
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
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Close the database connection
        conn.close()
        
        # Return the result as a list of tuples
        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in results]

    except pyodbc.Error as e:
        # Print and return the error message
        print("Error executing query: ", e)
        return []

# Example usage:
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"
diagnoses = query_all_diagnoses(connection_string)
for diagnosis in diagnoses:
    print(diagnosis)