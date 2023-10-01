# question-answering

## :gear: Setup
 Installing Elasticsearch on EC2 Instance: https://www.youtube.com/watch?v=adyA6bTk_ig

 For hte installation of java:
 - sudo yum install nginx
 - sudo dnf update
 - sudo dnf install java-1.8.0-amazon-corretto
 - sudo dnf install java-1.8.0-amazon-corretto-devel

Install Elasticsearch with RPM: 
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.17.13-x86_64.rpm
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.17.13-x86_64.rpm.sha512
shasum -a 512 -c elasticsearch-7.17.13-x86_64.rpm.sha512 
sudo rpm --install elasticsearch-7.17.13-x86_64.rpm

sudo nano /etc/elasticsearch/elasticsearch.yml

uncomment the following lines:
- cluster.name: my-application
- node.name: node-1
- network.host: 192.168.0.1 (and change it to network.host: 0.0.0.0)
- http.port: 9200
- discovery.seed_hosts: ["host1", "host2"] (and change it to discovery.seed_hosts: ["your Private IPv4 addresses of your ec2 instance"])
