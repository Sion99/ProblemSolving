-- Lv4인데 많이 쉽다..
-- '%서울%' 이렇게 하지 않고 '서울%' 이렇게 해야됨

SELECT REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE 
FROM REST_INFO
NATURAL JOIN REST_REVIEW
WHERE ADDRESS LIKE '서울%'
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC