def query_database(connection_string):
    import pyodbc

    try:
        # Establish a connection to the database
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
        
        # Close the database connection
        conn.close()

        # Return the results as a list of tuples
        return [(row.DoctorID, row.FirstName, row.LastName, row.Specialty, row.PhoneNumber) for row in result]
    
    except pyodbc.Error as e:
        # Handle any errors that occur during the database connection or query execution
        print("Error executing query: ", e)
        return []

# Define the connection string
connection_string = "driver={ODBC Driver 17 for SQL Server};server=web-service.database.windows.net;database=mimic-iii;UID=averyg99;PWD=#200267YuHAiGGIAHUY;"

# Call the function and print the results
doctors = query_database(connection_string)
for doctor in doctors:
    print(f"DoctorID: {doctor[0]}, Name: {doctor[1]} {doctor[2]}, Specialty: {doctor[3]}, Phone: {doctor[4]}")