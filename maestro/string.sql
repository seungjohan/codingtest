SELECT ANIMAL_ID, NAME, if(SEX_UPON_INTAKE like 'Intact%', 'X', 'O') as '중성화'
from ANIMAL_INS
order by ANIMAL_ID