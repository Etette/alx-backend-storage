-- script creates an index on the tables and the first letter of the name and score

CREATE INDEX idx_first_name ON names(name(1), score);
