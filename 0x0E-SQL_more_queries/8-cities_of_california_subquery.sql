-- cities of california subquery tell me now
SELECT id, name FROM cities WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
-- queries like requesting the information.