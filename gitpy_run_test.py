# -*- coding: utf-8 -*-
"""gitpy_run_test

Automatically generated by Colab.

Original file is located at
 https://colab.research.google.com/drive/1LfC5ZXCuoVLvzqDIYMI2nflSI9yFaRq7
"""

from openpyxl import load_workbook
from io import BytesIO
import subprocess
import os
import sys
import importlib

import streamlit as st

# GitHub リポジトリのクローン
REPO_NAME = 'please_run...'
REPO_URL = 'https://github.com/shintarotakasaki/please_run...'

if not os.path.exists(REPO_NAME):
    subprocess.run(['git', 'clone', REPO_URL])

# モジュールパスを追加
sys.path.append(REPO_NAME)

# 必要なモジュールを事前にインポート
try:
    xl_des = importlib.import_module('xl_des')
    pdf_des = importlib.import_module('pdf_des')
    pass
except ImportError as e:
    st.error(f"モジュールのインポートに失敗しました: {e}")
    st.stop()

st.title("伝票作成アプリ")

# 現在のディレクトリの名前と構成を表示
#def get_directory_structure(root_dir):
    #structure = {}
    #for root, dirs, files in os.walk(root_dir):
        #structure[root] = {"dirs": dirs, "files": files}
    #return structure

#current_dir = os.getcwd()
#st.write(f"Current Directory: {current_dir}")

#directory_structure = get_directory_structure(current_dir)
#for root, content in directory_structure.items():
    #st.write(f"Directory: {root}")
    #st.write("Subdirectories:")
    #st.write(content["dirs"])
    #st.write("Files:")
    #st.write(content["files"])

# ファイルアップローダー
uploaded_file = st.file_uploader("ファイルをアップロードしてください")

if uploaded_file is not None:
    file_mime = uploaded_file.type

    if file_mime == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        file = BytesIO(uploaded_file.getvalue())
        wb = load_workbook(filename=file)
        sheet = wb.active
        st.write(f"シートタイトル: {sheet.title}")

        # xl_des モジュールの関数を実行
        if hasattr(xl_des, 'main'):
            xl_des.main(uploaded_file)
            str_data() = xl_des.xl_data_upload(uploaded_file)
        else:
            st.warning("xl_des モジュールに 'main' 関数が見つかりません。")

    elif file_mime == 'application/pdf':
        st.write("PDFをアップロードしました")

        # pdf_des モジュールの関数を実行
        if hasattr(pdf_des, 'main'):
            pdf_des.main(uploaded_file)
            str_data = pdf_des.main(uploaded_file)
        else:
            st.warning("pdf_des モジュールに 'main' 関数が見つかりません。")

    else:
        st.write("エクセルファイル(.xlsx)またはPDFファイルをアップロードしてください")

    
