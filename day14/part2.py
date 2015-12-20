
def get_block_distance(speed, run_time, rest_time, total_time):
    block_distance = int(total_time / (run_time + rest_time)) * run_time * speed
    return int(total_time / (run_time + rest_time)) * run_time * speed

def get_extra_distance(speed, run_time, rest_time, total_time):
    extra_time = total_time % (run_time + rest_time)
    return min(run_time, extra_time) * speed

def get_distance(speed, run_time, rest_time, total_time):
    return get_block_distance(speed, run_time, rest_time, total_time) + get_extra_distance(speed, run_time,rest_time, total_time)

def process_line(line, time):
    words = line.split(" ")
    data =  {"name": words[0], "speed" : int(words[3]), "run_time" : int(words[6]), "rest_time" : int(words[13])}

    return {"name" : data["name"], "distance" : get_distance(data["speed"], data["run_time"], data["rest_time"], time)}

def init_winners(filename):
    winners = []
    f = open(filename,'r')
    for line in f:
        words = line.split(" ")
        winners.append({"name": words[0], "points" : 0 })

    return winners

winners = init_winners('input.txt')
#print (winners)

for time in range(1, 2504):
    race_data = []
    f = open('input.txt','r')
    for line in f:
        race_data.append(process_line(line,time))

    #print(race_data)
    winning_distance = max(x["distance"] for x in race_data)
    #print(winning_distance)
    leaders = [l["name"] for l in race_data if l["distance"] == winning_distance]
    for leader in leaders:
        winner = next((w for w in winners if w["name"]== leader),None)
        winner["points"] +=1
        #leader["points"] += 1
    #winner = max(race_data, key=lambda x:x["distance"])["name"]

    #atob = next((x for x in winners if x["name"] == winner), None)
    #print(atob)
    #print(atob["points"])
    #atob["points"] += 1
    #print(atob)
    #print next((x for x in winners if x["name"]==winner),None)
    #winners[winner]["points"] += 1

print(winners)
