package handler

import (
	"github.com/gin-gonic/gin"
)

type Handler struct {}

func (h *Handler) InitRoutes() *gin.Engine {
	router := gin.New()

	auth := router.Group("/auth")
	{
		auth.POST("sign-up", h.signUp)
		auth.POST("sign-in", h.signIn)
	}

	api := router.Group("/api")
	{
		posts := api.Group("/posts")
		{
			posts.GET("/", h.getAllPosts)
			posts.GET("/:id", h.getPostById)
			posts.POST("/:id", h.updatePostById)
		}
	}
	return router
}