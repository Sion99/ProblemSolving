-- Lv4인데 많이 쉽다..
-- '%서울%' 이렇게 하지 않고 '서울%' 이렇게 해야됨

SELECT REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE from rest_info
natural join rest_review
where address like '서울%'
group by REST_ID
order by SCORE desc, FAVORITES desc