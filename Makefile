mail_server:
	uv run -- aiosmtpd -n -l localhost:2525

auth_server:
	uv run auth_server.py

mail:
	swaks --to test@example.com \
		--from sender@example.com \
		--server localhost       \
		--port 25       \
		--auth LOGIN       \
		--auth-user test       \
		--auth-password password

.PHONY: mail_server mail auth_server
