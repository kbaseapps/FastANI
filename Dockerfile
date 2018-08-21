FROM kbase/kbase:sdkbase2.latest
MAINTAINER Jay R Bolton <jrbolton@lbl.gov>

# -----------------------------------------
# App-specific dependencies

RUN apt-get update

ENV FASTANI_URL="https://github.com/ParBLiSS/FastANI/releases/download/v1.1/fastani-Linux64-v1.1.zip"

# Fetch and compile FastANI
RUN curl $FASTANI_URL -L --output /opt/fastani.zip && \
    unzip /opt/fastani.zip -d /opt && \
    rm /opt/fastani.zip && \
    ln -s /opt/fastANI /usr/local/bin/fastANI

# R and genoPlotR are required for fastANI visualization
RUN apt-get install -y r-base \
    && Rscript -e "install.packages('genoPlotR', repos='http://cran.us.r-project.org')"

# Update security deps
RUN pip install -U pip
RUN pip install --upgrade \
    cffi pyopenssl ndg-httpsclient pyasn1 requests 'requests[security]'

# Install pip deps
COPY requirements.txt /kb/module/requirements.txt
WORKDIR /kb/module
RUN pip install -r requirements.txt

# End app-specific dependencies
# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module
RUN make all
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
CMD [ ]
