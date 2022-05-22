package entities

type Action struct {
	Action   string `json:"action"`
}
type Post struct {
	Id       string `json:"id"`
	Title    string `json:"title"`
	Category string `json:"category"`
	Content  string `json:"content"`
}

type CRUD struct {
	Post
	Action
}

type Posts struct {
	Posts []Post
}
