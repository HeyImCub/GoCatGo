import os
import sys

print('Formatter')
if(len(sys.argv) < 2):
    print("Missing input file")
    print("python ./formatter.py inputFile dockerImgName binaryOutput tcpServPort")
    exit(1)

startBinary = sys.argv[1]

if not os.path.isfile(startBinary):
    print("Please enter a valid file path")
    print("python ./formatter.py inputFile dockerImgName binaryOutput tcpServPort")
    exit(1)

if(len(sys.argv) < 5):
    print("Missing Arguments")
    print("python ./formatter.py inputFile dockerImgName binaryOutput tcpServPort")
    exit(1)

print(f'Building Docker Image: {sys.argv[2]}')
os.system(f'docker build -t {sys.argv[2]} ./')

print(f'Running Docker image: {sys.argv[2]} to make new Binary: {sys.argv[3]} with inputFile {sys.argv[1]} combined')

files = ["go.mod","bin","dockerfile","formatter.py","go.sum","main.go","program.sh","readme.md"]
for a in files:
    if a in sys.argv[1]:
        print("Please use an input file thats not part of the program because it can be deleted")
        exit(0)
os.system(f'mv {sys.argv[1]} ./inputBinary' )


print(f'with nyancat running on tcp server on port:{sys.argv[4]}')
os.system(f'docker run -v ./:/app {sys.argv[2]} {sys.argv[3]} {sys.argv[4]}')