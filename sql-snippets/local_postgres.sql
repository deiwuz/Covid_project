SELECT country, SUM(deaths) AS deaths 
FROM country_summary
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10; 