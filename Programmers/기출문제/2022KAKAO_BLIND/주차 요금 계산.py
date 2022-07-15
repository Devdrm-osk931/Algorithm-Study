from math import ceil


def calculate_time(in_out_times):
    total_time = 0
    if len(in_out_times) % 2 != 0:
        in_out_times.append('23:59')

    for i in range(0, len(in_out_times), 2):
        in_hour, in_min = tuple(in_out_times[i].split(":"))
        out_hour, out_min = tuple(in_out_times[i + 1].split(":"))
        total_time += (int(out_hour) * 60 + int(out_min)) - (int(in_hour) * 60 + int(in_min))

    return total_time

def solution(fees, records):
    answer = []
    time_by_car = {}

    for record in records:
        in_out_time, car_num, _ = record.split(" ")
        if car_num not in time_by_car:
            time_by_car[car_num] = [in_out_time]
        else:
            time_by_car[car_num].append(in_out_time)

    for key in sorted(list(time_by_car.keys())):
        acc_time = calculate_time(time_by_car[key])
        if acc_time <= fees[0]:
            # 기본 시간보다 작거나 같은 경우는 기본 요금을 부과한다
            answer.append(fees[1])
        else:
            answer.append(int(fees[1] + ceil((acc_time - fees[0])/fees[2]) * fees[3]))

    return answer

# solution([180, 5000, 10, 600], 
#         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])


# solution([120, 0, 60, 591],
# ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])

solution([1, 461, 1, 10], ["00:00 1234 IN"])