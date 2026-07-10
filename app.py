import streamlit as st
import base64

# 设置页面配置，适应手机端浏览
st.set_page_config(page_title="设备操作文档", layout="wide")
st.title("📱 设备操作指引")

file_path = "method.pdf"

# 1. 提供备用下载按钮（为了兼容部分无法直接预览的手机浏览器）
with open(file_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📥 如果下方无法预览，请点击这里下载/打开文档",
    data=PDFbyte,
    file_name="method.pdf",
    mime="application/pdf"
)

st.divider()

# 2. 将 PDF 转换为 Base64 编码并内嵌展示
def display_pdf(path):
    with open(path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # 使用 iframe 嵌入 PDF
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

display_pdf(file_path)