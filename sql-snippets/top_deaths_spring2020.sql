SELECT country_name, SUM(new_deceased) AS total_deaths
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE date BETWEEN '2020-03-01' AND '2020-05-31'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10