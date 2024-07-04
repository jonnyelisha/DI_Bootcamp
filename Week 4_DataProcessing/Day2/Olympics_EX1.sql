--Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. Use a correlated subquery to achieve this.

SELECT 
	m.medal_name, AVG(gc.age)
FROM 
	olympics.competitor_event AS ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.medal m ON ce.medal_id = m.id
WHERE 
	m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY
	m.medal_name;
			   			


--Task 2  Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events.
-- Use nested subqueries to filter and aggregate the data.



SELECT 
		nr.region_name,
		COUNT(DISTINCT(gc.id)) AS unique_competitors	
FROM
		olympics.games_competitor AS gc
JOIN 
		olympics.person AS p ON gc.person_id = p.id
JOIN
		olympics.person_region AS pr ON pr.person_id = p.id
JOIN 
		olympics.noc_region AS nr ON pr.region_id = nr.id
WHERE
		gc.id IN (
			SELECT competitor_id
			FROM olympics.competitor_event
			GROUP BY competitor_id
			HAVING COUNT(event_id)>3)
GROUP BY
		nr.region_name
ORDER BY
		unique_competitors DESC LIMIT(5);



---Task 3: Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.

CREATE TEMPORARY TABLE medal_counts  (
    person_id INT,
    total_medals INT
);

INSERT INTO medal_counts(person_id, total_medals)
SELECT 
	gc.person_id,
	COUNT(ce.medal_id) AS total_medals
FROM
	olympics.competitor_event AS ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.person p ON gc.person_id = p.id
WHERE 
	ce.medal_id IN ('1','2','3')
GROUP BY
	gc.person_id
HAVING 
	COUNT(ce.medal_id)>2;

SELECT 
	p.full_name,
	medal_counts.total_medals
FROM
	medal_counts 
JOIN
	olympics.person p ON medal_counts.person_id = p.id
ORDER BY
	total_medals DESC;
---------------------------------------------------------------------------------------
SELECT
	p.full_name,
	COUNT(ce.medal_id) AS total_medals
FROM
	olympics.competitor_event AS ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.person p ON gc.person_id = p.id
WHERE ce.medal_id IN ('1','2','3')
GROUP BY
	p.full_name

ORDER BY
	total_medals DESC;
		

--Task 4: Use a subquery within a DELETE statement to remove records of competitors who have not won any medals from a temporary table created for analysis.

DROP TABLE IF EXISTS region_medals;

CREATE TEMPORARY TABLE region_medals(
	region_id INT,
	person_id INT,
	medal_id INT);
	
INSERT INTO region_medals(region_id, person_id, medal_id)
SELECT
	pr.region_id,
	pr.person_id,
	ce.medal_id
FROM
	olympics.competitor_event ce 
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.person_region pr ON gc.person_id = pr.person_id;

DELETE FROM
	region_medals rm
WHERE
	rm.medal_id = 4;
---
SELECT 
	nr.region_name,
	COUNT(rm.medal_id) AS won_medals
FROM
	region_medals rm
JOIN
	olympics.noc_region nr ON rm.region_id = nr.id
GROUP BY
	nr.region_name
ORDER BY
	won_medals DESC;


-- Exercise 2: Advanced Data Manipulation And Optimization
--Task 1: Update the heights of competitors based on the average height of competitors from the same region. Use a correlated subquery within the UPDATE statement.

DROP TABLE IF EXISTS nation_heights;

CREATE TEMPORARY TABLE nation_heights(region_id INT, region_name VARCHAR (100),average_heights NUMERIC);
INSERT INTO nation_heights(region_id, region_name, average_heights)
SELECT 
	pr.region_id,
	nr.region_name,
	AVG(p.height) AS avg_height
FROM
	olympics.person_region pr
JOIN
	olympics.noc_region nr ON pr.region_id = nr.id
JOIN
	olympics.person p ON pr.person_id = p.id
GROUP BY
	region_id,
	region_name
HAVING
	AVG(p.height) > 0
ORDER BY
	avg_height DESC;



UPDATE olympics.person p
SET height = (
	SELECT nh.average_heights
	FROM nation_heights AS nh
	JOIN(
			SELECT MIN(region_id) as region_id, person_id
			FROM olympics.person_region
			GROUP BY person_id
		) pr ON nh.region_id = pr.region_id
		WHERE pr.person_id = p.id
		LIMIT 1  -- Ensure a single value is returned
			)
