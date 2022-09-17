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
	docker container rm object-detection-web-app-frontend-1
	docker container rm object-detection-web-app-backend-1
	docker image rm object-detection-web-app-frontend
	docker image rm object-detection-web-app-backend