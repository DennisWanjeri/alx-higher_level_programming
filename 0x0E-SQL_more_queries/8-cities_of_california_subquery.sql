-- lists all the cities of Carlifornia
-- results ordered by ascending cities.id
SELECT `id`, `name`
       FROM `cities`
WHERE `state_id` IN
      (SELECT `id`
      	      FROM `states`
	      WHERE `name` = "California")
ORDER BY `id`;
