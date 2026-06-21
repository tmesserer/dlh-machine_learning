-- this comment is a description of the script below
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN RETURN 0;
    ELSE RETURN (a / b);
    END IF;
END$$
DELIMITER ;

SELECT SafeDiv(10, 2);
SELECT SafeDiv(4, 5);
SELECT SafeDiv(6, 2);
SELECT SafeDiv(2, 3);
SELECT SafeDiv(6, 3);
SELECT SafeDiv(4, 5);
SELECT SafeDiv(10, 2);
SELECT SafeDiv(7, 0);
SELECT SafeDiv(6, 8);
SELECT SafeDiv(9, 89);