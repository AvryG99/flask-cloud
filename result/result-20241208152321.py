def query_john_doe_status(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to find John Doe's PatientID
        patient_id_query = """
        SELECT PatientID
        FROM Patients
        WHERE FirstName = 'John' AND LastName = 'Doe'
        """

        cursor.execute(patient_id_query)
        patient_row = cursor.fetchone()

        if not patient_row:
            print("John Doe not found in the database.")
            return []

        patient_id = patient_row.PatientID

        # SQL query to get John Doe's diagnoses
        diagnoses_query = """
        SELECT d.DiagnosisCode, d.DiagnosisDescription, pd.DiagnosisDate
        FROM Diagnoses d
        JOIN PatientDiagnoses pd ON d.DiagnosisID = pd.DiagnosisID
        WHERE pd.PatientID = ?
        """

        cursor.execute(diagnoses_query, patient_id)
        diagnoses_result = cursor.fetchall()

        # SQL query to get John Doe's medicines
        medicines_query = """
        SELECT m.MedicineName, pm.Dosage, pm.PrescriptionDate
        FROM Medicines m
        JOIN PatientMedicines pm ON m.MedicineID = pm.MedicineID
        WHERE pm.PatientID = ?
        """

        cursor.execute(medicines_query, patient_id)
        medicines_result = cursor.fetchall()

        conn.close()

        # Prepare and return the results
        status = {
            "Diagnoses": [(row.DiagnosisCode, row.DiagnosisDescription, row.DiagnosisDate) for row in diagnoses_result],
            "Medicines": [(row.MedicineName, row.Dosage, row.PrescriptionDate) for row in medicines_result]
        }

        return status

    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return {}

# Connection string provided in the question
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"

# Call the function and print John Doe's status
john_doe_status = query_john_doe_status(connection_string)
print(john_doe_status)