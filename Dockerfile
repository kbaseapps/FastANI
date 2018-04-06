FROM kbase/kbase:sdkbase2.latest
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

# We require R and genPlotR to generate FastANIs visualization
# Leaving this out for now as it only works for FastANI 1:1
RUN apt-get update && apt-get install -y r-base
RUN Rscript -e "install.packages('genoPlotR', repos='http://cran.us.r-project.org')"

# Fetch and compile FastANI
RUN git clone https://github.com/ParBLiSS/FastANI.git /opt/FastANI && \
    cd /opt/FastANI && \
    git checkout tags/v1.0 -b v1.0 && \
    ./bootstrap.sh && \
    ./configure && \
    make && \
    # Place fastANI in the PATH for this user
    ln -s $(readlink -f ./fastANI) /usr/local/bin/fastANI && \
    # Copy some sample data to an absolute path for easy testing
    cp -r data/ /tmp/fastANI-data

# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
