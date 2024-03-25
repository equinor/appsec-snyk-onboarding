FROM nginxinc/nginx-unprivileged:1.25-alpine
COPY index.html /usr/share/nginx/html/index.html
COPY content /usr/share/nginx/html/content
COPY nginx/nginx.conf /etc/nginx/
