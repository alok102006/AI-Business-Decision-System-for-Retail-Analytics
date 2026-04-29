from insights import (
    loss_making_categories,
    discount_impact,
    profit_by_region,
    seasonal_trends
)

def loss_category_rule(loss):
    if loss["worst_category"]:
        return {
            "decision": f"Reduce losses in {loss['worst_category']} category",
            "priority": "HIGH",
            "confidence": 0.9,
            "reason": f"Category is generating highest loss ({round(loss['loss_value'],2)})"
        }
    return None

def discount_rule(discount):
    if discount["worst_discount_range"] in ["20-30%", "30%+"]:
        return {
            "decision": "Avoid high discounts (>20%)",
            "priority": "HIGH",
            "confidence": 0.85,
            "reason": "Higher discount ranges are leading to losses"
        }
    return None

def region_rule(region):
    return {
        "decision": f"Improve performance in {region['worst_region']} region",
        "priority": "MEDIUM",
        "confidence": 0.75,
        "reason": "Region has lowest profit contribution"
    }

def seasonal_rule(season):
    return {
        "decision": f"Plan campaigns for month {season['worst_month']}",
        "priority": "MEDIUM",
        "confidence": 0.7,
        "reason": "Month has lowest average sales"
    }


def generate_decisions(df):
    loss = loss_making_categories(df)
    discount = discount_impact(df)
    region = profit_by_region(df)
    season = seasonal_trends(df)

    rules = [
        loss_category_rule(loss),
        discount_rule(discount),
        region_rule(region),
        seasonal_rule(season)
    ]

    decisions = [r for r in rules if r is not None]

    PRIORITY_SCORE = {
        "HIGH": 3,
        "MEDIUM": 2,
        "LOW": 1
    }

    for d in decisions:
        d["score"] = PRIORITY_SCORE[d["priority"]] * d["confidence"]

    decisions = sorted(decisions, key=lambda x: x["score"], reverse=True)

    for i, d in enumerate(decisions, 1):
        d["rank"] = i

    return decisions