/*
🌟 Exercise 1: Detailed Medal Analysis
Task 1: Identify competitors who have won at least one medal in events spanning 
both Summer and Winter Olympics. Create a temporary table to store these competitors 
and their medal counts for each season, and then display the contents of this table.
*/
SELECT * FROM olympics.city -- id, city_name
SELECT * FROM olympics.games_competitor --id, games_id, person_id, age
SELECT * FROM olympics.competitor_event -- event_id, competitor_id, medal_id
SELECT * FROM olympics.medal -- id, medal_name
SELECT * FROM olympics.person -- id, full_name, gender, height, weight
SELECT * FROM olympics.person_region -- person_id, region_id
SELECT * FROM olympics.event -- id, sport_id, event_name
SELECT * FROM olympics.noc_region -- id, n region_name
SELECT * FROM olympics.games -- id, games_year, games_name, season
SELECT * FROM olympics.games_city -- games_id, city_id
SELECT * FROM olympics.sport -- id, sport_name
-------------------------------------------------------------------------------
CREATE TEMPORARY TABLE medal_by_season AS
SELECT ce.competitor_id, g.season, COUNT(medal_id) FROM olympics.competitor_event ce
JOIN olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN olympics.games g ON gc.games_id = g.id
WHERE medal_id != 4
GROUP BY ce.competitor_id, g.season
ORDER BY competitor_id

SELECT * FROM medal_by_season
/*
Task 2: Create a temporary table to store competitors who have won medals in 
exactly two different sports, and then use a subquery to identify the top 3 competitors 
with the highest total number of medals across all sports. 
Display the contents of this table.
*/

SELECT * FROM olympics.event -- id, sport_id, event_name
SELECT * FROM olympics.competitor_event -- event_id, competitor_id, medal_id

DROP TABLE IF EXISTS competitors_with_medals;

CREATE TEMPORARY TABLE competitors_with_medals AS 
SELECT ce.competitor_id, 
	   COUNT(medal_id) AS total_medals,
       COUNT(DISTINCT e.sport_id) AS distinct_sports
FROM olympics.competitor_event ce
JOIN olympics.event e ON ce.event_id = e.id
WHERE ce.medal_id != 4
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT sport_id) = 2

SELECT * FROM competitors_with_medals

SELECT competitor_id, total_medals 
FROM competitors_with_medals
WHERE 
    competitor_id IN (
        SELECT competitor_id 
        FROM competitors_with_medals
        ORDER BY total_medals DESC
        LIMIT 3
    )
ORDER BY total_medals DESC;


/*
🌟 Exercise 2: Region And Competitor Performance
Task 1: Retrieve the regions that have competitors who have won 
the highest number of medals in a single Olympic event. 
Use a subquery to determine the event with the highest number of medals 
for each competitor, and then display the top 5 regions with the highest total medals.
*/

WITH max_medals_per_event AS (
    SELECT 
        ce.competitor_id, 
        ce.event_id, 
        COUNT(ce.medal_id) AS medal_count
    FROM olympics.competitor_event ce
    WHERE ce.medal_id != 4
    GROUP BY ce.competitor_id, ce.event_id
    ORDER BY ce.competitor_id, medal_count DESC
),

competitor_region_medals AS (
    SELECT 
        pr.region_id, 
        mmpe.competitor_id, 
        MAX(mmpe.medal_count) AS max_medal_count
    FROM max_medals_per_event mmpe
    JOIN olympics.games_competitor gc ON mmpe.competitor_id = gc.id
    JOIN olympics.person_region pr ON gc.person_id = pr.person_id
    GROUP BY pr.region_id, mmpe.competitor_id
)

SELECT 
    cr.region_id, 
    SUM(cr.max_medal_count) AS total_medals
FROM competitor_region_medals cr
GROUP BY cr.region_id
ORDER BY total_medals DESC
LIMIT 5;
/*
Task 2: Create a temporary table to store competitors who have participated in 
more than three Olympic Games but have not won any medals. 
Retrieve and display the contents of this table, including their full names 
and the number of games they participated in.
*/
CREATE TEMPORARY TABLE competitors_no_medals AS 
SELECT gc.person_id, p.full_name, COUNT(gc.games_id) AS number_of_games 
FROM olympics.games_competitor gc --id, games_id, person_id, age
JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id -- event_id, competitor_id, medal_id
JOIN olympics.person p ON gc.person_id = p.id-- id, full_name, gender, height, weight
WHERE medal_id = 4
GROUP BY gc.person_id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3

SELECT * FROM competitors_no_medals