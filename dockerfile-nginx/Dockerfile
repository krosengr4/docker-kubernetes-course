# Defining the base image
FROM nginx:1.27.0

# Install vim dependency we want to use from within the container
RUN apt-get update
# The command below will need the user to confirm (not good for automation), to solve this we add the -y in the command to confirm automatically
RUN apt-get -y install vim

# /usr/share/nginx/html/index.html
# How we copy the index.html file. COPY takes a source(index.html) and a destination(/usr/share/nginx/html/index.html)
COPY index.html /usr/share/nginx/html/index.html
# Here we are changing the ownership (chown = change ownership) of the file to match the nginx user
RUN chown nginx:nginx /usr/share/nginx/html/index.html