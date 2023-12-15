# ---------------------------------------------------------------------------- #
#                                    DEFINS                                    #
# ---------------------------------------------------------------------------- #
NAME	:= inquisitor.py
TARGET	:= inquisitor

SERVER	:= server
CLIENT	:= client

CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
RESET="\033[m"

# ---------------------------------------------------------------------------- #
#                                     RULES                                    #
# ---------------------------------------------------------------------------- #

.PHONY: all
all	:
	docker-compose up --build

.PHONY: clean
clean	:
	docker-compose down

.PHONY: prune
prune	: clean
	-docker system prune -f -a

.PHONY: fclean
fclean	: clean
	-docker stop $(shell docker ps -qa) 2>/dev/null
	-docker rm $(shell docker ps -qa) 2>/dev/null
	-docker rmi -f $(shell docker images -qa) 2>/dev/null
	-docker volume rm $(shell docker volume ls -q) 2>/dev/null
	-docker network rm $(shell docker network ls -q) 2>/dev/null

.PHONY: server
server	:
	docker exec -it server /bin/bash

.PHONY: client
client	:
	docker exec -it client /bin/sh

.PHONY: inquisitor
inquisitor	:
	docker exec -it inquisitor /bin/bash

.PHONY: info
info	:
	@printf "[docker informations]\n"

	@echo $(CYAN)$(SERVER)$(RESET)
	@printf " - IPAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(SERVER)
	@printf " - MacAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(SERVER)

	@echo $(CYAN)$(CLIENT)$(RESET)
	@printf " - IPAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(CLIENT)
	@printf " - MacAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(CLIENT)

	@echo $(CYAN)$(TARGET)$(RESET)
	@printf " - IPAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(TARGET)
	@printf " - MacAddress	: "
	@docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(TARGET)

.PHONY: perm
perm	:
	sudo groupadd -f docker
	sudo usermod -aG docker $(USER)
	newgrp docker

# ---------------------------------------------------------------------------- #
#                                     UTILS                                    #
# ---------------------------------------------------------------------------- #

IP_SV := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(SERVER))
MAC_SV := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(SERVER))
IP_CL := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(CLIENT))
MAC_CL := $(shell docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $(CLIENT))

.PHONY: run
run	:
	@echo "Execute: "
	@echo ./$(NAME) $(IP_SV) $(MAC_SV) $(IP_CL) $(MAC_CL)

.PHONY: cp
cp	:
	docker cp inquisitor.py inquisitor:/usr/src/app
