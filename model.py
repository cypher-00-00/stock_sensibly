import pandas as pd
from sklearn.linear_model import LinearRegression

def build_features(df, lags=5):
    data = pd.DataFrame(index=df.index)
    for i in range(1, lags + 1):
        data[f"lag{i}"] = df["Return"].shift(i)
    data["target"] = df["Return"]
    return data.dropna()

def train_and_evaluate(df, lags=5):
    data = build_features(df, lags)
    X = data.drop(columns="target")
    y = data["target"]

    split = int(len(data) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    model = LinearRegression().fit(X_train, y_train)
    preds = model.predict(X_test)

    direction_acc = ((preds > 0) == (y_test > 0)).mean()
    mae_model = (preds - y_test).abs().mean()
    mae_baseline = y_test.abs().mean()

    latest = pd.DataFrame([df["Return"].iloc[-lags:][::-1].values], columns=X.columns)
    next_return = model.predict(latest)[0]

    return {"direction_acc": direction_acc, "mae_model": mae_model,
            "mae_baseline": mae_baseline, "next_return": next_return}