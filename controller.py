
from mysql.connector import connect, Error
connection = None


try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="vape_shop",
        port="3306"
    )
    
    cursor = connection.cursor()
    print("Connected to the database!")
    
    def checkUser(username, password=None):
        cmd = f"Select count(username) from user where username='{username}' and BINARY password='{password}'"
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a
    
    def add_order(name,orders,total_price,cash,balance):
        try:
            query = "INSERT INTO ordertb (name,orders,total,cash,balance) VALUES (%s, %s, %s, %s, %s)"
            values = (name, orders,total_price,cash,balance)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def get_total_price():
        try:
            cmd = """SELECT SUM(total) FROM ordertb;"""
            cursor.execute(cmd)
            total_amount = cursor.fetchone()[0]
            
            if total_amount is None:
                total_amount = 0
            return total_amount
            
        except Exception as e:
            print(f"Error: {e}")
            return []
        
    def get_total_order():
        try:
            cmd = """SELECT COUNT(*) FROM ordertb;"""
            cursor.execute(cmd)
            total_data = cursor.fetchone()[0]
            
            if total_data is None:
                total_data = 0
            return total_data
            
        except Exception as e:
            print(f"Error: {e}")
            return []
        
        
    def get_orders():
        try:
            cmd = "SELECT id,name,orders,total,cash,balance FROM ordertb;"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()

            # Return the results
            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return [] 
        
       # update order
    def update_order(id,order):
        cmd = f"update ordertb set orders ='{order}' where id = '{id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False
        return True
            
        
        # Delete a order
    def delete_order(id):
        cmd = f"delete from ordertb where id='{id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    
except Error as e:
    print(f"Error: {e}")