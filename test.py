directory = "D:\development\github\candybox\data"

import json
import os

  
# 使用例
directory_path = r"D:\development\github\candybox\data"
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r+', encoding='utf-8') as json_file:
                data = json.load(json_file)
                newData = {}
                for key, value in data.items():
                    newData[f"{key[0].lower()}{key[1:]}"] = value
                # 特定のキーが存在する場合、値を更新
                # if target_key in data:
                #     data[target_key] = new_value

                #     # ファイルの先頭に戻り、更新されたデータで上書き
                json_file.seek(0)
                json.dump(newData, json_file, indent=4, ensure_ascii=False)
                json_file.truncate()  # 余分なデータを削除
