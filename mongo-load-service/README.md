[//]: # (Copyright \(c\) 2023 by Delphix. All rights reserved.)

# Mongo Hyperscale Compliance Unload Service

This is an unload service created for Mongo DB.

## Development:

For contributing to the project, follow the below steps:

### Pre requisites

Python 3.9 should be installed on your system.

    python3.9 -V

For creating virtual environment and installing all the dependencies:

    make env

For running the FastAPI project:

    make run

In case you want to run the app inside a docker container:
    
    make docker-run

This command will first remove the existing docker container and image if it exists,
then build a new docker image and at create and run a docker container with the app inside it.



## Testing

This will run all the unit tests and generate the pytest and coverage reports.

    make tests

