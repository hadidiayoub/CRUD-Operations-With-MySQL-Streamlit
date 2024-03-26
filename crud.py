import streamlit as st
import mysql.connector

# Establish a connection to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    port=3306, # This is commented out but correct
    database="crud_new1",
    user="root",
    passwd=""
)
try:
    #Create a cursor object
    mycursor = mydb.cursor()
    print("Connection Established")
except:
    st.error("cONNECTION ERROR")

def main():
    st.title("CRUD Operations With MySQL")
    # Display Options for CRUD Operations
    # It seems like you didn't complete this line. Example:
    option = st.sidebar.selectbox("Select an operation", ("Create", "Read", "Update", "Delete"))

    if option == "Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter a name")
        email=st.text_input("Enter Email")
        if st.button("Create"):
            sql= "Insert into users(name,email) values(%s,%s)"
            val= (name,email)

            # Check if my database is commited successfully
            try:
                mycursor.execute(sql, val)
                mydb.commit()  # This will attempt to commit changes to the database.
                if mycursor.rowcount > 0:  # Check if any rows were affected/inserted.
                    st.success("Record created successfully.")
                else:
                    st.error("No record was created. Please check your input.")
            except mysql.connector.Error as err:
                st.error(f"An error occurred: {err}")  # Display the error to the user.

    elif option == "Read":
        st.subheader("Read a Record")
        mycursor.execute("select * from users ORDER BY id")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Update":
        st.subheader("Update a Record")
        id = st.number_input("Enter ID", value=1)
        name = st.text_input("Enter new Name")
        email = st.text_input("Enter new Email")
        if st.button("Update"):
            sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
            val = (name, email, id)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                if mycursor.rowcount > 0:
                    st.success("Record updated successfully.")
                else:
                    st.warning("No record was updated. Please check the ID and your input.")
            except mysql.connector.Error as err:
                st.error(f"An error occurred: {err}")



    elif option == "Delete":
        st.subheader("Delete a Record")
        id = st.number_input("Enter ID", value=1)
        if st.button("Delete"):
            sql = "DELETE FROM users WHERE id=%s"
            val = (id,)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                if mycursor.rowcount > 0:
                    st.success("Record deleted successfully.")
                else:
                    st.warning("No record was deleted. Please check the ID.")
            except mysql.connector.Error as err:
                st.error(f"An error occurred: {err}")



if __name__ == "__main__":
    main()
