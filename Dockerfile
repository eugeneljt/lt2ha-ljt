FROM ghcr.io/home-assistant/base:latest

WORKDIR /app

RUN \
  apk add --no-cache \
    python3 \
    py3-pip

COPY ./pyproject.toml ./
RUN pip3 install -e . --break-system-packages --no-cache-dir
COPY ./src/ ./
COPY --chmod=755 ./run.sh /

CMD ["/run.sh"]
