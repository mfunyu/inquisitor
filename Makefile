# ---------------------------------------------------------------------------- #
#                                    DEFINS                                    #
# ---------------------------------------------------------------------------- #

SERVER := server
CLIENT:= client

CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
RESET="\033[m"

# ---------------------------------------------------------------------------- #
#                                     RULES                                    #
# ---------------------------------------------------------------------------- #

all	:
	docker-compose up --build

clean	:
	docker-compose down

fclean	: clean
	-docker stop $(shell docker ps -qa) 2>/dev/null
	-docker rm $(shell docker ps -qa) 2>/dev/null
	-docker rmi -f $(shell docker images -qa) 2>/dev/null

server	:
	docker exec -it server /bin/bash

client	:
	docker exec -it client /bin/sh

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
