SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from member_profile
where date_format(date_of_birth, '%m') = '03'
and gender = 'W'
and tlno is not null
order by member_id;