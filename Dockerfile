FROM python:3.11.0a3-alpine3.15

# install cap package and set the capabilities on busybox
RUN apk update && \
    apk add restic && \
    apk add --update --no-cache libcap && \
    setcap cap_setgid=ep /bin/busybox && \
    pip install --upgrade pip

RUN adduser -D runner
USER runner
WORKDIR /home/runner

COPY --chown=runner:runner requirements.txt .
COPY --chown=runner:runner python_api.py .
COPY --chown=runner:runner restic.sh .

RUN chmod +x ./python_api.py && \
    chmod +x ./restic.sh

RUN mkdir /tmp/crontabs
COPY runner /tmp/crontabs/runner

ENV RESTIC_PASSWORD="VVdtsc4v5QtUCNXA"
ENV RESTIC_REPOSITORY=/home/runner/backup

RUN mkdir /home/runner/exchange && \
    mkdir /home/runner/backup && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN restic init --repo /home/runner/backup

CMD ["crond", "-c", "/tmp/crontabs", "-l", "2", "-f"]