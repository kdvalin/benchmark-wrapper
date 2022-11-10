FROM registry.access.redhat.com/ubi8:latest
COPY snafu/image_resources/centos8.repo /etc/yum.repos.d/centos8.repo

RUN dnf install --enablerepo=centos8 -y git make libtirpc-devel net-tools gcc

WORKDIR /opt

RUN git clone https://github.com/intel/lmbench.git

WORKDIR /opt/lmbench

RUN ln -s /usr/include/tirpc/rpc/* /usr/include/rpc/
RUN ln -s /usr/include/tirpc/netconfig.h /usr/include/

RUN make LDFLAGS=-ltirpc