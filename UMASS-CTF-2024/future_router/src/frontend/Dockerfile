FROM nginx:stable-alpine-slim
COPY nginxproxy.conf /etc/nginx/nginxproxy.conf
EXPOSE 80
CMD ["nginx","-c","nginxproxy.conf", "-g", "daemon off;"]