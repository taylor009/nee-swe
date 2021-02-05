## eIQ Mobility SWE Take-Home Assignment

This repository includes instructions for the eIQ Mobility take home assignment.

# SWE Take-Home Assignment

A simple Flask-Kubernetes-Docker web application that allows the user to upload a .CSV file. On successful file upload, the application should perform the following validations:

* Checks whether the uploaded is a .CSV and not any other format.
* Check whether the .CSV file has exactly 10 rows and 3 columns.
* Checks whether the data is present in each cell (.CSV file is "complete"). A "complete" sample test.csv is available in this repository for testing purposes.

Build, push, and deploy a docker container on Kubernetes Engine that performs the above validations for an uploaded .csv file.

The submission should include:

* A public link to the flask web application
* Entire codebase along with Dockerfile
* README explaining the solution and all the commands used for docker build, push, and Kubernetes deployment

# Tips
* In addition to docker, kubernetes engine, and Flask; you are free use to any additional language/tool/services.
* You may use the the promotional Google Cloud Platform credits for access to Kubernetes and other services you may need to compile this application. Choice of cloud platform is entirely yours.
* If you do not have promotional credits, you may create a new Google/Gmail account for $300 promotional credits. Let me know if you face any issues in this regard.
* Use best practices.
