local_up:
	docker-compose -f docker-compose-local.yaml up --force-recreate --build --remove-orphans
.PHONY: local_up

local_down:
	docker-compose  -f docker-compose-local.yaml down
.PHONY: local_down

eventhub_up:
	docker-compose -f docker-compose-eventhub.yaml up --force-recreate --build --remove-orphans
.PHONY: eventhub_up

eventhub_down:
	docker-compose  -f docker-compose-eventhub.yaml down
.PHONY: eventhub_down
