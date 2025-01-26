#!/usr/bin/env python3

from crewai import Crew, Agent, Task
from crewai.process import Process
from crewai.tasks.output_format import OutputFormat

def run_manual_task_order():
    """
    展示如何手动设定任务执行顺序的示例。
    通过明确指定任务依赖关系和使用 Process.sequential 来控制执行顺序。
    """
    # Step 1: 创建三个测试用 Agent
    researcher = Agent(
        role="研究员",
        goal="收集并汇总市场数据",
        backstory="擅长从各种渠道获取市场信息和数据"
    )
    
    analyst = Agent(
        role="分析师",
        goal="分析市场数据中的趋势和洞察",
        backstory="专注于数据分析和趋势预测"
    )
    
    writer = Agent(
        role="作者",
        goal="撰写调查报告并提供最终结论",
        backstory="善于整合信息并撰写专业报告"
    )

    # Step 2: 创建任务并明确指定执行顺序
    task1 = Task(
        description="收集过去一年的市场数据",
        agent=researcher,
        expected_output="整理好的市场数据清单",
        output_format=OutputFormat.RAW
    )

    task2 = Task(
        description="分析市场数据中的关键趋势",
        agent=analyst,
        expected_output="市场趋势分析报告",
        output_format=OutputFormat.RAW,
        context=[task1]  # 依赖第一个任务的输出
    )

    task3 = Task(
        description="撰写最终市场分析报告",
        agent=writer,
        expected_output="完整的市场分析报告",
        output_format=OutputFormat.RAW,
        context=[task2]  # 依赖第二个任务的输出
    )

    # Step 3: 创建 Crew 并指定顺序执行
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[task1, task2, task3],
        process=Process.sequential,  # 明确指定顺序执行
        verbose=True
    )

    # Step 4: 执行任务并获取结果
    result = crew.kickoff()
    print("\n最终结果:")
    print(result.raw)

if __name__ == "__main__":
    run_manual_task_order()
