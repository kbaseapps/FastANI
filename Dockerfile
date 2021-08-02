FROM kbase/sdkbase2:python

# -----------------------------------------
# App-specific dependencies

# Install pip deps
COPY requirements.txt /kb/module/requirements.txt
ENV FASTANI_URL="https://github.com/ParBLiSS/FastANI/releases/download/v1.33/fastANI-Linux64-v1.33.zip"

RUN apt-get update && \
    # Fetch and compile FastANI
    curl $FASTANI_URL -L --output /opt/fastani.zip && \
    unzip /opt/fastani.zip -d /opt && \
    rm /opt/fastani.zip && \
    ln -s /opt/fastANI /usr/local/bin/fastANI && \
    # R and genoPlotR are required for fastANI visualization
    apt-get install -y r-base \
    && Rscript -e "install.packages('genoPlotR', repos='http://cran.us.r-project.org')" && \
    pip install -U pip && \
    cd /kb/module && \
    pip install -r requirements.txt

# End app-specific dependencies
# -----------------------------------------

COPY ./ /kb/module
WORKDIR /kb/module
RUN mkdir -p /kb/module/work && \
    chmod -R a+rw /kb/module && \
    chmod +x /kb/module/scripts/entrypoint.sh && \
    make all
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
CMD [ ]
