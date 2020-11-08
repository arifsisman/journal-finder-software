FROM aucse/journal-finder-base:latest

WORKDIR /root/journal-finder
COPY src src
WORKDIR /root/journal-finder/src

ENTRYPOINT ["python", "main.py"]
