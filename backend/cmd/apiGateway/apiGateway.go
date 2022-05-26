package main

import (
	"log"

	s "rest_api/backend/pkg/apiGateway/server"
	h "rest_api/backend/pkg/apiGateway/handler"
)

func main() {
	handler := new(h.Handler)
	server := new(s.Server)
	if err := server.RunServer("8080", handler.InitRoutes()); err != nil { // get from env
		log.Fatalf("Ошибка при запуска сервера: %v\n", err.Error())
	}
}
