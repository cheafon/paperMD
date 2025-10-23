# ACE 示例数据集

本目录包含用于测试ACE原型的示例任务。

## 文件说明

### simple_tasks.json

包含10个不同类别的简单编程任务,用于测试ACE的基本功能。

**任务类别:**

1. **mathematics** (数学计算)
   - 阶乘计算
   - 质数查找

2. **string_processing** (字符串处理)
   - 统计元音字母
   - 回文检测

3. **data_structures** (数据结构)
   - 列表操作
   - 字典操作
   - 排序算法

4. **file_operations** (文件操作)
   - 文件读写

5. **logic** (逻辑问题)
   - FizzBuzz问题

6. **functions** (函数实现)
   - GCD计算

## 使用方法

### 方式1: 使用脚本批量运行

```python
import json
from ace_prototype import ACEFramework

# 加载任务
with open('examples/simple_tasks.json', 'r') as f:
    data = json.load(f)

# 初始化ACE
ace = ACEFramework(playbook_path="./playbooks/simple_tasks.json")

# 运行所有任务
for task_data in data['tasks']:
    print(f"\n运行任务 {task_data['id']}: {task_data['category']}")
    ace.run_task(
        task=task_data['task'],
        ground_truth=task_data.get('ground_truth')
    )

# 查看最终的playbook
ace.print_playbook()
```

### 方式2: 运行单个任务

```python
from ace_prototype import ACEFramework

ace = ACEFramework()

# 选择一个任务
task = "Write Python code to calculate the factorial of 10 and print the result."
ground_truth = "3628800"

# 运行
result = ace.run_task(task, ground_truth)

# 查看结果
print(f"Success: {result['success']}")
print(f"Output: {result['generation']['output']}")
```

## 任务难度

- **easy**: 简单的单步操作,适合初始测试
- **medium**: 需要一定的算法知识或多步操作
- **hard**: (待添加) 复杂的多步骤任务

## 扩展建议

你可以添加自己的任务到这个JSON文件中,格式如下:

```json
{
  "id": "custom-001",
  "category": "your_category",
  "task": "具体的任务描述",
  "ground_truth": "预期的输出结果",
  "difficulty": "easy/medium/hard"
}
```

## 预期学习效果

随着ACE执行这些任务,playbook会逐步积累以下知识:

1. **通用策略**: 如何分解问题、处理边界情况
2. **代码模式**: 常用的Python代码片段和模式
3. **常见错误**: 经常出现的错误及其避免方法
4. **API使用**: 标准库的正确使用方式

经过10个任务后,playbook应该包含足够的知识来更高效地处理类似的新任务!
