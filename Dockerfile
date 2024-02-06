FROM prefecthq/prefect:2.12-python3.11

COPY requirements.txt .
RUN pip install -r requirements.txt --trusted-host pypi.python.org --no-cache-dir
RUN mkdir -p /src
COPY . /src

ENTRYPOINT ["/opt/prefect/entrypoint.sh", "prefect", "server", "start"]
