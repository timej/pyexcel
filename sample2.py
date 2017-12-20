import pandas as pd

# 入力ファイルを指定
path = 'data/sample2_lf.csv'
# 出力ファイルを措定
out = 'data/sample2_crlf.xlsx'

df = pd.read_csv(path, header=None, dtype=object)
df.to_excel(out, header=False, index=False)

# GDPのデータを内閣府のホームページからダウンロードしてみました
# http://www.esri.cao.go.jp/jp/sna/data/data_list/sokuhou/files/2017/qe173_2/gdemenuja.html
url1 = 'http://www.esri.cao.go.jp/jp/sna/data/data_list/sokuhou/files/2017/qe173_2/__icsFiles/afieldfile/2017/12/07/gaku-mg1732.csv'
df1 = pd.read_csv(url1, encoding='cp932', header=None)
print(df1)
