local_up:
	docker-compose -f docker-compose-local.yaml up --force-recreate --build --remove-orphans
.PHONY: compose_up

local_down:
	docker-compose  -f docker-compose-local.yaml down
.PHONY: compose_down

eventhub_up:
	docker-compose -f docker-compose-eventhub.yaml up --force-recreate --build --remove-orphans
.PHONY: compose_up

eventhub_down:
	docker-compose  -f docker-compose-eventhub.yaml down
.PHONY: compose_down
