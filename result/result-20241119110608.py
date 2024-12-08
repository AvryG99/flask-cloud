def query_database(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Step 1: Get the MedicineID for Metformin
        query_medicine_id = """
        SELECT MedicineID
        FROM Medicines
        WHERE MedicineName = 'Metformin'
        """
        cursor.execute(query_medicine_id)
        medicine_id_row = cursor.fetchone()
        if not medicine_id_row:
            print("Metformin is not found in the Medicines table.")
            return []
        medicine_id = medicine_id_row.MedicineID

        # Step 2 & 3: Get PatientID and DoctorID for those prescribed Metformin
        query_doctors_prescribing_metformin = """
        SELECT DISTINCT d.DoctorID, d.FirstName, d.LastName
        FROM Doctors d
        JOIN PatientDoctor pd ON d.DoctorID = pd.DoctorID
        JOIN PatientMedicines pm ON pd.PatientID = pm.PatientID
        WHERE pm.MedicineID = ?
        """
        cursor.execute(query_doctors_prescribing_metformin, (medicine_id,))
        result = cursor.fetchall()
        conn.close()

        return [{"DoctorID": row.DoctorID, "FirstName": row.FirstName, "LastName": row.LastName} for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Connection string
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"

# Executing the function and printing the results
doctors_prescribing_metformin = query_database(connection_string)
for doctor in doctors_prescribing_metformin:
    print(f"Doctor ID: {doctor['DoctorID']}, Name: {doctor['FirstName']} {doctor['LastName']}")