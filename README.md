"# django_first_proj" 
allow port 8000 on ec2
then build the image and rundocker build . -t django-dev:v0.1
docker run -p 8000:8000 -it --rm django-dev:v0.1
then open the public ip of the with http instead of https at port 8000
