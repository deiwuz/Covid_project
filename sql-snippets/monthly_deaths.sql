CREATE TABLE `covid-project-481605.covid.monthly_summary` AS SELECT
DATE_TRUNC(date, MONTH) AS month, SUM(new_deceased) AS total_deaths
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE aggregation_level = 0
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10