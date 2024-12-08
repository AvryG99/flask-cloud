def query_prescribing_doctors(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to find doctors who have prescribed Metformin
        query = """
        SELECT DISTINCT d.FirstName, d.LastName
        FROM Doctors d
        JOIN PatientDoctor pd ON d.DoctorID = pd.DoctorID
        JOIN PatientMedicines pm ON pd.PatientID = pm.PatientID
        JOIN Medicines m ON pm.MedicineID = m.MedicineID
        WHERE m.MedicineName = 'Metformin'
        """

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the result
        return [(row.FirstName, row.LastName) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage:
connection_string = "driver={ODBC Driver 17 for SQL Server};server=MSI;database=EHR;Trusted_Connection=yes;"
doctors = query_prescribing_doctors(connection_string)
print("Doctors who prescribed Metformin:")
for first_name, last_name in doctors:
    print(f"{first_name} {last_name}")