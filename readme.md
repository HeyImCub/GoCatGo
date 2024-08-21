# GoCatGo
### !Not Good Code Warning!
Takes a binary and adds a nyancat ssh 
Thanks to https://github.com/travisjeffery/nyancat/

Uses golang embed to combine a nyancat tcp server with any binary
Made quickly and there's probably way better examples of golang:embed and better ways to achive this goal

Steps:
* IF NOT USING `formatter.py`
    * inputBinary has to be named inputBinary
    * Build the image with a custom name
    `docker build -t custom-name ./`

    * Run the image to create the new binary with nyancat tcp added to it
    * Change the values: 
        * customName - image name
        * output - filename of output binary
        * 1337 - port of tcp server
    `docker run -v ./:/app custom-name output 1337`

* Using `formatter.py`
    * `python ./formatter.py inputFile dockerImgName binaryOutput tcpServPort`

* Both methods should put the binary in the bin folder
* arguments will pass to the original binary
Notes:
* Once the image is built it is custom for each input binary :)
