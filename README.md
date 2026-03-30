Docker --> container
helps us isolate the software from the hostmachine 
For example the host has ubuntu 24.48 but our requirement is 24.40 so we can add to docker and it is local to our container

docker run -it ubuntu --> so now we are inside the snapshot of the container and we can install whatever we want without affecting the host machine
