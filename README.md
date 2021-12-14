# Exchange-currency-API 💰
Code regularly (e.g. every 3 hours) downloads the EURO exchange rate for a few selected currencies (max 5) provided by the API 

To run the solution, you should have the following files: Dockerfile 🐳, root (a file for CRON operation), and a script called restic.sh - to start backups.

How it works: Python script downloads the EURO exchange rate for 5 currencies via an external API every 3 hours. Builds defined CRON when building Docker Dockerfile 🐳 with root file. The saved .csv files are backed up using the restic client, which is built by the restic.sh script

How to run the solution:

1) Build a Docker image with the command '🐳 docker image build'. (All files must be in the same directory as Dockerfile 🐳)

2) Run the docker container with the command '🐳 **docker container run -dt --name** "container name" "image name"'.

Useful links:

DockerHub: https://hub.docker.com/r/v17v3/apicronbackup/tags 🐳
