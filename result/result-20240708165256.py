def query_database(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
        SELECT d.DiagnosisCode, d.DiagnosisDescription
        FROM Diagnoses d
        JOIN PatientDiagnoses pd ON d.DiagnosisID = pd.DiagnosisID
        JOIN Patients p ON pd.PatientID = p.PatientID
        WHERE p.Gender = 'M'
        """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        return [(row.DiagnosisCode, row.DiagnosisDescription) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=EHR;Trusted_Connection=yes;'
diagnoses_of_male_patients = query_database(connection_string)
for diagnosis in diagnoses_of_male_patients:
    print(f"Diagnosis Code: {diagnosis[0]}, Description: {diagnosis[1]}")