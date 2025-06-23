# Usa Python 3.10.11 baseado no Debian Bullseye (leve)
FROM python:3.10.11

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Instala dependências do sistema e Python
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o código-fonte e o entrypoint
COPY . /app/
COPY entrypoint.sh /app/entrypoint.sh

# Permissão de execução
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

# Usa o entrypoint personalizado
ENTRYPOINT ["/app/entrypoint.sh"]
