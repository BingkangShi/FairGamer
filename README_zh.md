[中文](README_zh.md) | [English](README.md)

论文地址：https://arxiv.org/abs/2508.17825

> [!IMPORTANT]
> 1. 本项目在进行大量异步测试时会并发调用 LLM API。您需要参考 API 提供方提供的每分钟请求数（RPM）上限，设置合理的请求量，以免出现大量 RPM 或 TPM 超额报错。若因此被 API 提供方视为 DDoS 攻击行为，本开源评测项目不承担责任。
> 2. 若 API 提供方提供 KV cache 命中、记忆功能或类似选项，请关闭它们，以获得 LLM 在决策偏好方面最真实的能力评测结果。

# 简介

FairGamer：首个用于评估 LLM 游戏 NPC 在交易、合作和竞争三种交互模式中社会偏见（阶层、种族、年龄和国籍）的基准。

本仓库属于会议论文《FairGamer: Evaluating Social Biases in LLM-Based Video Game NPCs》。

NPC 交互中的社会偏见构想：
<div align="center">
  <img src="img/Conception.png" alt="Conception of social biases in interactions between NPCs" width="800" />
</div>

FairGamer 基准评测流程：
<div align="center">
  <img src="img/pipeline_v2.png" alt="FairGamer Benchmark Evaluation Pipeline" width="800" />
</div>

# 使用方法

我们建议您使用 asyncio 和 AsyncOpenAI 库运行 FairGamer 评测程序，因为该程序使用异步请求进行 API 测试。

## 安装

您需要确保 Python 版本 >= 3.9，并安装 requirements.txt 中的 Python 依赖：
```bash
pip install -r requirements.txt
```

## 评测

我们评测了以下模型：**GPT-4.1**、**Grok-4**、**Grok-4-fast**、**DeepSeek-V3.2**、**Qwen2.5-72B**、**Llama3.3-70B**、**Llama3.1-8B**

### 评测：交易（Tr）
以 DeepSeek-V3.2 为例，在命令行中执行以下命令：
```bash
cd FairGamer/Trade
python eval_all_Tr.py --config "./config_dsv3.json"
```
LLM 的输出决策会被提取为 json，平均后的 json 输出会记录在 FairGamer/Trade/record/Tr_deepseek-chat_analysis.json 文件中。

在完成全部 7 个模型的交易模式评测后，执行以下命令：
```bash
cd FairGamer/Trade
python mcv_Tr.py"
```
随后您将在命令行中获得具体的 FairMCV 结果。

### 评测：合作（Coo）
与交易模式类似，若要测试合作模式，需要运行以下命令：
```bash
cd FairGamer/Cooperation
python eval_all_Coo.py --config "./config_dsv3.json"
python mcv_Coo.py"
```

### 评测：竞争（Com）
与交易模式类似，若要测试竞争模式，需要运行以下命令：
```bash
cd FairGamer/Competition
python eval_all_Com.py --config "./config_dsv3.json"
python mcv_Com.py"
```

最终测试结果如下表所示（英文数据）：
<div align="center">
  <img src="img/FairMCV_Score.png" alt="FairGamer Benchmark Results" width="800" />
</div>

为清晰起见，FairMCV 分数高于 95% 的 LLM 被解释为足够公平且无偏见的模型。

## 分析

我们分别按交互模式和偏见类型对实验结果取平均，得到以下结果：

<div align="center">
<table>
<tr>
<td align="center"><img src="img/inter_bar_chart_en.png" alt="HeatMap of task SNPCV (DeepSeek-V3)" width="95%" /></td>
<td align="center"><img src="img/bias_bar_chart_en.png" alt="HeatMap of task SNPCV (DeepSeek-V3)" width="95%" /></td>
</tr>
<tr>
<td align="center">（a）3 种交互场景（英文数据）下的公平性表现：交易（Tr）、合作（Coo）和竞争（Com）。</td>
<td align="center">（b）4 种社会偏见类型（英文数据）下的模型公平性表现：
阶层、种族、年龄和国籍。</td>
</tr>
</table>
</div>

<div align="center">
<table>
<tr>
<td align="center"><img src="img/inter_bar_chart_zh.png" alt="HeatMap of task SNPCV (DeepSeek-V3)" width="95%" /></td>
<td align="center"><img src="img/bias_bar_chart_zh.png" alt="HeatMap of task SNPCV (DeepSeek-V3)" width="95%" /></td>
</tr>
<tr>
<td align="center">（c）3 种交互场景（中文数据）下的公平性表现：交易（Tr）、合作（Coo）和竞争（Com）。</td>
<td align="center">（d）4 种社会偏见类型（中文数据）下的模型公平性表现：
阶层、种族、年龄和国籍。</td>
</tr>
</table>
</div>

图（a）和图（c）在一定程度上反映了不同模型在三种交互模式中暴露出的偏见差异。同时，图（b）和图（d）展示了这些模型在具体类别上的偏见程度。请注意，在上述四张图中，数值越高表示模型越公平。

## FairMCV 的设计理念

我们提出的公平性指标 FairMCV 试图将模型输出的公平性与收敛性联系起来。当 LLM 处理与角色设定（Role Information）无关的任务时，在理想公平条件下，其决策应在不同角色之间保持一致。在这种情况下，模型的决策输出应当具有收敛性，即输出一致性越高，公平性越强。

## Cite the project

```bibtex
@article{shi2025fairgamer,
  title={Fairgamer: Evaluating biases in the application of large language models to video games},
  author={Shi, Bingkang and Huang, Jen-tse and Li, Guoyi and Zhang, Xiaodan and Yao, Zhongjiang},
  journal={arXiv preprint arXiv:2508.17825},
  year={2025}
}
```
