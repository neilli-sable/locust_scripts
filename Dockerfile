FROM locustio/locust
LABEL maintainer=neilli-sable

COPY ./scripts/ /scripts/

EXPOSE 8089
EXPOSE 5557
EXPOSE 5558
