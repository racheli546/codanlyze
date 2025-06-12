import matplotlib.pyplot as plt
from io import BytesIO
import Testing_quality_code as T


def create_lengths_list(dict):
   all_lengths = find_key_in_dict(dict,"func_length")
   return create_histogram(all_lengths)

def create_issue_dict(data):
    issue_dict= {
        "Long Functions": sum(1 for i in find_key_in_dict(data, "func_length") if i > 20),
        "Large Files": sum(1 for i in find_key_in_dict(data, "len") if i > 120),
        "Missing Docstrings": sum(1 for i in find_key_in_dict(data, "is_docstring") if not i),
        "Undefined Variables": sum(len(i) for i in find_key_in_dict(data, "list_undefined")),
        }
    return create_issue_pie(issue_dict)


def find_sum_issue(dict_file):
    sum_all = 0
    sum_all +=sum(1 for i in find_key_in_dict(dict_file, "func_length") if i > 20)
    sum_all += sum(1 for i in find_key_in_dict(dict_file, "len") if i > 120)
    sum_all+= sum(1 for i in find_key_in_dict(dict_file, "is_docstring") if not i)
    sum_all += sum(len(i) for i in find_key_in_dict(dict_file, "list_undefined"))
    return sum_all


def create_list_sum_issue(data):
    file_data_values = {}
    for fileName, file in data.items():  # בלי [0]
        file_data_values[fileName] = find_sum_issue(file)
    return create_bar_sum_issue_for_file(file_data_values)



def create_histogram(lengths):
    # להבטיח שכל האורכים הם מספרים שלמים
    lengths_int = [int(x) for x in lengths]
    plt.figure(figsize=(8, 5))
    plt.hist(lengths_int, bins=10, color='skyblue', edgecolor='black')
    plt.title("Function Length Distribution")
    plt.xlabel("Function Length (lines)")
    plt.ylabel("Number of Functions")
    plt.grid(True)
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf




def find_key_in_dict(d, target_key):
    if isinstance(d, dict):
        for key, value in d.items():
            if key == target_key:
                yield value
            else:
                yield from find_key_in_dict(value, target_key)
    elif isinstance(d, list):
        for item in d:
            yield from find_key_in_dict(item, target_key)



#create_lengths_list(T.analzye_code(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\witProject\classes"))

def create_issue_pie(dict_issue):
    plt.figure(figsize=(7,7))
    plt.pie(dict_issue.values(), labels=dict_issue.keys(), autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title('Number of Issues by Type')
    plt.axis('equal')  # כדי שהעוגה תוצג כעיגול מושלם
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf



def create_bar_sum_issue_for_file(dict_files):
    plt.figure(figsize=(7, 7))
    keys = list(dict_files.keys())
    values = list(dict_files.values())
    bars = plt.bar(keys, values, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, int(yval), ha='center', va='bottom')
    plt.title("Summary of Issues in Code")
    plt.xlabel("Issue Type")
    plt.ylabel("Count")
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf



def create_diagram(folder_path):
    data = T.analzye_code(folder_path)
    dict_img = {"lengths_list": create_lengths_list(data), "issue_dict": create_issue_dict(data),
                "list_sum_issue": create_list_sum_issue(data)}
    return dict_img

print(create_diagram(r"C:\Users\user1\Documents\תיכנות\שנה ב\סמסטר א\Pyton\witProject\classes"))
