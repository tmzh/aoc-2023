from day05.main import *
from unittest import TestCase


class Test(TestCase):
    sample_input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''
    almanac = parse_challenge(sample_input, sections=paras)

    def test_parse_almanac(self):
        seeds, maps = parse_almanac(self.almanac)
        self.assertEqual(seeds, [79, 14, 55, 13])

    def test_get_endpoints(self):
        _, maps = parse_almanac(self.almanac)
        self.assertEqual(get_endpoints(maps),
                         {-1, 0, 13, 14, 15, 21, 22, 25, 26, 43, 44, 49, 50, 51, 52, 53, 54, 58, 59, 61, 62, 65, 66, 68,
                          69, 70, 71, 81, 82, 91, 92, 93, 97, 98, 99, 100})

    def test_get_location(self):
        seeds, maps = parse_almanac(self.almanac)
        for seed, location in (
                [79, 82],
                [14, 43],
                [55, 86],
                [13, 35],
        ):
            self.assertEqual(get_location(seed, maps), location)

    def test_get_part_2_seeds(self):
        self.assertEqual(27, len(get_part_2_seeds([79, 14, 55, 13], range(100))))

    def test_part_2(self):
        seeds, maps = parse_almanac(self.almanac)
        endpoint_seeds = get_endpoints(maps)
        self.assertEqual(min(get_location(seed, maps) for seed in  get_part_2_seeds(seeds, endpoint_seeds)), 46)




class TestAlmanacMap(TestCase):
    m = AlmanacMap()
    m.update(98, 2, 50)

    def test_keys(self):
        m = AlmanacMap()
        m.update(56, 37, 60)
        m.update(93, 4, 56)
        self.assertEquals(m.list_endpoints(), {0, 96, 97, 55, 56, 92, 93})

    def test_lookup(self):
        self.assertEquals(self.m.lookup(98), 50)
        self.assertEquals(self.m.lookup(99), 51)

    def test_reverse_lookup(self):
        self.assertEquals(self.m.reverse_lookup(50), 98)
        self.assertEquals(self.m.reverse_lookup(51), 99)

