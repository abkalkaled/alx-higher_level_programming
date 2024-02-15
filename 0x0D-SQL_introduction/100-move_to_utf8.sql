-- Script converts hbtn_0c_0 database to UTF8
ALTER DATABASE $database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE $database.$table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE $database.$table MODIFY $field VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
