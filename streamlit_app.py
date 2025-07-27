import streamlit as st
import openai

# 设置标题
st.set_page_config(page_title="StepEase 动动酱", layout="centered")
st.title("🪄 StepEase · 拖延拆解助手")
st.write("输入你现在在拖延的事，动动酱会帮你拆解步骤！")

# 输入框
user_input = st.text_area("😴 你现在卡在哪？", placeholder="比如：我现在躺在床上，想整理房间", height=150)

# 当点击按钮时执行
if st.button("💡 创建计划"):
    if user_input.strip() == "":
        st.warning("请输入内容哦")
    else:
        with st.spinner("动动酱正在努力拆解中..."):
            prompt = f"""
你是一个温柔而理性的行动引导助手，名字叫“动动酱”。
用户会告诉你他们现在正在拖延的事情，卡住的原因，以及他们目前的状态（时间、情绪、行为等）。
你的任务是根据用户的输入，为他们拆分出一套”循序渐进的微行动计划“。

请根据一下原则生成回复：
1.拆分成至少5个小步骤（用emoji开头，每步一行）
2.每步内容要具体清晰、可以立刻行动，避免空泛指令
3.要考虑用户说的时间点、情绪、地点、状态，不要无视“现在是晚上”“我还在床上”之类的语境
4.可以用比喻（比如”像游戏里按下技能键“”像给角色回血“）来降低心理负担
5.最后可以给一段温柔地激励（但不要强硬或贬低用户）

请用 markdown 格式输出以下两个部分：
## 步骤
- ...
- ...
## 额外建议
- ...

用户输入：{user_input}
"""

            client = openai.OpenAI(
                api_key=st.secrets["OPENAI_API_KEY"]
            )

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8
            )

            output = response.choices[0].message.content
            output = output.replace("。", "。<br>")
            st.markdown(output, unsafe_allow_html=True)
        