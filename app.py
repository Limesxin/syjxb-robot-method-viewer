import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="设备操作文档", layout="wide")
st.title("📱 设备操作指引")

file_path = "method.pdf"

# 依然保留兜底按钮，防止极个别老旧机型不兼容
with open(file_path, "rb") as pdf_file:
    st.download_button(
        label="📥 备用通道：点击使用手机自带阅读器打开",
        data=pdf_file,
        file_name="method.pdf",
        mime="application/pdf"
    )

st.divider()

# 使用专门的 pdf_viewer 组件替代之前的 display_pdf 函数
# width=700 可以让它在电脑端看起来大小合适，在手机端会自动适应屏幕宽度
pdf_viewer(file_path, width=700)