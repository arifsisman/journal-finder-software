DIR := ${CURDIR}

ifndef TAG
override TAG = latest
endif

################################
# Building Images
################################
# Build Application Base Docker Image
buildbase:
	@echo Start Building App Base Image\n
	docker build -f Dockerfile.base -t aucse/journal-finder-base:$(TAG) .

# Build Application Docker Image
build:
	@echo Start Building App Base Image\n
	docker build -f Dockerfile -t aucse/journal-finder:$(TAG) .

################################
# Running Container
################################
# To run app temprarily
run: build
	docker run -p 5000:5000 -it --rm aucse/journal-finder:$(TAG)

db:
	docker run --name mssql -d -p 1433:1433 -it --rm aucse/journaldb:$(TAG)

deploy:
	docker run --name journal-mssql -d -p 1433:1433 aucse/journaldb:$(TAG)
	docker run --name journal-finder -p 5000:5000 --link journal-mssql aucse/journal-finder:$(TAG)

push:
	docker push aucse/journaldb:$(TAG)
	docker push aucse/journal-finder-base:$(TAG)
	docker push aucse/journal-finder:$(TAG)
