CREATE DATABASE IF NOT EXISTS rto_seva CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'rto_user'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON rto_seva.* TO 'rto_user'@'localhost';
FLUSH PRIVILEGES;
