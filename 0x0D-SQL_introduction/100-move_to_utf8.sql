-- Convert a database to utf8mb4
USE hbtn_0c_0;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
ALTER TABLE first_table COVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
