-- lists all comedy shows
SELECT t.`title`
       FROM `tv_shows` AS t
       	    INNER JOIN `tv_show_genres` AS s
	    ON t.`id` = s.`show_id`

	    INNER JOIN `tv_genres` AS g
	    ON g.`id` = s.`genre_id`
	    WHERE g.`name` = "comedy"
	ORDER BY t.`title`;
