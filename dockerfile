FROM golang:latest

WORKDIR /app

RUN go env -w GOFLAGS="-buildvcs=false"
ENTRYPOINT ["/app/program.sh"]

CMD ["default_arg1", "default_arg2"]

