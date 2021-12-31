# https://programmers.co.kr/learn/courses/30/lessons/59408

SELECT 
    COUNT(*) AS count 
FROM ( 
    SELECT NAME, 
    COUNT(*) 
    FROM ANIMAL_INS 
    GROUP BY NAME 
    HAVING NAME IS NOT NULL ) AS NAME_TABLE