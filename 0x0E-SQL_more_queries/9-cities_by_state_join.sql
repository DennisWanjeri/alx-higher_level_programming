-- lists all cities in hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
SELECT c.`id`, c.`name`, s.`name`
       FROM `cities` AS c
       	    INNER JOIN `states` AS s
	    ON c.`state_id` = s.`id`
       ORDER BY c.`id`;
