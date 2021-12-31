# https://programmers.co.kr/learn/courses/30/lessons/59412?language=mysql

SELECT HOUR(DATETIME) AS hour, COUNT(*) AS count
FROM ANIMAL_OUTS
GROUP BY hour
HAVING hour BETWEEN 9 AND 19
ORDER BY hour;