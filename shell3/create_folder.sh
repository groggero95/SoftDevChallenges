rm -rf dirA
rm -rf dirB

touch -a -t 201701181205.09 file1
mkdir ./dirA
mkdir ./dirA/dirC
touch -a -t 201701181205.09  ./dirA/dirC/file4
touch -a -t 201701181205.09  ./dirA/dirC/file5
mkdir  ./dirA/dirC/dirD
touch -a -t 201701181205.09 ./dirA/dirC/dirD/file8
touch -a -t 201811181205.09 ./dirA/dirC/dirD/file6
touch -a -t 201701181205.09 ./dirA/dirC/dirD/file7
mkdir ./dirA/dirE
touch -a -t 201701181205.09 ./dirA/dirE/file9
touch -a -t 201701181205.09 ./dirA/file2
touch -a -t 201701181205.09 ./dirA/file3
mkdir ./dirB
touch -a -t 201811181205.09 ./dirB/file10
mkdir  ./dirB/dirF
touch -a -t 201701181205.09 ./dirB/dirF/file11
touch -a -t 201701181205.09 ./dirB/dirF/file12
mkdir  ./dirB/dirF/dirG
touch -a -t 201701181205.09 ./dirB/dirF/dirG/file13

