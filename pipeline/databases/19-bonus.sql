-- this comment is a description of the script below
DELIMITER $$
CREATE PROCEDURE AddBonus
    (IN user_id VARCHAR(255), IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (id, name) VALUES (DEFAULT, project_name)
        END IF;
    INSERT INTO corrections 
        IF project_name NOT IN (
            SELECT name FROM projects a
                INNER JOIN corrections b
                ON a.id = b.project_id
            ) 
                THEN VALUE(name = project_name), 
        VALUE (score = score)
END$$
DELIMITER ;
