def query_database_for_doctors(connection_string):
    import pyodbc

    try:
        # Establish a connection to the SQL Server database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the SQL query to retrieve all doctors
        query = """
        SELECT DoctorID, FirstName, LastName, Specialty, PhoneNumber
        FROM Doctors
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DoctorID, row.FirstName, row.LastName, row.Specialty, row.PhoneNumber) for row in result]
    
    except pyodbc.Error as e:
        # Print any errors that occur during the query execution
        print("Error executing query: ", e)
        return []

# Example usage
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"
doctors = query_database_for_doctors(connection_string)
for doctor in doctors:
    print(doctor)