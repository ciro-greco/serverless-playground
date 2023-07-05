# Use the official Python base image
FROM public.ecr.aws/lambda/python:3.9

# Install pip and other dependencies
RUN pip3 install --upgrade pip \
    && pip3 install boto3==1.26.3 python-decouple==3.8


COPY handler.py .

# Set the CMD to the lambda handler
CMD [ "handler.lambda_handler" ]