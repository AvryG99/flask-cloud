def query_database(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
        SELECT DISTINCT d.FirstName, d.LastName
        FROM Medicines m
        JOIN PatientMedicines pm ON m.MedicineID = pm.MedicineID
        JOIN PatientDoctor pd ON pm.PatientID = pd.PatientID
        JOIN Doctors d ON pd.DoctorID = d.DoctorID
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
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"
doctors = query_database(connection_string)
for doctor in doctors:
    print(f"Doctor: {doctor[0]} {doctor[1]}")