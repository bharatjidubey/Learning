
# Assets : things a business own like money and machinery. paise or machine or jammen factory ki jo bacha jaa sake.

# Cureent Assets : Assets converted in cash, sold within a year usually. esi chij jise jaldi se bach ke cash liya jaa sake

# Recivables : customer who didnt give money, after taking the service. udhaar paisa jo log denge.

# Inventory : Goods held for sale or to make product. saman jo ki bacha jayega ya usse kuch banaya jayenga.

# Equipment : Tools, Machines etc

# Liabilities : amount / debts a business owe to other people or organization. Company ke upper jo karz hai loan ya supplier bill.

# Current Liabilities : debts that are goning to be paid in a year. esa udhar jise hum saal bhar mai chuka dete hai.

# Payables : money has to given to supplier for purchasing goods.

# Loan : debts . karz / udhar.

# Equity : owners money, money remain after deducting liabilities. sabhi kharch hatane ke baad ka bacccha hua paise jo malik hai.

# Share Capital : amt uinvested in a company by an individual in exchange of its share..

# Revenue : Money earned by selling goods. saman bachne ke baad jo paisa aya.

# Expanse : money used to run the bussiness.

# Net Profit : Profit after deducting expanses and taxes etc. paise jo ke sabhi tax ya company kharach ke baad bacha.

# Debt : Money Borrowed.

# Liquidity : amt a business can repay its short-term debts.

# Leverage : Amt. of Debt taken to run the business.

# Margin : Proportion of Revenue that remain as profit.

# Return : % Profit earned relative to money invested. 


# Assets = Liabilities + Equity
# Current ratio : Current assets / current liabilities
# Quick ratio : (Current assets - inventory) / current liabilities
# Debt-equity ratio : Total debt / shareholders' equity
# Net profit margin : (Net profit / revenue) x 100
# Return on equity : (Net profit / shareholders' equity) x 100

def current_ratio(current_assets, current_liabilities):
    """Current ratio = current assets / current liabilities."""
    if current_liabilities <= 0:
        raise ValueError("Current liabilities must be positive")
    return current_assets / current_liabilities

def quick_ratio(current_assets, inventory, current_liabilities):
    """Quick ratio = (current assets - inventory) / current liabilities."""
    if current_liabilities <= 0:
        raise ValueError("Current liabilities must be positive")
    return (current_assets - inventory) / current_liabilities

def debt_equity_ratio(total_debt, equity):
    """Debt-equity ratio = total debt / shareholders' equity."""
    if equity <= 0:
        raise ValueError("Shareholders' equity must be positive")
    return total_debt / equity

def net_profit_margin(net_profit, revenue):
    """Net profit margin (%) = net profit / revenue x 100."""
    if revenue <= 0:
        raise ValueError("Revenue must be positive")
    return net_profit / revenue * 100

def return_on_equity(net_profit, equity):
    """Return on equity (%) = net profit / shareholders' equity x 100."""
    if equity <= 0:
        raise ValueError("Shareholders' equity must be positive")
    return net_profit / equity * 100

def interpret_current_ratio(ratio):
    if ratio < 1:
        return "weak liquidity: short-term debts exceed short-term assets"
    elif ratio < 2:
        return "adequate liquidity"
    return "strong liquidity"









# =========   GOOD WILL ===============




# Profit : money a business earns after deducting its expenses from its revenue.

# Average Profit : sum of profits over several years divided by the number of years.

# Weighted Average Profit —  An average in which some years' profits receive more importance than others.

# Weight — A number that determines how much importance a particular year's profit receives.

# Goodwill — The value associated with a business's reputation, customer relationships, brand, location and ability to earn profits.

# Years' Purchase — A multiplier representing how many years of a specified profit measure are used to estimate goodwill.

# Normal Profit : The profit a business is expected to earn under normal industry conditions.

# Super Profit : The profit earned by a business above its normal expected profit.

# Normal Rate of Return : The percentage return normally expected from an investment in comparable circumstances.

# Capitalisation of Profit : A method of estimating business value by converting annual profit into capital value using the normal rate of return.

# Net Assets : The total value of a business's assets minus its total liabilities.


# Shares : Units representing ownership in a company.

# Shareholders : Individuals or entities that own shares in a company.

# Net Asset Value per Share : The net assets available to shareholders divided by the total number of shares.

# Dividend : A portion of a company's profits distributed to its shareholders.

# Dividend Rate : The dividend expressed as a percentage of the share's nominal or face value.

# Paid-up Value : The amount of share capital actually paid by shareholders for each share.

# Yield Value per Share : The estimated value of a share calculated using its dividend rate and the normal rate of return.

# def average_profit(profits):
#     """Return the simple average of the profits."""
#     if not profits:
#         raise ValueError("At least one year of profit is needed")
#     return sum(profits) / len(profits)

# def weighted_average_profit(profits, weights=None):
#     """Return sum(profit x weight) / sum(weights); weights default to 1, 2, 3, ..."""
#     if not profits:
#         raise ValueError("At least one year of profit is needed")
#     if weights is None:
#         weights = list(range(1, len(profits) + 1))
#     if len(weights) != len(profits):
#         raise ValueError("Need one weight per year")
#     weighted_total = sum(p * w for p, w in zip(profits, weights))
#     return weighted_total / sum(weights)

# def goodwill_average(profits, years_purchase):
#     return average_profit(profits) * years_purchase

# def goodwill_weighted(profits, years_purchase, weights=None):
#     return weighted_average_profit(profits, weights) * years_purchase

# def goodwill_super_profit(profits, normal_profit, years_purchase):
#     super_profit = average_profit(profits) - normal_profit
#     return super_profit * years_purchase

# def goodwill_capitalisation(profits, normal_rate, net_assets):
#     if normal_rate <= 0:
#         raise ValueError("Normal rate must be positive")
#     return average_profit(profits) * 100 / normal_rate - net_assets

# def net_asset_value_per_share(total_assets, total_liabilities, shares):
#     if shares <= 0:
#         raise ValueError("Number of shares must be positive")
#     return (total_assets - total_liabilities) / shares

# def yield_value_per_share(dividend_rate, normal_rate, paid_up_value=100):
#     if normal_rate <= 0:
#         raise ValueError("Normal rate must be positive")
#     return dividend_rate / normal_rate * paid_up_value