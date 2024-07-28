# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Juizi CC <johan@juizi.com>" \
      org.label-schema.name="p22-varnish" \
      org.label-schema.description="P22 Varnish image." \
      org.label-schema.vendor="Juizi CC"

COPY etc/varnish.vcl /etc/varnish/default.vcl
