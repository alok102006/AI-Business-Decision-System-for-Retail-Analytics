import pandas as pd


def loss_making_categories(df):
    result = df.groupby('sub_category')['profit'].sum().sort_values()
    losses = result[result < 0]

    return {
        "data": losses,
        "worst_category": losses.idxmin() if not losses.empty else None,
        "loss_value": losses.min() if not losses.empty else 0
    }


def high_discount_losses(df):
    filtered = df[(df['discount'] > 0.2) & (df['profit'] < 0)]

    return {
        "count": len(filtered),
        "sample": filtered.head()
    }


def monthly_sales(df):
    month = df['order_date'].dt.month
    monthly = df.groupby(month)['sales'].mean()

    return {
        "data": monthly,
        "best_month": monthly.idxmax(),
        "worst_month": monthly.idxmin()
    }


def profit_making_categories(df):
    pro = df.groupby('category')['profit'].sum().sort_values(ascending=False)

    return {
        "data": pro,
        "top_category": pro.idxmax(),
        "top_profit": pro.max()
    }


def top_profitable_products(df, n=5):
    top = df.groupby('product_name')['profit'].sum().sort_values(ascending=False).head(n)

    return top


def top_loss_making_products(df, n=5):
    top_loss = df.groupby('product_name')['profit'].sum().sort_values().head(n)

    return top_loss


def profit_by_region(df):
    region_profit = df.groupby('region')['profit'].sum().sort_values(ascending=False)

    return {
        "data": region_profit,
        "best_region": region_profit.idxmax(),
        "worst_region": region_profit.idxmin()
    }


def discount_impact(df):
    bins = pd.cut(
        df['discount'],
        bins=[-0.01, 0.1, 0.2, 0.3, 1],
        labels=['0-10%', '10-20%', '20-30%', '30%+']
    )

    discount_profit = df.groupby(bins)['profit'].mean().sort_values()

    return {
        "data": discount_profit,
        "worst_discount_range": discount_profit.idxmin()
    }


def seasonal_trends(df):
    month = df['order_date'].dt.month
    seasonal = df.groupby(month)['sales'].mean().sort_values(ascending=False)

    return {
        "data": seasonal,
        "best_month": seasonal.idxmax(),
        "worst_month": seasonal.idxmin()
    }


def worst_monthly_profit(df):
    month = df['order_date'].dt.month
    monthly_profit = df.groupby(month)['profit'].sum()

    worst_month = monthly_profit.idxmin()

    return {
        "month": worst_month,
        "profit": monthly_profit[worst_month]
    }


def worst_monthly_sales(df):
    month = df['order_date'].dt.month
    monthly_sales = df.groupby(month)['sales'].sum()

    worst_month = monthly_sales.idxmin()

    return {
        "month": worst_month,
        "sales": monthly_sales[worst_month]
    }


# 🔥 MOST IMPORTANT FUNCTION
def generate_summary(df):
    loss_cat = loss_making_categories(df)
    discount = discount_impact(df)
    region = profit_by_region(df)
    season = seasonal_trends(df)

    summary = {
        "key_insights": [
            f"Worst category: {loss_cat['worst_category']} with loss {round(loss_cat['loss_value'],2)}",
            f"Worst discount range: {discount['worst_discount_range']}",
            f"Worst region: {region['worst_region']}",
            f"Worst month: {season['worst_month']}"
        ]
    }

    return summary