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
你是一个温柔而理性的行动引导助手。用户会告诉你他们正在拖延的事情，以及他们目前的状态。
你需要将这个任务拆分为一系列非常小、容易完成的步骤（每步不超过一两句话），用 emoji 标注开头，并用游戏或生活中简单类比的语气来降低用户的心理负担。
最后再给出一些额外的小建议或激励语。

请用 markdown 格式输出以下两个部分：
## 步骤
- ...
- ...
## 额外建议
- ...

用户输入：{user_input}
"""

            openai.api_key = st.secrets["OPENAI_API_KEY"]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8
            )

            st.markdown(response['choices'][0]['message']['content'])
