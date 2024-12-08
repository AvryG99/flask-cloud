def query_database(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database using the provided connection string
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to retrieve all doctors
        query = """
        SELECT DoctorID, FirstName, LastName, Specialty, PhoneNumber
        FROM Doctors
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all results from the executed query
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the list of doctors as tuples
        return [(row.DoctorID, row.FirstName, row.LastName, row.Specialty, row.PhoneNumber) for row in result]

    except pyodbc.Error as e:
        # Print the error if there is one and return an empty list
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
doctors = query_database(connection_string)
for doctor in doctors:
    print(f"DoctorID: {doctor[0]}, Name: {doctor[1]} {doctor[2]}, Specialty: {doctor[3]}, Phone: {doctor[4]}")