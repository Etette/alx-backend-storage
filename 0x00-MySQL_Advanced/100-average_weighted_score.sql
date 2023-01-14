-- Creates a stored procedure thaat computes and stores the
-- weighted score for a student.

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	UPDATE users
	SET overall_score = (SELECT AVG(score)
		FROM corrections
			WHERE corrections.user_id=user_id
			GROUP BY corrections.user_id)
		WHERE id=user_id;
END //
DELIMITER;
