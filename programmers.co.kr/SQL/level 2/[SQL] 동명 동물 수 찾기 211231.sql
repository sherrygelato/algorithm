# https://programmers.co.kr/learn/courses/30/lessons/59041?language=mysql

SELECT
    NAME,
    count(*) AS COUNT
FROM
    ANIMAL_INS
GROUP BY
    NAME
HAVING 
    COUNT(NAME) >= 2 
ORDER BY 
    NAME;