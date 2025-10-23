#!/usr/bin/env python3
"""
ACE 快速入门脚本
无需配置即可了解ACE的工作流程(使用模拟模式)
"""

import json
import os
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional


# 简化的数据结构
@dataclass
class Bullet:
    id: str
    section: str
    content: str
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


class MockACEDemo:
    """
    ACE演示版本 - 不需要API密钥
    展示三步工作流程的概念
    """

    def __init__(self):
        self.playbook_bullets = []

    def demonstrate_workflow(self):
        """演示ACE的完整工作流程"""
        print("\n" + "="*70)
        print("🎓 ACE (Agentic Context Engineering) 工作流程演示")
        print("="*70)

        # 示例任务
        task = "编写Python代码计算1到100之间所有偶数的和"

        print(f"\n📋 任务: {task}")
        print("\n" + "-"*70)

        # Step 1: Generator
        print("\n【步骤1: Generator - 生成器】")
        print("="*70)
        print("Generator的职责: 执行任务,生成并运行代码")
        print("\n生成的代码:")
        print("```python")
        generated_code = """# 计算1到100之间所有偶数的和
total = sum(i for i in range(1, 101) if i % 2 == 0)
print(f"偶数之和: {total}")"""
        print(generated_code)
        print("```")

        print("\n执行结果:")
        print("偶数之和: 2550")
        print("✅ 代码执行成功!")

        # Step 2: Reflector
        print("\n" + "-"*70)
        print("\n【步骤2: Reflector - 反思器】")
        print("="*70)
        print("Reflector的职责: 分析执行结果,提取见解")

        reflection = {
            "reasoning": "代码使用了生成器表达式和sum()函数,这是Python中计算序列和的惯用方法。代码简洁且效率高。",
            "error_identification": "代码执行成功,没有错误。方法选择恰当。",
            "root_cause_analysis": "使用了Pythonic的写法,利用了内置函数的优化。",
            "correct_approach": "对于过滤和求和任务,优先使用生成器表达式配合sum()函数,而不是显式的for循环。",
            "key_insight": "在Python中处理序列过滤和聚合时,使用生成器表达式 + 内置函数(sum, max, min等)比显式循环更简洁高效"
        }

        print("\n生成的反思:")
        for key, value in reflection.items():
            print(f"\n• {key}:")
            print(f"  {value}")

        print("\n💡 关键见解: " + reflection["key_insight"])

        # Step 3: Curator
        print("\n" + "-"*70)
        print("\n【步骤3: Curator - 策展人】")
        print("="*70)
        print("Curator的职责: 将见解整合为playbook更新")

        new_bullet = Bullet(
            id=f"bullet-{len(self.playbook_bullets):05d}",
            section="code_patterns",
            content="对于序列过滤求和任务,使用 sum(x for x in seq if condition) 而非显式for循环"
        )

        self.playbook_bullets.append(new_bullet)

        print(f"\n生成的更新操作:")
        print(f"• 操作类型: ADD")
        print(f"• 添加到章节: {new_bullet.section}")
        print(f"• 内容: {new_bullet.content}")
        print(f"• Bullet ID: {new_bullet.id}")

        print("\n✅ Playbook已更新!")
        print(f"📚 当前Playbook包含 {len(self.playbook_bullets)} 条知识")

        # 展示Playbook
        print("\n" + "="*70)
        print("📚 当前Playbook内容")
        print("="*70)

        if self.playbook_bullets:
            sections = {}
            for bullet in self.playbook_bullets:
                if bullet.section not in sections:
                    sections[bullet.section] = []
                sections[bullet.section].append(bullet)

            for section, bullets in sections.items():
                print(f"\n## {section.upper().replace('_', ' ')}")
                for bullet in bullets:
                    print(f"  [{bullet.id}] {bullet.content}")
        else:
            print("(空)")

        # 演示增量更新的优势
        print("\n" + "="*70)
        print("🎯 ACE的核心优势")
        print("="*70)

        advantages = [
            ("增量更新", "只添加新知识,不重写整个context,避免信息丢失"),
            ("结构化存储", "每条知识都有独立ID,可以精确追踪和更新"),
            ("防止坍缩", "不会像传统方法那样将context压缩成简短摘要"),
            ("可解释性", "每条知识都有明确来源,人类可读"),
            ("可扩展性", "随着长上下文模型发展,可以容纳更多知识")
        ]

        for title, desc in advantages:
            print(f"\n✅ {title}")
            print(f"   {desc}")

        # 下一步指引
        print("\n" + "="*70)
        print("🚀 下一步")
        print("="*70)
        print("\n要使用真实的ACE系统:")
        print("1. 安装依赖: pip install google-adk")
        print("2. 配置API: export GOOGLE_API_KEY='your-key'")
        print("3. 运行完整版: python ace_prototype.py")
        print("4. 查看文档: cat README_ACE.md")
        print("\n或运行测试套件: python test_ace.py")


