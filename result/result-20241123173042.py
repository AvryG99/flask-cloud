def query_doctors(connection_string):
    import pyodbc

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
        SELECT DoctorID, FirstName, LastName, Specialty, PhoneNumber
        FROM Doctors
        """

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        # Return list of doctors with their details
        return [(row.DoctorID, row.FirstName, row.LastName, row.Specialty, row.PhoneNumber) for row in result]
    except pyodbc.Error as e:
        print("Error executing query: ", e)
        return []

# Example usage:
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
doctors = query_doctors(connection_string)
for doctor in doctors:
    print(f"DoctorID: {doctor[0]}, Name: {doctor[1]} {doctor[2]}, Specialty: {doctor[3]}, Phone: {doctor[4]}")