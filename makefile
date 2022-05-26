# win #
.SILENT:

# Run service apiGateway
b-gw:
	go build -o .\.bins\apiGateway\apiGateway.exe .\backend\cmd\apiGateway\apiGateway.go 

r-gw: b-gw
	.\.bins\apiGateway\apiGateway.exe

# Bot telegram
r-bot:
	python3 .\frontend\bot\bot.py -p envs\bot.env
