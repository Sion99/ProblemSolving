select INGREDIENT_TYPE, sum(total_order) as TOTAL_ORDER
from first_half
natural join icecream_info
group by INGREDIENT_TYPE;