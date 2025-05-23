
CREATE DATABASE admin_db;
CREATE USER admin_rw WITH PASSWORD 'admin_pass';
CREATE USER user_reader WITH PASSWORD 'reader_pass';


GRANT ALL PRIVILEGES ON DATABASE admin_db TO admin_rw;
GRANT CONNECT ON DATABASE admin_db TO user_reader;


\c admin_db;


GRANT ALL PRIVILEGES ON SCHEMA public TO admin_rw;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO user_reader;


ALTER DEFAULT PRIVILEGES FOR USER admin_rw IN SCHEMA public
GRANT SELECT ON TABLES TO user_reader;
