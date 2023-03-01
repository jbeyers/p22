# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6.0.1
FROM plone/plone-backend:${PLONE_VERSION}

LABEL maintainer="Juizi CC <johan@juizi.com>" \
      org.label-schema.name="p22-backend" \
      org.label-schema.description="p22 backend image." \
      org.label-schema.vendor="Juizi CC"

# Add local code
COPY . .

# Install local requirements and fix permissions
RUN <<EOT
    ./bin/pip install mxdev
    mv requirements-docker.txt requirements.txt
    ./bin/mxdev -c mx.ini
    ./bin/pip install -r requirements-mxdev.txt
    chown -R plone: /app
EOT
