Always port number should be 5000 above
passing database information dynamically:

sudo docker build -t rajflk .
sudo docker run -dit -p  5000:5000 -e DATABASE_URL=postgres://raj:UPL64CjBLgQd4Sc5VlvRNcE4268zPjNg@dpg-ckrb2pg5vl2c73bqmhgg-a.oregon-postgres.render.com/raj  rajflk

Amazon linux docker install:
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo chkconfig docker on
sudo docker --version
sudo usermod -aG docker ec2-user.




