FROM python:3.8.13

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# copying all files over
COPY . /app

# Expose port 
ENV PORT 80
EXPOSE 80
# cmd to launch app when container is run
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]

# streamlit-specific commands for config
# ENV LC_ALL=C.UTF-8
# ENV LANG=C.UTF-8
# RUN mkdir -p /root/.streamlit
# RUN bash -c 'echo -e "\
# [general]\n\
# email = \"\"\n\
# " > /root/.streamlit/credentials.toml'

# RUN bash -c 'echo -e "\
# [server]\n\
# enableCORS = false\n\
# " > /root/.streamlit/config.toml'