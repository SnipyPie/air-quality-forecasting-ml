from app.features.build_features import load_data, build_features

df = load_data()
df_features = build_features(df)

print(df_features.head())
print("Shape:", df_features.shape)