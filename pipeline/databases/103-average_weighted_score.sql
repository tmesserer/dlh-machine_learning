-- this comment is a description of the script below
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser
    (IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SELECT SUM((a.score * b.weight)) / (SUM(b.weight)) INTO avg_score FROM corrections a
        INNER JOIN projects b ON a.project_id = b.id
    WHERE a.user_id = user_id;
    UPDATE users c SET c.average_score = avg_score WHERE id = user_id;
END$$
DELIMITER ;
