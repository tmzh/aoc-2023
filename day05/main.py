from utils import parse_challenge, paras, matches_to_list


class AlmanacMap:
    def __init__(self):
        self.forward_map = {}
        self.reverse_map = {}

    def update(self, src, size, dst):
        self.forward_map[range(src, src + size)] = dst
        self.reverse_map[range(dst, dst + size)] = src

    def list_endpoints(self):
        endpoints = {0}
        for r in self.forward_map.keys():
            endpoints.update([r.start - 1, r.start, r.stop - 1, r.stop])
        return endpoints

    def values(self):
        return self.forward_map.values()

    def lookup(self, item):
        for r in self.forward_map.keys():
            if item in r:
                return self.forward_map[r] + item - r.start
        else:
            return item

    def reverse_lookup(self, item):
        for r in self.reverse_map.keys():
            if item in r:
                return self.reverse_map[r] + item - r.start
        else:
            return item


def parse_seeds(section):
    return matches_to_list(section, r'\d+', int)


def parse_map(lines):
    m = AlmanacMap()
    for line in lines:
        dest, source, size = matches_to_list(line, r'\d+', int)
        m.update(source, size, dest)
    return m


def parse_almanac(sections):
    maps = {}
    for section in sections:
        if 'seeds:' in section:
            seeds = parse_seeds(section)
        else:
            section = section.splitlines()
            name = section[0].replace(' map:', '')
            maps[name] = parse_map(section[1:])
    return seeds, maps


def get_location(seed, d):
    soil = d['seed-to-soil'].lookup(seed)
    fertilizer = d['soil-to-fertilizer'].lookup(soil)
    water = d['fertilizer-to-water'].lookup(fertilizer)
    light = d['water-to-light'].lookup(water)
    temperature = d['light-to-temperature'].lookup(light)
    humidity = d['temperature-to-humidity'].lookup(temperature)
    location = d['humidity-to-location'].lookup(humidity)
    return location


def get_endpoints(d: dict):
    reverse_maps = ['temperature-to-humidity',
                    'light-to-temperature', 'water-to-light',
                    'fertilizer-to-water', 'soil-to-fertilizer',
                    'seed-to-soil']
    endpoints = d['humidity-to-location'].list_endpoints()
    for m in reverse_maps:
        new_endpoints = d[m].list_endpoints()
        for ep in endpoints:
            new_endpoints.add(d[m].reverse_lookup(ep))
        endpoints = new_endpoints
    return new_endpoints


def get_part_2_seeds(seeds, endpoint_seeds):
    part_2_seeds = []
    for seed in endpoint_seeds:
        for i, start in enumerate(seeds[::2]):
            size = seeds[i * 2 + 1]
            if start <= seed < (start + size):
                part_2_seeds.append(seed)
    return part_2_seeds


if __name__ == '__main__':
    almanac = parse_challenge(5, sections=paras)
    seeds, maps = parse_almanac(almanac)
    print("Part 1: ", min(get_location(seed, maps) for seed in seeds))
    endpoint_seeds = get_endpoints(maps)
    print("Part 2: ",
          min(get_location(seed, maps) for seed in   get_part_2_seeds(seeds, endpoint_seeds)))
