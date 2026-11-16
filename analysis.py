import pandas as pd
df = pd.read_csv("dceu_films.csv")
df["multiple"] = df.worldwide_gross_musd / df.budget_musd
df["profit_proxy_musd"] = df.worldwide_gross_musd - 2 * df.budget_musd  # rough break-even: gross >= 2x budget
print(df.sort_values("multiple", ascending=False)[["title","multiple","rt_critics_pct"]].round(2))
print("Correlation (RT vs multiple):", round(df.rt_critics_pct.corr(df.multiple), 2))
print(df.groupby("director").multiple.mean().sort_values(ascending=False).round(2))
