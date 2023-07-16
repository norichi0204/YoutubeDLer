from pytube import YouTube

# ダウンロードしたい動画のURL
url = input("ダウンロードしたい動画のURL > ")

yt = YouTube(url)

print('タイトル:', yt.title)
print('長さ:', yt.length, '秒')

yt.streams.get_highest_resolution().download()
print('ダウンロードが完了しました。')
