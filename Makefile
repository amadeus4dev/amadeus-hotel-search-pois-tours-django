PORTS = -p 8000:8000
ENV = \
  -e AMADEUS_CLIENT_ID=${AMADEUS_CLIENT_ID} \
  -e AMADEUS_CLIENT_SECRET=${AMADEUS_CLIENT_SECRET} \
  -e HERE_API_KEY=${HERE_API_KEY} \
  -e AMADEUS_HOSTNAME=${AMADEUS_HOSTNAME} \
  -e DEBUG_VALUE=${DEBUG_VALUE}

NS ?= amadeus4dev
VERSION ?= latest

IMAGE_NAME ?= hotel-search-demo
CONTAINER_NAME ?= hotel-search-demo
CONTAINER_INSTANCE ?= default

build: Dockerfile
	docker build -t $(NS)/$(IMAGE_NAME):$(VERSION) -f Dockerfile .

run:
	docker run --rm -i -t --name $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) \
		$(PORTS) \
		$(ENV) \
		$(NS)/$(IMAGE_NAME):$(VERSION)

start:
	docker run -d --name $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) \
		$(PORTS) \
		$(ENV) \
		$(NS)/$(IMAGE_NAME):$(VERSION)

stop:
	docker stop $(CONTAINER_NAME)-$(CONTAINER_INSTANCE)

rm:
	docker rm $(CONTAINER_NAME)-$(CONTAINER_INSTANCE)

default: build

.PHONY: build run start stop rm
