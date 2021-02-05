# dbimp-project
Sandy Wood, Sara Alotaibi

Files for CS 487 final group project - benchmarking PostgreSQL on an Ubuntu 20.04 LTS VM.

## Part 1: Data Generation and System Selection

For simplicity, we decided to analyze only PostgreSQL, as it was the database system we were the most familiar with. We also decided it would allow us more time to experiment if we only needed to maintain and become familiar with a single system.

### Data Generation

Three test data files were generated for this project, the same files as used in the Wisconsin Benchmark. Interestingly, it was fairly difficult to find a good example of such a generator, many of the generators were for more common types of data such as phone numbers. We decided to use the data generator component of sqalpel's implementation of a wisconsin benchmark tool, found at: https://github.com/sqalpel/wisconsin/tree/master/src. This tool was freely available and produced the data that we desired in an easy-to-import format. We only needed to edit the output to be delimited with commas rather than pipes, and then imported them into our database using PostgreSQL's \copy command. The final csv files can be found in the [data directory.](https://github.com/sandyaspen/dbimp-project/tree/main/data) Screenshots showing the imported datat tables can be found in the [screenshots directory](https://github.com/sandyaspen/dbimp-project/tree/main/data)

### System Selection

We chose to work with a VM for this project. We are analyzing the effects of changing the configurations for PostgreSQL. In an attempt to create similar resdults across different hardware, we are creating a virtual machine instance to perform our tests in. We are using Ubuntu 20.04 LTS as the operating system, as it is a very popular linux distribution and is often installed on virtual machines. We ran into a few issues setting up a database server and connecting pgadmin to our server, which were mostly related to the VM's virtual networking.
