def query_all_patient_diagnoses(connection_string):
    import pyodbc

    try:
        # Establish a connection to the SQL Server
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to retrieve all diagnoses of all patients
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

        # Return the results as a list of tuples
        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]

    except pyodbc.Error as e:
        # Handle SQL errors
        print("Error executing query: ", e)
        return []

# Connection string for the database
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"

# Query the database and print results
diagnoses = query_all_patient_diagnoses(connection_string)
for diagnosis in diagnoses:
    print(f"Diagnosis Code: {diagnosis[0]}, Diagnosis Description: {diagnosis[1]}")