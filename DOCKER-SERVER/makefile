.PHONY: clean build start stop

clean:
	sudo docker-compose down
	sudo docker image rm dockermshl/docker_test:server2
	sudo docker image rm dockermshl/docker_test:server1
	sudo docker image rm dockermshl/docker_test:balancer
	rm -f tmpfile.txt

stop:
	sudo docker-compose stop

build: tmpfile.txt
	sudo docker-compose build

start:
	sudo docker-compose up

tmpfile.txt:
	touch tmpfile.txt
