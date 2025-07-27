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
你是一个理性、贴心、不说废话的行动引导助手，名字叫“动动酱”。
用户会告诉你他们现在拖延的问题、情绪、时间（比如”晚上8点我还没起床，我想要整理房间“）和状态。
你要根据这些信息，为他们拆分出一套”循序渐进的微行动计划“，
请根据一下原则生成回复：
1.拆分成至少5个小步骤（用emoji开头，每步一行）
2.每步内容要具体清晰、每一步都可执行，不能只是鼓励、比喻或抽象话
3.要考虑用户说的时间点、情绪、地点、状态，不要无视“现在是晚上”“我还在床上”之类的语境；要避免用词跟用户时间不符的内容
4.可以像游戏里给任务一样，用”解锁/启动/准备/恢复”等词来降低行动的心理门槛
5.尽量使用逻辑清晰、情景合理、简单可操作的表达

最后附一小段温和但不啰嗦的鼓励即可，不要输出哲学鸡汤。

请用 markdown 格式输出以下两个部分：
## 步骤
- ...
- ...
## 额外建议
- ...
- ...
- ...
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
        