class Solution:
    import sys
    sys.set_int_max_str_digits(0) # Prevents limit errors on massive integers
    
    def maxDepth(self, s: str) -> int:
        par_list = []

        for l in s:
            if l != ")" and l != "(":
                continue

            par_len = len(par_list)

            if l == ")":
                for e in reversed(range(par_len)):
                    if par_list[e] == -1:
                        par_list[e] = 0
                        break

            if l == "(":
                accounted = False
                
                #  WHY NOT THIS 
                # if par_len > 0 and all(x != -1 for x in par_list):
                #     par_list[0] = -1
                #     accounted = True
                #     break
                # else:
                #     for f in range(par_len):
                #         if par_list[f] == -1 and f + 1 < par_len and par_list[f + 1] != -1:
                #             par_list[f + 1] = -1
                #             accounted = True
                #             break 

                
                for f in range(par_len):
                    if par_list[f] == -1 and f + 1 < par_len and par_list[f + 1] != -1:
                        par_list[f + 1] = -1
                        accounted = True
                        break 
                    if all(x != -1 for x in par_list):
                        par_list[f] = -1
                        accounted = True
                        break


                if not accounted: par_list.append(-1)

        return len(par_list)





        