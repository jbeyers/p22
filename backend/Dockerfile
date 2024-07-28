# syntax=docker/dockerfile:1
ARG PLONE_VERSION
FROM plone/server-builder:${PLONE_VERSION:-6.0.11} as builder

WORKDIR /app

# Add local code
COPY . .

# Install local requirements and pre-compile mo files
RUN <<EOT
    set -e
    bin/pip install mxdev
    mv requirements-docker.txt requirements.txt
    sed -i 's/-e src\/p22\[test\]/src\/p22/g' mx.ini
    bin/mxdev -c mx.ini
    bin/pip install -r requirements-mxdev.txt
    bin/python /compile_mo.py
    rm -Rf src/
EOT

FROM plone/server-prod-config:${PLONE_VERSION:-6.0.11}

LABEL maintainer="Juizi CC <johan@juizi.com>" \
      org.label-schema.name="p22-backend" \
      org.label-schema.description="P22 backend image." \
      org.label-schema.vendor="Juizi CC"

# Copy /app from builder
COPY --from=builder /app /app

RUN <<EOT
    set -e
    ln -s /data /app/var
EOT
