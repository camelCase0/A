import re

def find_and_replace(file_path):
    content=''
    with open(file_path, 'r') as file:
        content = file.read()
        res_content =''

        split_pattern1 = re.compile(r'\n\s*While\s+\d+\s*\n')
        split_pattern2 = re.compile(r'\n\s*For\s+\$.+=\s*\d+\s+To\s+\d+\n')
        parts1 = re.split(split_pattern1, content)
        w_list = [part for subpart in parts1 for part in split_pattern2.split(subpart)]
        # w_list = content.split("While")
        # w_list = [part for element in w_list for part in element.split('For')]
        print(w_list[236:240])
        t_list = []
        for i, w in enumerate(w_list):
            if(i == 0):
                res_content+=w
                continue

            var_rule = r'(^\$\S+)\s*=\s*(\d+)'
            var_dict={}
            if_rule = r'If\s(\$\S+)\s*=\s*(\d+)\s+Then'
            for wv in w_list[i-1].split('\n'):
                mach = re.search(var_rule,wv)
                if mach:
                    var_dict[mach.group(1)] = mach.group(2)

            var = re.search(if_rule,w)
            if var:
                var = var.group(1)
                # var_rule = re.compile(r'If\s'+var+r'\s*=\s*'+var_dict[var]+r'\s+Then')
                if var not in var_dict:
                    continue
                st_rule = r'If\s'+'\\'+var+r'\s*=\s*'+var_dict[var]+r'\s+Then'
                # print(f"Rule {st_rule} in BLOCK: BBB{w}BBB")

                start = re.search(st_rule,w).span()[1]
                end = w.find("ExitLoop")
                if end < 0:
                    continue
                res_content += w[start:end]
                # print(w[start:end])
                print(i)
        content = res_content

    with open(file_path+"deLOOP", 'w') as file:
        file.write(content)

find_and_replace("A")
