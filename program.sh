#!/bin/sh

# check if the arguemtns are there
if [ -z "$1" ]; then
    echo "Missing outputFile and Port"
    echo "Run a binary and also run a Nyancat tcp server in the same binary"
    echo "inputBinary cannot have ./ just use the filename and have it in the same dir"
    exit 1
elif [ -z "$2" ]; then
    echo "Missing port"
    exit 1
elif [ $# -gt 3 ]; then
    echo "More than 2 arguments were provided"
    exit 1
fi

sed -i "s|.*//go:embed.*|//go:embed inputBinary|" "./main.go"

sed -i "/var Port/c\var Port = \"$2\"" ./main.go

go build -o "bin/$1"