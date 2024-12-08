def get_all_patient_diagnoses(connection_string):
    import pyodbc

    try:
        # Establish the database connection
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to fetch all diagnoses for all patients
        query = """
        SELECT p.FirstName, p.LastName, d.DiagnosisCode, d.DiagnosisDescription
        FROM Patients p
        JOIN PatientDiagnoses pd ON p.PatientID = pd.PatientID
        JOIN Diagnoses d ON pd.DiagnosisID = d.DiagnosisID
        """

        # Execute the query
        cursor.execute(query)
        # Fetch all results
        result = cursor.fetchall()
        # Close the connection
        conn.close()

        # Return list of tuples containing patient name and diagnosis details
        return [(row.FirstName, row.LastName, row.DiagnosisCode, row.DiagnosisDescription) for row in result]
    
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=None;Database=None;Trusted_Connection=yes;"

diagnoses = get_all_patient_diagnoses(connection_string)
for diagnosis in diagnoses:
    print(diagnosis)