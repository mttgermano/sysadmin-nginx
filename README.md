
<p align="center">
	<img src="https://cdn.iconscout.com/icon/free/png-256/free-nginx-logo-icon-svg-download-png-3030173.png"></img>
</p>

# Demo Nginx
> Repositório demo para configuração e utilização do Nginx como:

- 🌐 HTTP Web Server  
- 🔁 Reverse Proxy  
- ⚖️ Load Balancer  
- 📧 Mail Proxy Server  

---

## 📖 Sobre o Nginx

Segundo o site oficial:

> “nginx ("engine x") is an HTTP web server, reverse proxy, content cache, load balancer, TCP/UDP proxy server, and mail proxy server”

Ou seja, o Nginx é um servidor extremamente versátil que pode atuar tanto servindo aplicações web quanto intermediando comunicação entre serviços.

---

# ⚙️ Instalação

## 📦 Ubuntu / Debian
```bash
sudo apt update
sudo apt install nginx
```

## 🔎 Verificar status
```bash
sudo systemctl status nginx
```

## ▶️ Iniciar serviço
```bash
sudo systemctl start nginx
```

## 🔥 Liberar no firewall
```bash
sudo ufw allow 'Nginx HTTP'
```

---

# 🛠️ Gerenciamento do Serviço

Via systemctl:
```bash
sudo systemctl start nginx
sudo systemctl reload nginx
sudo systemctl stop nginx
```

Via comando nginx:
```bash
nginx -s stop     # fast shutdown
nginx -s quit     # graceful shutdown
nginx -s reload   # reload configuração
nginx -s reopen   # reopen logs
```

---

# 📂 Arquivos de Configuração

Arquivo principal:
```
nginx.conf
```

Possíveis caminhos:
- `/etc/nginx/nginx.conf`
- `/usr/local/nginx/conf/nginx.conf`
- `/usr/local/etc/nginx/nginx.conf`

---

# 📜 Logs

Diretório padrão:
```
/var/log/nginx/
```

Arquivos principais:

- `access.log` → Registra todas as requisições recebidas
- `error.log` → Registra erros, falhas e diagnósticos


# 🧪 Como Testar

```bash
chmod +x ./demo
echo "Usage: ./demo {start|test|reload|stop} {web|mail|load}"
./demo start web
```

Acesse no navegador:
```
http://localhost
```
