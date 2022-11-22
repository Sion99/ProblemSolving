SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(tlno, "NONE") as TLNO
from patient
where age <= 12
and gend_cd = 'W'
order by AGE desc, PT_NAME;