"""
 - Connect to the hr.db (stored in supporting-files directory) with sqlite3 
 - Write a query to find the names (first_name, last_name) of the employees who have a manager who works for a department based in the United States. 
 

Expected columns:
    - first_name	
    - last_name	
    - manager_od

Notes:
    - Use tables employees, departments and locations
    - You shouldn’t use JOINs here. 
    - You can connect to DB from Jupyter Lab/Notebook, explore the table and try different queries
    - In the variable 'SQL' store only the final query ready for validation 
"""
import sqlite3

# Connect to the HR database
connection = sqlite3.connect('supporting_files/hr.db')
cursor = connection.cursor()

# Define the SQL query
SQL = """
SELECT 
    e.first_name, 
    e.last_name, 
    e.manager_id AS manager_id
FROM 
    employees AS e
WHERE 
    e.manager_id IN (
        SELECT 
            e1.employee_id
        FROM 
            employees AS e1
        WHERE 
            e1.department_id IN (
                SELECT 
                    d.department_id
                FROM 
                    departments AS d
                WHERE 
                    d.location_id IN (
                        SELECT 
                            l.location_id
                        FROM 
                            locations AS l
                        WHERE 
                            l.country_id = 'US'
                    )
            )
    );
"""
# Execute the query
cursor.execute(SQL)

# Fetch the results
results = cursor.fetchall()