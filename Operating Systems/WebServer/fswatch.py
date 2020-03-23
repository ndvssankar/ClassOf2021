from fswatch import Monitor

monitor = Monitor()
monitor.add_path("/Sankar/2021/ClassOf2021/Operating Systems/WebServer")

def callback(path, evt_time, flags, flags_num, event_num):
    print(path.decode())

monitor.set_callback(callback)

monitor.start()