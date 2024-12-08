def query_database(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
        SELECT m.MedicineName, pm.Dosage
        FROM Medicines m
        JOIN PatientMedicines pm ON m.MedicineID = pm.MedicineID
        JOIN PatientDiagnoses pd ON pm.PatientID = pd.PatientID
        JOIN Diagnoses d ON pd.DiagnosisID = d.DiagnosisID
        WHERE d.DiagnosisDescription = 'Acute sinusitis'
        """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        return [(row.MedicineName, row.Dosage) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Use the function to query the database
connection_string = "DRIVER={SQL Server};SERVER=MSI;DATABASE=EHR;Trusted_Connection=yes;"
results = query_database(connection_string)

for medicine, dosage in results:
    print(f"Medicine: {medicine}, Dosage: {dosage}")