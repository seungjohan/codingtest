SELECT A.NAME, A.DATETIME FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY DATETIME LIMIT 3



 SELECT INS.NAME, INS.DATETIME
 FROM ANIMAL_INS AS INS
 LEFT JOIN ANIMAL_OUTS AS OUTS
 ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
 WHERE INS.ANIMAL_ID NOT IN (SELECT OUTS.ANIMAL_ID
                            FROM ANIMAL_OUTS AS OUTS)
 ORDER BY INS.DATETIME
 LIMIT 3;