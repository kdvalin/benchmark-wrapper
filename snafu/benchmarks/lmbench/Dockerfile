FROM registry.access.redhat.com/ubi8:latest
COPY snafu/image_resources/centos8.repo /etc/yum.repos.d/centos8.repo

RUN dnf install --enablerepo=centos8 -y git make libtirpc-devel net-tools gcc

RUN git clone https://github.com/intel/lmbench.git /opt/lmbench

WORKDIR /opt/lmbench

RUN ln -s /usr/include/tirpc/rpc/* /usr/include/rpc/
RUN ln -s /usr/include/tirpc/netconfig.h /usr/include/

RUN make LDFLAGS=-ltirpc

RUN mv bin/*/* bin/

WORKDIR /opt/lmbench/bin

RUN dnf install -y --nodocs python3.8 python38-devel procps-ng iproute net-tools ethtool nmap iputils && dnf clean all
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip3 install --upgrade pip
COPY . /opt/snafu
RUN pip3 install -r /opt/snafu/requirements/py38-reqs/install.txt -e /opt/snafu
