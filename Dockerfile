FROM kbase/kbase:sdkbase2.latest
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

# RUN apt-get update


# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

# Fetch and compile FastANI

RUN mkdir -p bin && \
    git clone https://github.com/ParBLiSS/FastANI.git bin/FastANI && \
    cd bin/FastANI && \
    git checkout tags/v1.0 -b v1.0 && \
    ./bootstrap.sh && \
    ./configure && \
    make

CMD [ ]
