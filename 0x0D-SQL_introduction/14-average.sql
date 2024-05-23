-- calculate the avg of score in the scond_table
ALTER TABLE second_table ADD COLUMN IF NOT EXISTS average DECIMAL(10,4);
UPDATE second_table SET average = (SELECT AVG(score) FROM second_table);
SELECT avrage FROM second_table;
