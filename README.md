# To UDFs and Beyond: Demonstration of a Fully Decomposed Data Processor for General Data Wrangling Tasks


To follow along with our demonstration simply clone this repository and run

```bash
docker-compose up
```

You'll now have a working JODA setup. You can access the web interface at http://localhost:8080. 

You can find the language specification at https://joda-explore.github.io/JODA/

Additionally, does the `example_queries.txt` file contain some example queries that you can run in the web interface.

## Example modules

The `modules` folder contains some example modules that you can use to get started with user-defined-modules JODA.

The included directoies are:
- `aggregation`: Contains modules that can be used to aggregate multiple documents
- `export`: Contains modules that can be used to export data from JODA
- `ìmport`: Contains modules that can be used to import data into JODA
- `index`: Contains modules that can be used to create custom indices
- `value`: Contains modules that can be used to create user-defined functions for usage in the JODA query language

## Database (optional)

If you want to experiment with the database connection modules you can run 

```bash
./initEmptyDB.sh
``` 
to initialize an empty database with an empty table in it.
The database will be initialized within the docker container started with the remaining JODA services.