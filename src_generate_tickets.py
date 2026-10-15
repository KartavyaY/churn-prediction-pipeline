import pandas as pd, numpy as np
np.random.seed(42)

cust = pd.read_csv("data/raw/telco.csv")
n = 15000
tickets = pd.DataFrame({
    "ticket_id": range(n),
    "customerID": np.random.choice(cust.customerID, n),
    "ticket_date": pd.to_datetime("2024-01-01") + pd.to_timedelta(np.random.randint(0, 365, n), unit="D"),
    "category": np.random.choice(["billing", "network", "service", "other"], n),
    "resolution_hrs": np.random.randint(1, 72, n),
})
tickets.to_csv("data/raw/tickets.csv", index=False)
print(tickets.shape)
