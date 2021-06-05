# Exchange-currency-API 💰
Code regularly (e.g. every 3 hours) downloads the EURO exchange rate for a few selected currencies (max 5) provided by the API 

Aby uruchomić rozwiązanie powinno Państwo posiadać plikami: Dockerfile 🐳, root(plik do działania CRON) i skryptem on nazwie restic.sh - dla rozpoczęcia backupów.

Krótki opis działania: Python skrypt przez zewnętrzne API co 3 godziny pobiera kurs waluty EURO na 5 walut. Przy budowanie kontenera Docker Dockerfile 🐳 za pomocą plika root buduje zdefiniowany CRON. Zapisane pliki .csv są backupowe z użyciem klienta restic, który buduje się przez skrypt restic.sh

Sposób uruchomienia rozwiązania:
1) Zbudować obraz Docker za pomocą polecenia '🐳 docker image build'. (Wszystkie pliki muszą znajdować się w tym samym katalogu co plik Dockerfile 🐳)

2)Uruchomić kontener dockera za pomocą polecenia '🐳 docker container run -dt --name "nazwa kontenera" "nazwa obrazu"'.

Przydatne linki:

GitHub: https://github.com/vv173/Exchange-currency-API.git

DockerHub: https://hub.docker.com/r/v17v3/apicronbackup/tags 🐳