def get_block_distance(speed, run_time, rest_time, total_time):
    block_distance = int(total_time / (run_time + rest_time)) * run_time * speed
    return int(total_time / (run_time + rest_time)) * run_time * speed

def get_extra_distance(speed, run_time, rest_time, total_time):
    extra_time = total_time % (run_time + rest_time)
    return min(run_time, extra_time) * speed

def get_distance(speed, run_time, rest_time, total_time):
    return get_block_distance(speed, run_time, rest_time, total_time) + get_extra_distance(speed, run_time,rest_time, total_time)

def process_line(line):
    words = line.split(" ")
    data =  {"name": words[0], "speed" : int(words[3]), "run_time" : int(words[6]), "rest_time" : int(words[13])}
    return {"name" : data["name"], "distance" : get_distance(data["speed"], data["run_time"], data["rest_time"], 2503)}

f = open('input.txt','r')
for line in f:
    print(process_line(line))
