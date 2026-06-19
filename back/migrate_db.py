'''临时修改数据库'''
import sqlite3
conn = sqlite3.connect('notebook.db')
cursor = conn.cursor()
print("正在修改数据库...")
# 修改note表
try:
    cursor.execute("ALTER TABLE notes ADD COLUMN is_deleted INTEGER DEFAULT 0")
    print("已成功添加is_deleted字段到notes表")
except sqlite3.OperationalError as e:
    print(f"修改notes表失败: {e}")

# 修改Todos表
try:
    cursor.execute("ALTER TABLE todos ADD COLUMN tomato_count INTEGER DEFAULT 0")
    cursor.execute("ALTER TABLE todos ADD COLUMN parent_id INTEGER")
    cursor.execute("ALTER TABLE todos ADD COLUMN is_deleted INTEGER DEFAULT 0")
    print("已成功添加tomato_count和parent_id字段以及is_deleted字段到todos表")
except sqlite3.OperationalError as e:
    print(f"修改todos表失败: {e}")
conn.commit()
cursor.close()
conn.close()
print("数据库修改完成！")
