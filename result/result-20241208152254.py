def get_prescriptions_of_john_doe(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to get the prescriptions for John Doe
        query = """
        SELECT m.MedicineName, pm.Dosage, pm.PrescriptionDate
        FROM Patients p
        JOIN PatientMedicines pm ON p.PatientID = pm.PatientID
        JOIN Medicines m ON pm.MedicineID = m.MedicineID
        WHERE p.FirstName = 'John' AND p.LastName = 'Doe'
        """

        # Execute the query
        cursor.execute(query)
        # Fetch all results
        result = cursor.fetchall()
        # Close the connection
        conn.close()

        # Return the result in a readable format
        return [(row.MedicineName, row.Dosage, row.PrescriptionDate) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
prescriptions = get_prescriptions_of_john_doe(connection_string)
for prescription in prescriptions:
    print(f"Medicine Name: {prescription[0]}, Dosage: {prescription[1]}, Prescription Date: {prescription[2]}")