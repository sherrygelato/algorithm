# https://programmers.co.kr/learn/courses/30/lessons/59047?language=mysql

SELECT 
    ANIMAL_ID, 
    NAME
FROM 
    ANIMAL_INS 
WHERE (
    NAME LIKE '%EL%'
    AND
    ANIMAL_TYPE = 'Dog'
)
ORDER BY NAME;