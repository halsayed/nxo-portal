FROM alpine:latest
# --virtual .build-deps
RUN apk add --no-cache \
			ca-certificates \
			python3 \
			mariadb-client \
			build-base \
			python3-dev \
			mariadb-dev \
			&& ln -s /usr/bin/python3 /usr/local/bin/python \
			&& ln -s /usr/bin/pip3 /usr/local/bin/pip \
			&& rm -rf /var/cache/apk/*
RUN pip install --no-cache-dir django \
				mysqlclient \
				pyvmomi \
				django-tables2