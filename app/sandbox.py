# import app.services
import psycopg2
# app.services._add_tables()

# import psycopg2
# conn = psycopg2.connect(
#     host="localhost",
#     database="fastapi_database",
#     user="myuser",
#     password="mypassword",
#     port="5432"  # Match the host port used in the docker run command
# )
# cur = conn.cursor()


#conn = psycopg2.connect("dbname=fastapi_database user=myuser password=mypassword host=localhost")
# conn = psycopg2.connect("dbname=fastapi_database user=postgres password=password host=localhost")
# cur = conn.cursor()


# query = """
# SELECT table_name, privilege_type
# FROM information_schema.role_table_grants
# WHERE grantee = %s;
# """
# cur.execute(query, ('myuser',))
# data = cur.fetchall()
# for row in cur.fetchall():
#     print(f"Table: {row[0]}, Privilege: {row[1]}")

# cur.execute("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO myuser;")
# query = """
# SELECT rolname, rolsuper, rolcreaterole, rolcreatedb, rolcanlogin
# FROM pg_roles
# WHERE rolname = %s;
# """
# cur.execute(query, ('myuser',))
# user_info = cur.fetchone()
# print(user_info)
# if user_info:
#     print(f"User: {user_info[0]}")
#     print(f"Superuser: {user_info[1]}, Create Role: {user_info[2]}, Create DB: {user_info[3]}")
#

def grant_all_privileges(dbname, user_to_grant):
    try:
        # Connect as a superuser or the database owner
        conn = psycopg2.connect(
            dbname="fastapi_database",  # Initially connect to postgres or target db
            user="postgres",
            password="password",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True
        cur = conn.cursor()

        # 1. Grant all privileges on the database itself
        cur.execute(f'GRANT ALL PRIVILEGES ON DATABASE {dbname} TO {user_to_grant};')

        # 2. Grant privileges on schemas and objects inside the specific database
        # Note: You must be connected to the target database to grant internal privileges
        #print(f'\\c {dbname}')
        #cur.execute(f'\\c {dbname}')  # Or create a new connection to 'dbname'

        # Grant on schema
        cur.execute(f'GRANT ALL PRIVILEGES ON SCHEMA public TO {user_to_grant};')

        # Grant on all existing tables and sequences
        cur.execute(f'GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {user_to_grant};')
        cur.execute(f'GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO {user_to_grant};')

        # 3. Grant privileges on FUTURE tables created in the schema
        cur.execute(f'ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO {user_to_grant};')

        print(f"Successfully granted all privileges to {user_to_grant}")
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")


# grant_all_privileges("fastapi_database", "myuser")


# import os
# from dotenv import load_dotenv
#
# load_dotenv()
# POSTGRES_DB_USER = os.getenv("POSTGRES_DB_USER")
# POSTGRES_DB_PASSWORD = os.getenv("POSTGRES_DB_PASSWORD")
# POSTGRES_DB_HOST_PORT = os.getenv("POSTGRES_DB_HOST_PORT")
# POSTGRES_DB_NAME = os.getenv("POSTGRES_DB_NAME")
#
# DATABASE_URL = f"postgresql://{POSTGRES_DB_USER}:{POSTGRES_DB_PASSWORD}@localhost:{POSTGRES_DB_HOST_PORT}/{POSTGRES_DB_NAME}"
#
# print(DATABASE_URL)