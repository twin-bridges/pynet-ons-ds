from subproc_func import subprocess_wrapper
import re

cmd_list = ["df", "-h"]
std_out, std_err, return_code = subprocess_wrapper(cmd_list)

output = re.sub(r"Filesystem.*on", "", std_out)
match = re.findall(r"^(\S+)\s*.*?(\d+%)\s.*$", output, flags=re.M)

my_list = []
for file_system, usage in match:
    new_dict = {}
    new_dict["filesystem"] = file_system
    new_dict["usage"] = usage
    my_list.append(new_dict)

print(my_list)
