Always port number should be 5000 above
passing database information dynamically:

sudo docker build -t rajflk .

sudo docker run -dit -p  5000:5000 -e DATABASE_URL=securlystoredindaillynotes rajeshsingam/prod-working-flask:latest

Amazon linux docker install:
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo chkconfig docker on
sudo docker --version
sudo usermod -aG docker ec2-user.


Database schemas:
In render always take full url
like hostname@render.com
Ex: krb2pg5vl2c73bqmhgg-a.oregon-postgres.render.com

Creating table and getting all table names:
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL
);


//Getting all table names query
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'



rajeshsingam/prod-working-flask:tagname

docker tag rajflk:latest rajeshsingam/prod-working-flask:latest

docker push rajeshsingam/prod-working-flask:latest
docker pull rajeshsingam/prod-working-flask:latest
