
<p align="center">
	<img src="https://cdn.iconscout.com/icon/free/png-256/free-nginx-logo-icon-svg-download-png-3030173.png"></img>
</p>

# Demo Nginx
> Repositório demo para configuração e utilização do Nginx como:

- 🌐 HTTP Web Server  
- 🔁 Reverse Proxy  
- ⚖️ Load Balancer  
- 📧 Mail Proxy Server  

## 📖 Sobre o Nginx

Segundo o site oficial:

> “nginx ("engine x") is an HTTP web server, reverse proxy, content cache, load balancer, TCP/UDP proxy server, and mail proxy server”

Ou seja, o Nginx é um servidor extremamente versátil que pode atuar tanto servindo aplicações web quanto intermediando comunicação entre serviços.

---

# 1. Instalação Nginx

## 📦 Ubuntu / Debian
```bash
sudo apt update
sudo apt install nginx
```

---

# 2. Arquivos de Configuração

Arquivo principal:
```
nginx.conf
```

Possíveis caminhos:
- `/etc/nginx/nginx.conf`
- `/usr/local/nginx/conf/nginx.conf`
- `/usr/local/etc/nginx/nginx.conf`

---

# 3. Logs

Diretório padrão:
```
/var/log/nginx/
```

Arquivos principais:

- `access.log` → Registra todas as requisições recebidas
- `error.log` → Registra erros, falhas e diagnósticos

## 📜 Acessando logs
```bash
tail -f /var/log/nginx/acess.log
tail -f /var/log/nginx/error.log
```
---

# 🧪 Como Testar

## ⚙️ Instale as dependências
```bash
# uv
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# swaks (tool for SMTP testing)
sudo apt install swaks
```

## ▶️ Execute 
```bash
chmod +x ./demo
echo "Usage: ./demo {start|test|reload|stop} {web|mail|load}"
```

### Testando o Web Server
```bash
./demo start web
# open the broser on: http://localhost:8080
```

### Testando o Mail Server
```bash
make auth_server

# em outro terminal
make mail_server

# mais outro terminal
make mail
```
