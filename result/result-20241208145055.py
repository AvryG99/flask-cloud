def query_database(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Query to get the PatientID of John Doe
        query_patient_id = """
        SELECT PatientID
        FROM Patients
        WHERE FirstName = 'John' AND LastName = 'Doe'
        """

        cursor.execute(query_patient_id)
        patient_id_row = cursor.fetchone()

        if not patient_id_row:
            print("John Doe not found in the database.")
            return

        patient_id = patient_id_row.PatientID

        # Query to get John Doe's diagnoses
        query_diagnoses = """
        SELECT d.DiagnosisCode, d.DiagnosisDescription, pd.DiagnosisDate
        FROM Diagnoses d
        JOIN PatientDiagnoses pd ON d.DiagnosisID = pd.DiagnosisID
        WHERE pd.PatientID = ?
        """

        cursor.execute(query_diagnoses, patient_id)
        diagnoses = cursor.fetchall()

        # Query to get John Doe's medicines
        query_medicines = """
        SELECT m.MedicineName, pm.Dosage, pm.PrescriptionDate
        FROM Medicines m
        JOIN PatientMedicines pm ON m.MedicineID = pm.MedicineID
        WHERE pm.PatientID = ?
        """

        cursor.execute(query_medicines, patient_id)
        medicines = cursor.fetchall()

        # Query to get John Doe's doctors
        query_doctors = """
        SELECT d.FirstName, d.LastName, d.Specialty, pd.AssignmentDate
        FROM Doctors d
        JOIN PatientDoctor pd ON d.DoctorID = pd.DoctorID
        WHERE pd.PatientID = ?
        """

        cursor.execute(query_doctors, patient_id)
        doctors = cursor.fetchall()

        conn.close()

        # Constructing the results
        result = {
            "Diagnoses": [(row.DiagnosisCode, row.DiagnosisDescription, row.DiagnosisDate) for row in diagnoses],
            "Medicines": [(row.MedicineName, row.Dosage, row.PrescriptionDate) for row in medicines],
            "Doctors": [(row.FirstName, row.LastName, row.Specialty, row.AssignmentDate) for row in doctors]
        }

        return result

    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return {}

# Usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
john_doe_status = query_database(connection_string)
print(john_doe_status)