import select, sys, socket, datetime

# define a socket, set to a non-blocking one
svr_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_sock.setblocking(0)
svr_sock.bind(('localhost', 10000))
svr_sock.listen(5)

inputs = [svr_sock]
outputs = []

while True:
	# tigger for in/out/error events.
	in_queue, out_queue, err_queue = select.select(inputs, outputs, inputs)

	for i in in_queue:
		if i is svr_sock:
			# in case connection created
			clt_sock, clt_addr = svr_sock.accept()
			clt_sock.setblocking(0)
			print "connection established from %s:%i" % clt_addr
			inputs.append(clt_sock)
			outputs.append(clt_sock)
	for i in out_queue:
		data = str(datetime.datetime.now())
		i.send(data)
		if i in outputs: outputs.remove(i)
		if i in inputs: inputs.remove(i)
		i.close()







