# Usar a imagem mais recente do docker hub: https://hub.docker.com/r/bitnami/postgresql/tags
FROM bitnami/postgresql

# Define variáveis de ambiente para configurar o PostgreSQL
ENV POSTGRES_USER=openweather
ENV POSTGRES_PASSWORD=verificarclimas
ENV POSTGRES_DB=portugal_weather

# Cria um diretório para scripts de inicialização SQL (opcional)
# Esse script pode ser usado para carregar dados iniciais ou criar tabelas automaticamente
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expor a porta padrão do PostgreSQL
EXPOSE 5432
