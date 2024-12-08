def query_all_diagnoses(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        query = """
        SELECT p.FirstName, p.LastName, d.DiagnosisCode, d.DiagnosisDescription
        FROM Patients p
        JOIN PatientDiagnoses pd ON p.PatientID = pd.PatientID
        JOIN Diagnoses d ON pd.DiagnosisID = d.DiagnosisID
        """
        
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        return [(row.FirstName, row.LastName, row.DiagnosisCode, row.DiagnosisDescription) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage:
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"
diagnoses = query_all_diagnoses(connection_string)
for diagnosis in diagnoses:
    print(f"Patient: {diagnosis[0]} {diagnosis[1]}, Diagnosis Code: {diagnosis[2]}, Description: {diagnosis[3]}")