from google_play_scraper import reviews_all, Sort
import pandas as pd

scrapreview = reviews_all(
    'com.mobile.legends',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=3000  
)

df = pd.DataFrame(scrapreview)
df.to_csv('ulasan_aplikasi.csv', index=False)

print("Scraping selesai")
print("Jumlah data:", df.shape)