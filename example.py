# This is an example feature definition file

from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, FileSource, ValueType

# Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.

girls_test_parquet = FileSource(
    path="/home/elk/repo_girls/data/girls.parquet",
    event_timestamp_column="event_timestamp",
)

# Define an entity for the driver. You can think of entity as a primary key used to
# fetch features.
PassengerId = Entity(name="girl_id", value_type=ValueType.INT64, description="girl id",)

# Our parquet files contain sample data that includes a driver_id column, timestamps and
# three feature column. Here we define a Feature View that will allow us to serve this
# data to our model online.
girls_test_view = FeatureView(
    name="girls_test_parquet",
    entities=["girl_id"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="Bust", dtype=ValueType.INT64),
        Feature(name="Waist", dtype=ValueType.INT64),
        Feature(name="Hips", dtype=ValueType.INT64),
    ],
    online=True,
    batch_source=girls_test_parquet,
    tags={},
)
print('ok')
