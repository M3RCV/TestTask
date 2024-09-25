start:
	docker-compose up -d --build --remove-orphans

up:
	docker-compose up -d

build:
	docker-compose build

logs:
	docker-compose logs -f

down:
	docker-compose down
