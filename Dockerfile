FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive

# Update aptitude with new repo
RUN apt-get update
RUN apt-get install -y git cmake ninja-build clang-8 clang++-8

# Clone the conf files into the docker container
RUN git clone --recursive  https://github.com/microsoft/verona.git
WORKDIR verona
RUN git fetch origin pull/528/head:acquire-all
RUN git checkout acquire-all

RUN mkdir build-acquire-one build-acquire-all
WORKDIR build-acquire-one
RUN cmake ../ -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=clang++-8 -DCMAKE_C_COMPILER=clang-8 -DCMAKE_INSTALL_PREFIX=dist
RUN ninja

WORKDIR ../build-acquire-all
RUN cmake ../ -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=clang++-8 -DCMAKE_C_COMPILER=clang-8 -DCMAKE_INSTALL_PREFIX=dist -DACQUIRE_ALL=On
RUN ninja

WORKDIR ../../
COPY throughput-test.verona .
COPY runtest.py .
COPY transform.py .
COPY plot.py .

CMD python3 runtest.py --all=verona/build-acquire-all/dist/veronac --one=verona/build-acquire-one/dist/veronac --repeat=100 && \
    python3 transform.py && \
    cat log.csv