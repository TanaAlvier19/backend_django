# Usa Python 3.10.11 baseado no Debian Bullseye (leve)
FROM python:3.10.11

# Define o diretório principal do projeto
WORKDIR /app

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Instala pacotes do sistema necessários para compilar dlib
# Instala dependências Python
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o restante do código para o container
COPY . /app/

# Coleta arquivos estáticos e aplica migrações

# Expõe a porta usada pelo Gunicorn (Render espera 8000)
EXPOSE 8000

# Comando de inicialização do servidor (substitui o ENTRYPOINT)
CMD sh -c "gunicorn recursos.wsgi:application --bind 0.0.0.0:${PORT:-8000}"

