import re


class HandyHaversacks:
    __contained_bags_format = '[\d]+ ([a-z]+ [a-z]+) bag[s]?'
    __container_bag_format = '^([a-z]+ [a-z]+) bag'

    def __init__(self, rules):
        self.__bags_list = {}
        for rule in rules:
            parsed_rule = self.__parse_rule_to_entry(rule)
            for contained in parsed_rule[1]:
                if contained not in self.__bags_list:
                    self.__bags_list[contained] = [parsed_rule[0]]
                else:
                    self.__bags_list[contained].append(parsed_rule[0])

    def __parse_rule_to_entry(self, rule) -> (str, [str]):
        container_bag = re.findall(self.__container_bag_format, rule)[0]
        contained_bags = re.findall(self.__contained_bags_format, rule)
        return container_bag, contained_bags

    def count_valid_outermost_bags(self, contained_bag):
        return len(self.__get_outermost_bags(contained_bag))

    def __get_outermost_bags(self,contained_bag):
        outer_bags = set(self.__bags_list[contained_bag]).copy()
        acc = outer_bags
        for outer_bag in outer_bags:
            if outer_bag in self.__bags_list:
                acc = acc.union(self.__get_outermost_bags(outer_bag))
        return acc

class HandyHaversacks2:
    __contained_bags_format = '(\d)+ ([a-z]+ [a-z]+) bag[s]?'
    __container_bag_format = '^([a-z]+ [a-z]+) bag'

    def __init__(self, rules):
        self.__bags_map = {}
        for rule in rules:
            parsed_rule = self.__parse_rule_to_entry(rule)
            self.__bags_map[parsed_rule[0]] = parsed_rule[1]

    def __parse_rule_to_entry(self, rule) -> (str, (str,str)):
        container_bag = re.findall(self.__container_bag_format, rule)[0]
        contained_bags = re.findall(self.__contained_bags_format, rule)
        return container_bag, contained_bags

    def count_inner_bags(self, container_bag):
        if container_bag not in self.__bags_map:
            return 0

        acc = 0
        for contained_bag in self.__bags_map[container_bag]:
            amount_contained = int(contained_bag[0])
            acc += amount_contained + amount_contained*self.count_inner_bags(contained_bag[1])

        return acc