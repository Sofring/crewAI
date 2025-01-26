#!/usr/bin/env python3

from crewai import Crew, Agent, Task
from crewai.process import Process
from crewai.tasks.output_format import OutputFormat

def run_planning_demo():
    # Step A: 创建三个测试用 Agent
    researcher = Agent(
        role="研究员",
        goal="收集并汇总市场数据",
        backstory="喜欢从各种线上渠道获取信息"
    )
    analyst = Agent(
        role="分析师",
        goal="分析市场数据中的趋势和洞察",
        backstory="熟悉数据挖掘与可视化"
    )
    writer = Agent(
        role="作者",
        goal="撰写调查报告并提供最终结论",
        backstory="擅长文字组织和总结"
    )

    # Step B: 定义初始任务顺序
    tasks = [
        Task(
            description="收集市场数据",
            agent=researcher,
            expected_output="列出收集到的市场信息",
            output_format=OutputFormat.RAW,
        ),
        Task(
            description="分析数据并得出关键趋势",
            agent=analyst,
            expected_output="列出主要分析结论",
            output_format=OutputFormat.RAW,
        ),
        Task(
            description="总结并撰写正式报告",
            agent=writer,
            expected_output="带有主观分析和结论的调查报告",
            output_format=OutputFormat.RAW,
        )
    ]

    # Step C: 通过设置 planning=True 来激活规划功能
    crew = Crew(
        name="Planning Demo Crew",
        agents=[researcher, analyst, writer],
        tasks=tasks,
        process=Process.sequential,
        planning=True,            # 启用 Planning
        planning_llm="gpt-4",     # 指定用于规划的 LLM
        verbose=True
    )

    # Step D: 执行 kickoff，自动生成并打印规划结果
    result = crew.kickoff()
    print("执行结果:")
    print(result.raw)

if __name__ == "__main__":
    run_planning_demo()
