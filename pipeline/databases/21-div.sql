-- this comment is a description of the script below
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT) 
RETURNS DECIMAL(5,4)
DETERMINISTIC
BEGIN
    IF b = 0 THEN RETURN 0;
    ELSE RETURN (a / b);
    END IF;
END$$
DELIMITER ;
