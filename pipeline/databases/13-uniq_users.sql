-- this comment is a description of the script below
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
    email STR(255Char) never null UNIQUE
    name STR(255Char)
)