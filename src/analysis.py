def calculate_metrics(df):
    metrics = {}

    metrics['total_sales'] = df['sales'].sum()
    metrics['total_profit'] = df['profit'].sum()
    metrics['profit_margin'] = round(metrics['total_profit'] / metrics['total_sales'], 2)
    metrics['avg_discount'] = round(df['discount'].mean(), 2)

    return metrics