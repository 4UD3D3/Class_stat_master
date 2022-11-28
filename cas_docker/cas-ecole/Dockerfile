FROM apereo/cas:latest

ENV CN="localhost"
ENV DNAME="CN=$CN,O=Moodle,L=Perth,S=WA,C=AU"
ENV CERT_SUBJ_ALT_NAMES="ip:127.0.0.1"

COPY ./cas /etc/cas

ENTRYPOINT ["java", "-server", "-noverify", "-Xmx2048M", "-jar", "cas.war"]
