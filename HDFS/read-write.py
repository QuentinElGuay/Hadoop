import hdfs
client = hdfs.InsecureClient('http://localhost:9870/', user='quentin-Ubuntu')
client.list("/")



