# dbimp-project
Sandy Wood, Sara Alotaibi

Files for CS 487 final group project - benchmarking PostgreSQL on an Ubuntu 20.04 LTS VM.

## Part 1: Data Generation and System Selection

For simplicity, we decided to analyze only PostgreSQL, as it was the database system we were the most familiar with. We also decided it would allow us more time to experiment if we only needed to maintain and become familiar with a single system.

### Data Generation

[A python data generation script](https://github.com/sandyaspen/dbimp-project/blob/main/data/data_generator.py) was created to enable us to make datasets of custom sizes that still adhere to the structure as explained in the Wisconsin Database Benchmark paper. Example csv files can be found in the [data directory.](https://github.com/sandyaspen/dbimp-project/tree/main/data) Screenshots showing the imported data tables can be found in the [screenshots directory.](https://github.com/sandyaspen/dbimp-project/tree/main/data)

### System Selection

We chose to work with a VM for this project. We are analyzing the effects of changing the configurations for PostgreSQL. In an attempt to create similar resdults across different hardware, we are creating a virtual machine instance to perform our tests in. We are using Ubuntu 20.04 LTS as the operating system, as it is a very popular linux distribution and is often installed on virtual machines. We ran into a few issues setting up a database server and connecting pgadmin to our server, which were mostly related to the VM's virtual networking.

### Benchmark Design

The primary goal of our benchmark is to evaluate different settings of the Postgres memory parameters, and to determine the optimal settings for these parameters given our specific workloads and system configuration. The design document can be found [here.](https://github.com/sandyaspen/dbimp-project/blob/main/documents/benchmark_design.pdf)

### Benchmark Results Presentation

The results for the project are included in a slideshow presentation [here.](https://github.com/sandyaspen/dbimp-project/blob/main/documents/ResultsPresentation.pdf)