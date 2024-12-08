def query_database(connection_string):
    import pyodbc

    try:
        # Connect to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to find John Doe's PatientID
        query_patient_id = """
        SELECT PatientID
        FROM Patients
        WHERE FirstName = 'John' AND LastName = 'Doe'
        """
        
        cursor.execute(query_patient_id)
        patient_id_result = cursor.fetchone()

        # Check if patient exists
        if not patient_id_result:
            print("Patient John Doe not found in the database.")
            return {}

        patient_id = patient_id_result.PatientID

        # SQL query to retrieve diagnoses for John Doe
        query_diagnoses = """
        SELECT d.DiagnosisCode, d.DiagnosisDescription
        FROM Diagnoses d
        JOIN PatientDiagnoses pd ON d.DiagnosisID = pd.DiagnosisID
        WHERE pd.PatientID = ?
        """
        
        cursor.execute(query_diagnoses, patient_id)
        diagnoses_result = cursor.fetchall()

        # SQL query to retrieve prescriptions for John Doe
        query_prescriptions = """
        SELECT m.MedicineName, pm.Dosage, pm.PrescriptionDate
        FROM Medicines m
        JOIN PatientMedicines pm ON m.MedicineID = pm.MedicineID
        WHERE pm.PatientID = ?
        """
        
        cursor.execute(query_prescriptions, patient_id)
        prescriptions_result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Prepare the results
        diagnoses = [(row.DiagnosisCode, row.DiagnosisDescription) for row in diagnoses_result]
        prescriptions = [(row.MedicineName, row.Dosage, row.PrescriptionDate) for row in prescriptions_result]

        return {
            "Diagnoses": diagnoses,
            "Prescriptions": prescriptions
        }

    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return {}

# Use the function
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
results = query_database(connection_string)
print(results)