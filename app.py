import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# 设置页面配置，使布局适应手机屏幕
st.set_page_config(page_title="设备操作文档", layout="wide")
st.title("📱 设备操作指引")

file_path = "method.pdf"

# 保留备用下载/打开按钮，方便学生直接调用手机自带的阅读器
with open(file_path, "rb") as pdf_file:
    st.download_button(
        label="📥 备用通道：点击使用手机自带阅读器打开",
        data=pdf_file,
        file_name="method.pdf",
        mime="application/pdf"
    )

st.divider()

# 使用专用组件渲染 PDF，它会自动将每一页转换为适应手机屏幕宽度的页面
pdf_viewer(file_path)