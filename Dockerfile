FROM kbase/kbase:sdkbase2.latest
MAINTAINER Jay R Bolton <jrbolton@lbl.gov>

# -----------------------------------------
# App-specific dependencies

RUN apt-get update

# Fetch and compile FastANI
RUN git clone https://github.com/ParBLiSS/FastANI.git /opt/FastANI \
    && cd /opt/FastANI \
    && git checkout tags/v1.0 -b v1.0 \
    && ./bootstrap.sh \
    && ./configure \
    && make \
    # Place fastANI in the PATH for this user
    && ln -s $(readlink -f ./fastANI) /usr/local/bin/fastANI

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
