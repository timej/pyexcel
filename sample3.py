"""クロステーブルを入力用テーブルに変換"""
import pandas as pd

# Excelファイルの読み込み。2行をヘッダー及び2列をインデックス列に指定
df = pd.read_excel('data/sample3.xlsx', header=[0, 1], index_col=[0, 1])
# 計の行と列を除く
df = df.iloc[:-2, :-2]

# イテレータを使って1列に並べる
sr = pd.Series()
for index_id, row in df.iterrows():
    row.index = row.index.map(lambda x, i=index_id: i + x)
    sr = sr.append(row)
sr = sr.dropna()

# インデックスがtuppleになっているので、マルチインデックスに直す
sr.index = pd.MultiIndex.from_tuples(sr.index)
# Excelファイルに書き込み
sr.to_excel('data/sample3_result.xlsx')
# クリップボードにペーストできます
sr.to_clipboard()

# Qiitaの記事と同じ形式（タイトル無し、前の行と同じ項目名でも表示）
df2 = pd.DataFrame(sr)
df2 = df2.reset_index()
df2.to_excel('data/sample3_result2.xlsx', header=False, index=False)
