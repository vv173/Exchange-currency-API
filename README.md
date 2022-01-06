# Exchange-currency-API 💰
Code regularly (e.g. every 3 hours) downloads the EURO exchange rate for a few selected currencies (max 5) provided by the API 

To run the solution, you should have the following files: Dockerfile 🐳, runner (a file for CRON operation), and a script called restic.sh - to start backups.

How it works: Python script downloads the EURO exchange rate for 5 currencies via an external API every 3 hours. Builds defined CRON when building Docker Dockerfile 🐳 with root file. The saved .csv files are backed up using the restic backup application, which is started by the restic.sh script

How to run the solution:

1) Build a Docker image with the command

        `docker build -t v17v3/apicronbackup:v3.1 .`

2) Run the docker container with the command

        `docker run -dt --env API_KEY='your_valid_api_key' v17v3/apicronbackup:v3.1`

Useful links:

DockerHub: https://hub.docker.com/r/v17v3/apicronbackup 🐳
