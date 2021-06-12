FROM python:3.9.5-alpine3.12


RUN apk add --update bash
RUN pip install requests
RUN apk add restic


ENV RESTIC_PASSWORD="VVdtsc4v5QtUCNXA"
ENV RESTIC_REPOSITORY=/srv/backup


RUN ["mkdir", "/bin/exchange"]
RUN ["mkdir", "/srv/backup"]
RUN restic init --repo /srv/backup

COPY python_api.py /bin/exchange/
COPY restic.sh /bin/exchange/
COPY root /var/spool/cron/crontabs/

RUN chmod +x /bin/exchange/python_api.py
RUN chmod +x /bin/exchange/restic.sh
CMD crond -l 2 -f


