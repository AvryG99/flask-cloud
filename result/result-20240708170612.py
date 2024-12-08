def query_database(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
        SELECT DISTINCT d.FirstName, d.LastName
        FROM Doctors d
        JOIN PatientDoctor pd ON d.DoctorID = pd.DoctorID
        JOIN PatientMedicines pm ON pd.PatientID = pm.PatientID
        JOIN Medicines m ON pm.MedicineID = m.MedicineID
        WHERE m.MedicineName = 'Metformin'
        """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        return [(row.FirstName, row.LastName) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage:
connection_string = "DRIVER={SQL Server};SERVER=MSI;DATABASE=EHR;Trusted_Connection=yes;"
doctors_who_prescribed_metformin = query_database(connection_string)
for doctor in doctors_who_prescribed_metformin:
    print(f"Doctor: {doctor[0]} {doctor[1]}")