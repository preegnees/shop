# win
.SILENT:

b-gw:
	go build -o .\.bins\shop\apiGateway\apiGateway.exe .\cmd\shop\apiGateway\apiGateway.go  

r-gw: b-gw
	.\.bins\shop\apiGateway\apiGateway.exe