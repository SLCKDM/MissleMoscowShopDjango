dcu:
	docker network rm has-internet no-internet -f
	docker network create has-internet
	docker network create no-internet
	docker compose up --build -d

# test 2