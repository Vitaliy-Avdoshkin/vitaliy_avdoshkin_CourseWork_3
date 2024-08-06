from src.reports import spending_by_category
from src.services import investment_bank, transactions
from src.utils import df
from src.views import home_page

print(home_page(df))
print(investment_bank("2021-12", transactions, 10))
print(spending_by_category(df, "Транспорт"))
