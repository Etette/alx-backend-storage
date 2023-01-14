-- script creates a function that divides and returns the 
-- first by the second number or returns 0 if second number == 0

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	  DECLARE num FLOAT DEFAULT 0;

	  IF b != 0 THEN
		    SET num = a / b;
		  END IF;
		  RETURN num;
END //
