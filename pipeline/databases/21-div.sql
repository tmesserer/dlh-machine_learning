-- this comment is a description of the script below
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT) 
RETURNS DOUBLE
DETERMINISTIC
BEGIN
    IF b = 0 THEN RETURN 0;
    ELSE RETURN (a / b);
    END IF;
END$$
DELIMITER ;
