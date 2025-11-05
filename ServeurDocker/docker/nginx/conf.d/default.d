server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root   /var/www/php;
    index  index.html;

    location ~* \.php$ {
        fastcgi_pass   php:9000;
        include        fastcgi_params;
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param  SCRIPT_NAME     $fastcgi_script_name;
    }

}

server {
    listen 9114;
    server_name localhost;

    location /nginx_status {
        stub_status;
        allow all;
    }
}
