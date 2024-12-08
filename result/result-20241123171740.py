def query_all_doctors(connection_string):
    import pyodbc

    try:
        # Connect to the database using the provided connection string
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # SQL query to select all doctors
        query = """
        SELECT DoctorID, FirstName, LastName, Specialty, PhoneNumber
        FROM Doctors
        """

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the list of doctors as tuples
        return [(row.DoctorID, row.FirstName, row.LastName, row.Specialty, row.PhoneNumber) for row in result]
    except pyodbc.Error as e:
        # Print any errors that occur during the query execution
        print("Error executing query: ", e)
        return []

# Example usage:
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
doctors = query_all_doctors(connection_string)
for doctor in doctors:
    print(doctor)