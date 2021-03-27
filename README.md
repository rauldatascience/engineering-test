# engineering-test

## deduplication query with database related to the schema


I fill the database with the following schema

```
[
    {
        "mode": "REQUIRED",
        "name": "id",
        "type": "UUID"
    },
    {
        "mode": "REQUIRED",
        "name": "insert_time",
        "type": "TIMESTAMP"
    },
    {
        "mode": "REQUIRED",
        "name": "tx_amount",
        "type": "FLOAT"
    },
    {
        "mode": "REQUIRED",
        "name": "tx_type",
        "type": "STRING"
    },
    {
        "mode": "REQUIRED",
        "name": "status",
        "type": "STRING"
    }
]
```

Rule : 

The table given to you cannot be updated, so if there is a change in status of a transaction the new data is inserted instead of updating the status of the transaction, it will insert a new row with the same id and insert time based on the time when the row is inserted. You are assigned to create a view that only shows the most updated transactions for each id, so there is no duplicate id inside the view.

![alt text](https://github.com/rauldatascience/engineering-test/blob/main/figure/scenario_database.png?raw=true)

## Solution Query

```
SELECT 
    *
FROM `bigdata-etl-2.data_taxi.testing_deduplication`
WHERE insert_time =  (
SELECT 
    max(insert_time) as updated_data
FROM `bigdata-etl-2.data_taxi.testing_deduplication`
WHERE id = 1234)
```

![alt text](https://github.com/rauldatascience/engineering-test/blob/main/figure/deduplication_query.png?raw=true)
