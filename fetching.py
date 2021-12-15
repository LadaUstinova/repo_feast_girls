from pprint import pprint
from feast import FeatureStore

store = FeatureStore(repo_path=".")

feature_vector = store.get_online_features(
    features=[
        "girls_test_parquet:Bust",
        "girls_test_parquet:Waist",
        "girls_test_parquet:Hips",
    ],
    entity_rows=[
        {"girl_id": 4},
        {"girl_id": 5},
    ],
).to_dict()

pprint(feature_vector)