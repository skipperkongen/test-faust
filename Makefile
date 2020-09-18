compose_up:
	docker-compose up --force-recreate --build --remove-orphans
.PHONY: compose_up

compose_down:
	docker-compose down
.PHONY: compose_down