def show_architecture():
    """展示ACE的架构图"""
    print("\n" + "="*70)
    print("🏗️  ACE 架构示意图")
    print("="*70)

    architecture = """
    ┌─────────────────┐
    │   用户任务      │
    │  "计算偶数和"   │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  Generator (生成器)                  │
    │  • 接收: 任务 + 当前Playbook        │
    │  • 处理: 生成并执行Python代码       │
    │  • 输出: 执行轨迹 + 结果            │
    └────────┬────────────────────────────┘
             │ trajectory
             ▼
    ┌─────────────────────────────────────┐
    │  Reflector (反思器)                 │
    │  • 接收: 执行轨迹 + 结果            │
    │  • 处理: 分析成功/失败原因          │
    │  • 输出: 结构化反思                 │
    │    - 错误识别                       │
    │    - 根因分析                       │
    │    - 正确方法                       │
    │    - 关键见解                       │
    └────────┬────────────────────────────┘
             │ insights
             ▼
    ┌─────────────────────────────────────┐
    │  Curator (策展人)                   │
    │  • 接收: 反思 + 当前Playbook        │
    │  • 处理: 识别新知识                 │
    │  • 输出: 增量更新操作               │
    │    - ADD: 添加新bullet             │
    │    - 避免重复                       │
    └────────┬────────────────────────────┘
             │ delta updates
             ▼
    ┌─────────────────────────────────────┐
    │  Playbook (知识库)                  │
    │  • 结构化bullets集合                │
    │  • 分section组织                    │
    │  • JSON格式持久化                   │
    │  • 支持检索和更新                   │
    └─────────────────────────────────────┘
             │
             └──────┐
                    │ (下次任务时使用)
                    ▼
             ┌─────────────┐
             │  新任务...  │
             └─────────────┘
    """
    print(architecture)


def show_comparison():
    """展示与传统方法的对比"""
    print("\n" + "="*70)
    print("⚖️  ACE vs 传统Prompt优化方法")
    print("="*70)

    comparison = """
    ┌────────────────────┬──────────────────┬──────────────────┐
    │      特性          │   传统方法       │      ACE         │
    ├────────────────────┼──────────────────┼──────────────────┤
    │  更新方式          │  整体重写        │  增量添加        │
    │  知识丢失          │  容易发生        │  有效避免        │
    │  Context长度       │  趋向变短        │  稳定增长        │
    │  可解释性          │  较差            │  高              │
    │  领域细节          │  易被压缩        │  完整保留        │
    │  扩展性            │  有限            │  好              │
    └────────────────────┴──────────────────┴──────────────────┘

    传统方法问题:
    ❌ Brevity Bias: 倾向于简洁,丢失领域知识
    ❌ Context Collapse: 迭代重写导致信息坍缩

    ACE解决方案:
    ✅ 增量更新: 只添加新内容,保留旧知识
    ✅ 结构化: 每个知识点独立管理
    ✅ Grow-and-Refine: 稳步增长 + 定期去重
    """
    print(comparison)


def main():
    """主函数"""
    print("\n" + "🌟"*35)
    print("欢迎使用 ACE 原型演示!")
    print("🌟"*35)

    demo = MockACEDemo()

    # 1. 展示架构
    show_architecture()

    input("\n按Enter继续查看工作流程演示...")

    # 2. 演示工作流程
    demo.demonstrate_workflow()

    input("\n按Enter继续查看对比分析...")

    # 3. 展示对比
    show_comparison()

    print("\n" + "="*70)
    print("✨ 演示完成!")
    print("="*70)
    print("\n这只是一个概念演示。真实的ACE系统会:")
    print("• 使用Google Gemini或其他LLM作为后端")
    print("• 自动执行真实的Python代码")
    print("• 智能分析成功和失败案例")
    print("• 持续积累和优化知识库")
    print("\n查看完整实现: ace_prototype.py")
    print("阅读详细文档: README_ACE.md")
    print("\n" + "="*70)


if __name__ == "__main__":
    main()
