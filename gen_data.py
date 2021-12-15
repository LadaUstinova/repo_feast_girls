from datetime import datetime, timedelta
import pandas as pd

from feast import FeatureStore

# The entity dataframe is the dataframe we want to enrich with feature values
entity_df = pd.DataFrame.from_dict(
    {
        "girl_id": [1, 2, 3], 
        "event_timestamp": [
            datetime.now() - timedelta(minutes=11),
            datetime.now() - timedelta(minutes=36),
            datetime.now() - timedelta(minutes=73)],
    }
)

store = FeatureStore(repo_path=".")

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "girls_test_parquet:Bust",
        "girls_test_parquet:Waist",
        "girls_test_parquet:Hips",
    ],
).to_df()

print("----- Feature schema -----\n")
print(training_df.info())

print()
print("----- Example features -----\n")
print(training_df.head())