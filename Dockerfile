FROM python:3.11.0a3-alpine3.15

RUN apk update && \
    apk add restic && \
    pip install --upgrade pip

RUN adduser -D runner
USER runner
WORKDIR /home/runner

COPY --chown=runner:runner requirements.txt .
COPY --chown=runner:runner python_api.py .
COPY --chown=runner:runner restic.sh .
RUN chmod +x ./python_api.py
RUN chmod +x ./restic.sh

USER runner

ENV RESTIC_PASSWORD="VVdtsc4v5QtUCNXA"
ENV RESTIC_REPOSITORY=/home/runner/backup

RUN mkdir /home/runner/exchange && \
    mkdir /home/runner/backup && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN restic init --repo /home/runner/backup

RUN python3 python_api.py -a http://api.exchangeratesapi.io/v1/latest -k c168447546cedb690c58f867c4dbc434
RUN sh restic.sh

#COPY restic.sh /bin/exchange/
#COPY root /var/spool/cron/crontabs/

#RUN chmod +x /bin/exchange/restic.sh
#CMD crond -l 2 -f