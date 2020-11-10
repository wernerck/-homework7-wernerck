#Name: Christian Werner
#Uniqname: wernerck

import sqlite3 

def question0():
    ''' Constructs and executes SQL query to retrieve
    all fields from the Region table
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Region"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question1():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT * 
      FROM Territory
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question2():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT COUNT (*) 
      FROM Employee
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question3():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT * 
      FROM Product 
      ORDER BY ID DESC 
      LIMIT 10
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question4():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT ProductName, UnitPrice 
      FROM Product 
      ORDER BY UnitPrice DESC 
      LIMIT 3
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question5():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT ProductName, UnitPrice, UnitsInStock 
      FROM Product 
      WHERE UnitsInStock >= 60 AND UnitsInStock <=100
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question6():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT ProductName
      FROM Product 
      WHERE ReorderLevel > UnitsInStock 
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question7():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT Id
      FROM [Order]
      WHERE ShipCountry = "France" AND ShipPostalCode LIKE "%04" 
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question8():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT CompanyName, ContactName
      FROM Customer
      WHERE Country = "UK" AND FAX NOT NULL 
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question9():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT ProductName, UnitPrice
      FROM Product
      WHERE CategoryId = "1"
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question10():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT ProductName
      FROM Product
      WHERE CategoryId = "6" AND Discontinued = "1"
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question11():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT [Order].Id, Employee.FirstName, Employee.LastName
      FROM [Order] INNER JOIN Employee
      ON [Order].EmployeeId = Employee.Id
      WHERE ShipCountry = "Germany" 
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question12():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = '''
      SELECT [Order].Id, [Order].OrderDate, Customer.CompanyName
      FROM Customer INNER JOIN [Order]
      ON Customer.Id = [Order].CustomerId
      WHERE OrderDate <= "2012-07-10"
    '''
    result = cursor.execute(query).fetchall()
    connection.close()
    return result



#################################################################
########################  ECs start here  #######################
#################################################################

#########
## EC1 ##
#########

def print_query_result(raw_query_result):
    ''' Pretty prints raw query result
    
    Parameters
    ----------
    list 
        a list of tuples that represent raw query result
    
    Returns
    -------
    None
    '''
    #TODO Implement function
    pass


if __name__ == "__main__":
    '''WHEN SUBMIT, UNCOMMENT THE TWO LINES OF CODE
    BELOW IF YOU COMPLETED EC1'''

    # result = question9()
    # print_query_result(result)

#########
## EC2 ##
#########
    
    #TODO Implement interactive program here
    pass

