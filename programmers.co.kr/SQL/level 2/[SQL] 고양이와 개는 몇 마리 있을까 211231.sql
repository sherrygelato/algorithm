# https://programmers.co.kr/learn/courses/30/lessons/59040?language=mysql

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) 
FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE