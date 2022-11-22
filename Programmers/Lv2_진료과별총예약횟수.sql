-- 계속 틀리길래 뭐가 문제인지 싶었는데 제일 마지막 order by 절에서 '진료과코드' 따옴표 없이 진료과코드
-- 이렇게 써야했음..

SELECT MCDP_CD AS '진료과코드', COUNT(APNT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE date_format(APNT_YMD, '%m') = '05'
GROUP BY MCDP_CD
ORDER BY 5월예약건수, 진료과코드