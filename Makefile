local_up:
	docker-compose up -f docker-compose-local.yaml --force-recreate --build --remove-orphans
.PHONY: compose_up

local_down:
	docker-compose  -f docker-compose-local.yaml down
.PHONY: compose_down
