from functools import reduce


def value_grabber(json_array):
    print(json_array)


def triangulater(pos_lat_list, pos_lng_list, strenght_list):
    strenght_all = reduce(lambda acc, val: acc + val, strenght_list)
    pos_lat_tower = 0
    for i in range(len(pos_lat_list)):
        pos_lat_tower += (pos_lat_list[i] * (strenght_list[i]/strenght_all))
    pos_lng_tower = 0
    for i in range(len(pos_lng_list)):
        pos_lng_tower += (pos_lng_list[i] * (strenght_list[i]/strenght_all))
    return pos_lat_tower, pos_lng_tower

if __name__ == "__main__":
    pos_lat_list = [28.189260450000006,
                    28.195777477777824,
                    28.19577164444445,
                    28.189013391625167,
                    28.1890133916252,
                    28.1890133916252,
                    28.18255]
    pos_lng_list = [-25.868423,
                    -25.8616442888889,
                    -25.8663650111111,
                    -25.8583868203475,
                    -25.8583868203475,
                    -25.8583868203475,
                    -25.87912]
    strenght_list = [-82, -85, -90, -91, -93, -94, -99]

    triangulater(pos_lat_list, pos_lng_list, strenght_list)
