-- this comment is a description of the script below
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser
    (IN user_id VARCHAR(255))
BEGIN
    DECLARE avg_score FLOAT;
    SELECT AVG(score) INTO avg_score FROM corrections a WHERE a.user_id = user_id;
    UPDATE users b SET b.average_score = avg_score WHERE id = user_id;
END$$
DELIMITER ;

