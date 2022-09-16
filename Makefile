build:
	docker-compose build

up:
	docker-compose up

restart:
	make build
	make up

down:
	docker-compose down

rm:
	docker container rm object-detection-web-app_frontend_1
	docker container rm object-detection-web-app_backend_1
	docker image rm object-detection-web-app_frontend
	docker image rm object-detection-web-app_backend