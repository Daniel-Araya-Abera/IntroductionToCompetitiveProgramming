class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_list = a.split("+")
        b_list = b.split("+")
        
        normal_a, complex_a = int(a_list[0]), int(a_list[1][:len(a_list[1]) - 1])
        normal_b, complex_b = int(b_list[0]), int(b_list[1][:len(b_list[1]) - 1])
        
        
        # print("normal complex ", normal_a, " and ", complex_a)
        # print("normal complex ", normal_b, " and ", complex_b)
        
        normal_res = normal_a * normal_b -(complex_a * complex_b)
        complex_res = normal_a * complex_b + normal_b * complex_a
        
        return str(normal_res) + "+" + str(complex_res) + "i"
        