WHERE 
	height = 0;
	
SELECT * FROM nation_heights;

--Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.



DROP TABLE IF EXISTS event_participant;

CREATE temp TABLE event_participant (person_id INT, games_id INT,  total_events NUMERIC);

INSERT INTO event_participant(person_id, games_id, total_events)
SELECT
	gc.person_id,
	gc.games_id,
	COUNT( DISTINCT ce.event_id) AS total_events
FROM
	olympics.competitor_event ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
WHERE
	gc.person_id IN(
					SELECT
						gc_in.person_id
					FROM
						olympics.games_competitor gc_in
					JOIN
						olympics.competitor_event ce_in ON gc_in.id = ce_in.competitor_id
					GROUP BY
						gc_in.person_id, gc_in.games_id
					HAVING
						COUNT(DISTINCT ce_in.event_id) > 1)
GROUP BY
	gc.person_id,
	gc.games_id
ORDER BY
	total_events DESC;

SELECT 
	p.full_name,
	g.games_name,
	ep.total_events
FROM 
	event_participant ep
JOIN
	olympics.games g ON g.id = ep.games_id
JOIN
	olympics.person p ON p.id = ep.person_id;



--Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. Use subqueries to calculate and compare averages.

WITH total_region_medals AS(
	SELECT ROUND(AVG(total_medals),2) AS avg_medals_competitors
	FROM(
		SELECT pr.person_id, COUNT(ce.medal_id) AS total_medals
		FROM olympics.competitor_event ce 
		LEFT JOIN olympics.games_competitor gc ON ce.competitor_id = gc.id
		LEFT JOIN olympics.person_region pr ON gc.person_id = pr.person_id
		WHERE
			ce.medal_id IN ('1','2','3')
		GROUP BY
			pr.person_id
		) AS medals_per_person
	),
	
-- 2nd Step: Subquery to calculate average medals per region
region_avg_medals AS(
	SELECT region_id, ROUND(AVG(total_medals),2) AS avg_medals
	FROM(
		SELECT pr.region_id, pr.person_id, COUNT(ce.medal_id) AS total_medals
		FROM olympics.competitor_event ce 
		LEFT JOIN olympics.games_competitor gc ON ce.competitor_id = gc.id
		LEFT JOIN olympics.person_region pr ON gc.person_id = pr.person_id
		WHERE
			ce.medal_id IN ('1','2','3')
		GROUP BY
			pr.region_id, pr.person_id
		)AS region_medal_per_person
	GROUP BY region_id
)
-- 3rd: Final query to identify regions where avg_medals > overall average
SELECT nr.region_name, ram.avg_medals
FROM region_avg_medals ram
LEFT JOIN olympics.noc_region nr ON ram.region_id = nr.id
WHERE
	ram.avg_medals > (SELECT avg_medals_competitors FROM total_region_medals)
ORDER BY 
          ram.avg_medals DESC;




--  Task 4: 
--Create a temporary table to track competitors’ participation across different seasons
-- and identify those who have participated in both Summer and Winter games.

DROP TABLE IF EXISTS com_participation;

CREATE TEMPORARY TABLE com_participation(person_id INT, participated_games BOOLEAN);

INSERT INTO com_participation(person_id, participated_games)
-- 1st identifying competitors in more than one game per season 
SELECT
	p.id AS person_id,
	CASE
		WHEN EXISTS(
			SELECT 1
			FROM olympics.games_competitor gc_1
			JOIN olympics.games g_1 ON gc_1.games_id = g_1.id
			WHERE gc_1.person_id = p.id AND g_1.season = 'Summer'
		) AND EXISTS(
			SELECT 1
			FROM olympics.games_competitor gc_2
			JOIN olympics.games g_2 ON gc_2.games_id = g_2.id
			WHERE gc_2.person_id = p.id AND g_2.season = 'Winter'
		)
		THEN TRUE
		ELSE FALSE
	END AS participated_games
FROM olympics.person p;

SELECT p.full_name
FROM olympics.person p
JOIN com_participation cp ON cp.person_id = p.id
WHERE participated_games = TRUE;

