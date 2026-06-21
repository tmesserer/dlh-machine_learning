-- this comment is a description of the script below
DELIMITER $$
CREATE PROCEDURE AddBonus
    (IN user_id VARCHAR(255), IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    DECLARE project_id INT;
    IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (id, name) VALUES (DEFAULT, project_name);
    END IF;
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    INSERT INTO corrections (user_id, project_id, score) 
        VALUES(user_id, project_id, score);
END$$
DELIMITER ;
