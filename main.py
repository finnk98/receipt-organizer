food_keywords = ["billa", "mcdonald", "spar", "hofer", "lebensmittel"]
transport_keywords = ["wiener linien", "öbb", "ticket", "monatskarte"]
shopping_keywords = ["h&m", "zara", "shop", "online"]

with open("receipts.txt", "r", encoding="utf-8") as f:
    receipts = f.readlines()

for receipt in receipts:
    receipt = receipt.strip()
    receipt_lower = receipt.lower()

    if any(keyword in receipt_lower for keyword in food_keywords):
        category = "Food"
    elif any(keyword in receipt_lower for keyword in transport_keywords):
        category = "Transport"
    elif any(keyword in receipt_lower for keyword in shopping_keywords):
        category = "Shopping"
    else:
        category = "Unknown"

    print(f"{receipt} → {category}")