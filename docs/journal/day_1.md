# Day 1

## Learned
- Challenges in tracking and deploying ML models, and how MLflow addresses them.
- Core MLflow components: Tracking, Models, Model Registry, Datasets.
- MLflow Tracking concepts: runs, experiments, backend store, artifact store.

## Decisions
- Using NEPSE (Nepal Stock Exchange) data for the learning project.
- Data library: [nepsepy](https://github.com/menaceXnadin/nepsepy). It is free and claims to support live market data (not yet verified).
- First model: simple linear regression. Sentiment analysis comes later.

## Done
- Set up the project with uv and installed `mlflow` and `nepsepy`.

## Problems and fixes
- `uv add nepsey` failed because of a typo. The correct name is `nepsepy`.
- `client.gainers()` does not exist. The correct method is `top_gainers()`.
- Test script ran but printed nothing. Still debugging.

## Next
- Get `test_nepse.py` printing real data.
- Find the method for historical prices or index history.
- Save raw data to `data/raw/` as Parquet.